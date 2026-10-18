#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Create what-if-cn repo, push via git, enable Pages. PAT via env GH_PAT (never written to disk)."""
import os, json, subprocess, sys, urllib.request, time

REPO = "what-if-cn"
OWNER = "zhangkaicr"
ROOT = r"C:/WorkBuddy/what-if-cn"
TOKEN = os.environ.get("GH_PAT")
assert TOKEN, "set GH_PAT env var"
HDRS = {"Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28", "User-Agent": "what-if-cn-deploy"}

def api(method, path, body=None):
    req = urllib.request.Request(f"https://api.github.com{path}",
                                 data=json.dumps(body).encode() if body else None,
                                 headers=HDRS, method=method)
    try:
        with urllib.request.urlopen(req) as r:
            return r.status, json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read() or b"{}")

# 1) create repo if missing
code, _ = api("GET", f"/repos/{OWNER}/{REPO}")
if code != 200:
    code, data = api("POST", "/user/repos", {
        "name": REPO,
        "description": "《Causal Inference: What If》(Hernán & Robins) 全书中文翻译 · 在线阅读",
        "private": False, "has_issues": True, "has_wiki": False, "has_projects": False})
    print("create repo:", code, data.get("html_url", data.get("errors", data)))
else:
    print("repo exists")

# 2) git init & push
def run(cmd, **kw):
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, shell=True, **kw)
    print("$", cmd, "->", r.returncode)
    if r.stdout.strip(): print(r.stdout.strip()[-800:])
    if r.returncode != 0 and r.stderr.strip(): print(r.stderr.strip()[-800:])
    return r.returncode

tok_url = f"https://x-access-token:{TOKEN}@github.com/{OWNER}/{REPO}.git"
pub_url = f"https://github.com/{OWNER}/{REPO}.git"
if not os.path.exists(os.path.join(ROOT, ".git")):
    run("git init -b main")
run("git add -A")
run('git commit -m "《因果推断：What If》中文站 + 全书蒸馏 Skill 包（14 能力 / 8 入口）" || echo nothing-to-commit')
run("git remote remove origin || rem")
run(f"git remote add origin {tok_url}")
if run(f"git push -u origin main --force") == 0:
    print("pushed")
run("git remote remove origin")  # strip token from .git/config

# 3) enable Pages
code, data = api("POST", f"/repos/{OWNER}/{REPO}/pages",
                 {"source": {"branch": "main", "path": "/"}})
print("pages:", code, data.get("html_url", data.get("message", "")))
print("site will be at https://zhangkaicr.github.io/what-if-cn/")
