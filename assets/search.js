/* search.js — client-side full-text search over search_index.json */
(function () {
  var IDX = null;
  function flatten(pages) {
    var out = [];
    pages.forEach(function (p) {
      (p.sections || []).forEach(function (s, i) {
        out.push({ file: p.file, title: p.title, part: p.part || "",
                   anchor: s.id || "", text: s.text || "",
                   head: (i === 0 ? p.title : s.head) || p.title });
      });
    });
    return out;
  }
  function search(docs, query) {
    var terms = query.toLowerCase().split(/\s+/).filter(Boolean);
    if (!terms.length) return [];
    return docs.map(function (d) {
      var hay = (d.head + " " + d.text).toLowerCase();
      var score = 0, first = -1;
      terms.forEach(function (t) {
        var idx = hay.indexOf(t);
        if (idx >= 0) {
          score += idx < 40 ? 3 : 1;
          score += Math.min((hay.split(t).length - 1), 5) * 0.4;
          if (first < 0) first = idx;
        } else score = -1e9;
      });
      return { d: d, score: score, first: first };
    }).filter(r => r.score > 0)
      .sort((a, b) => b.score - a.score)
      .slice(0, 40);
  }
  function snippet(text, pos, terms) {
    var start = Math.max(0, pos - 50), end = Math.min(text.length, pos + 160);
    var frag = (start > 0 ? "…" : "") + text.slice(start, end) + (end < text.length ? "…" : "");
    terms.forEach(function (t) {
      try {
        frag = frag.replace(new RegExp(t.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"), "gi"),
                           function (m) { return "<mark>" + m + "</mark>"; });
      } catch (e) {}
    });
    return frag;
  }
  function esc(s) { var d = document.createElement("div"); d.textContent = s; return d.innerHTML; }
  function run() {
    var q = new URLSearchParams(location.search).get("q") || "";
    document.getElementById("q").value = q;
    var box = document.getElementById("results");
    if (!q) { box.innerHTML = '<p class="stats">输入关键词开始搜索（支持多词）。</p>'; return; }
    if (!IDX) { box.innerHTML = '<p class="stats">索引加载中…</p>'; return; }
    var docs = flatten(IDX.pages);
    var terms = q.toLowerCase().split(/\s+/).filter(Boolean);
    var hits = search(docs, q);
    var html = '<p class="stats">共 ' + hits.length + ' 条结果（前 40 条）</p><div class="results">';
    hits.forEach(function (h) {
      var href = h.d.file + (h.d.anchor ? "#" + h.d.anchor : "");
      html += '<div class="result">' +
        '<a href="' + href + '">' + esc(h.d.title) + (h.d.anchor ? " · " + esc(h.d.head) : "") + "</a>" +
        '<div class="path">' + esc(h.d.part) + "</div>" +
        '<div class="snippet">' + snippet(h.d.text, h.first, terms) + "</div></div>";
    });
    box.innerHTML = html + "</div>";
  }
  fetch("search_index.json").then(r => r.json()).then(j => { IDX = j; run(); })
    .catch(() => { document.getElementById("results").innerHTML = '<p class="stats">索引加载失败。</p>'; });
  run();
})();
