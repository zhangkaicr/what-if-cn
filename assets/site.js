/* site.js — theme toggle + nav select + "/" search focus */
(function () {
  function init() {
    var saved = null;
    try { saved = localStorage.getItem("wi-theme"); } catch (e) {}
    if (!saved) saved = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
    document.documentElement.setAttribute("data-theme", saved);
    var btn = document.querySelector(".cw-nav .tbtn");
    if (btn) {
      btn.textContent = saved === "dark" ? "☀️" : "🌙";
      btn.addEventListener("click", function () {
        var cur = document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark";
        document.documentElement.setAttribute("data-theme", cur);
        try { localStorage.setItem("wi-theme", cur); } catch (e) {}
        btn.textContent = cur === "dark" ? "☀️" : "🌙";
      });
    }
    var sel = document.querySelector(".cw-nav select");
    if (sel) sel.addEventListener("change", function () { if (sel.value) location.href = sel.value; });
    var q = document.querySelector(".cw-nav input.q");
    if (q) q.addEventListener("keydown", function (e) {
      if (e.key === "Enter") {
        var base = q.getAttribute("data-base") || "";
        location.href = base + "search.html?q=" + encodeURIComponent(q.value);
      }
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "/" && q && document.activeElement !== q) { e.preventDefault(); q.focus(); }
    });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
