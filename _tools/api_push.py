# -*- coding: utf-8 -*-
"""通过 GitHub Git Data API 推送本地 HEAD 到远程 main。

用途：本沙箱的 git HTTPS 隧道不稳定（CONNECT tunnel failed, 502），
     而 urllib 访问 api.github.com 正常，因此走 API 完成提交。

做法：取远程 main 当前 commit → 以其为 parent 新建一个 commit
     （树 = 远程现有树 + 本次改动的文件）→ 更新 ref。
     只推送工作区中相对远程 HEAD 有改动的文件，不重放整个历史。

用法：GH_PAT=<token> python _tools/api_push.py [file1 file2 ...]
      不带参数时自动检测相对远程 HEAD 有改动的已跟踪文件。
"""
import base64
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request

OWNER = "zhangkaicr"
REPO = "what-if-cn"
ROOT = r"C:/WorkBuddy/what-if-cn"
TOKEN = os.environ.get("GH_PAT")
assert TOKEN, "set GH_PAT env var"

HDRS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
    "User-Agent": "what-if-cn-api-push",
}


def api(method, path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(
        f"https://api.github.com/repos/{OWNER}/{REPO}{path}",
        data=data, headers=HDRS, method=method,
    )
    try:
        with urllib.request.urlopen(req) as r:
            return r.status, json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read() or b"{}")


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)


def main() -> int:
    # 1) 远程 main 当前 commit
    code, ref = api("GET", "/git/ref/heads/main")
    if code != 200:
        print(f"[fail] 读 ref: {code} {ref}")
        return 1
    parent_sha = ref["object"]["sha"]

    code, parent_commit = api("GET", f"/git/commits/{parent_sha}")
    if code != 200:
        print(f"[fail] 读 parent commit: {code} {parent_commit}")
        return 1
    base_tree = parent_commit["tree"]["sha"]
    print(f"[info] 远程 main = {parent_sha[:10]}，base tree = {base_tree[:10]}")

    # 2) 确定要推送的文件
    if len(sys.argv) > 1:
        files = sys.argv[1:]
    else:
        r = git("diff", "--name-only", parent_sha)
        if r.returncode != 0:
            print(f"[fail] git diff: {r.stderr.strip()}")
            return 1
        files = [f for f in r.stdout.split() if f.strip()]
    if not files:
        print("[ok] 无改动需要推送")
        return 0
    print(f"[info] 待推送 {len(files)} 个文件: {' '.join(files)}")

    # 3) 为每个文件建 blob
    tree_entries = []
    for rel in files:
        path = os.path.join(ROOT, rel.replace("/", os.sep))
        if not os.path.exists(path):
            # 文件被删除：树条目不带 sha 即表示删除
            tree_entries.append({"path": rel, "mode": "100644", "type": "blob", "sha": None})
            continue
        raw = open(path, "rb").read()
        code, blob = api("POST", "/git/blobs", {
            "content": base64.b64encode(raw).decode(),
            "encoding": "base64",
        })
        if code != 201:
            print(f"[fail] blob {rel}: {code} {blob}")
            return 1
        tree_entries.append({
            "path": rel, "mode": "100644", "type": "blob", "sha": blob["sha"],
        })
        print(f"  blob ok  {rel}  ({len(raw)} B)")

    # 4) 建树（基于远程现有树，只覆盖改动项）
    code, tree = api("POST", "/git/trees", {"base_tree": base_tree, "tree": tree_entries})
    if code != 201:
        print(f"[fail] tree: {code} {tree}")
        return 1

    # 5) 建 commit
    code, commit = api("POST", "/git/commits", {
        "message": "README：补充占位页说明（13 章翻译进行中，站内无死链）",
        "tree": tree["sha"],
        "parents": [parent_sha],
    })
    if code != 201:
        print(f"[fail] commit: {code} {commit}")
        return 1

    # 6) 更新 ref
    code, upd = api("PATCH", "/git/refs/heads/main", {"sha": commit["sha"], "force": True})
    if code != 200:
        print(f"[fail] 更新 ref: {code} {upd}")
        return 1

    print(f"[ok] 已推送: {commit['sha'][:10]} -> main")
    print(f"     {upd.get('object', {}).get('sha', '')[:10]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
