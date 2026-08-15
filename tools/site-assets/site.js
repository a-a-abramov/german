/* site.js — the word table's search and filters.
 *
 * Every row is already in the HTML, so the table works without this file; all this
 * does is hide rows. No fetch, no build step, no framework.
 */
(function () {
  "use strict";

  // A rail link into chunks.html targets a collapsed <details>; CSS cannot open one,
  // so a deep link would otherwise land on a closed box.
  function openTarget() {
    if (!location.hash) return;
    var el = document.getElementById(location.hash.slice(1));
    if (el && el.tagName === "DETAILS" && !el.open) {
      el.open = true;
      el.scrollIntoView();
    }
  }
  openTarget();
  window.addEventListener("hashchange", openTarget);

  var q = document.getElementById("q");
  var table = document.getElementById("words");
  var count = document.getElementById("count");
  if (!q || !table || !count) return;

  var rows = Array.prototype.slice.call(table.tBodies[0].rows);
  var active = Object.create(null);

  // same folding vocab.py uses: lowercase, umlauts stripped, ß = ss
  function fold(s) {
    return s.toLowerCase()
      .replace(/ß/g, "ss")
      .normalize("NFD").replace(/[̀-ͯ]/g, "");
  }

  function passes(row, needle) {
    if (needle && row.dataset.k.indexOf(needle) === -1) return false;
    if (active.target && row.dataset.kind !== "target") return false;
    if (active.glue && row.dataset.kind !== "glue") return false;
    if (active.used && row.dataset.used !== "1") return false;
    if (active.open && row.dataset.used !== "0") return false;
    if (active.written && row.dataset.w !== "1") return false;
    return true;
  }

  var timer;
  function apply() {
    var needle = fold(q.value.trim());
    var n = 0;
    for (var i = 0; i < rows.length; i++) {
      var ok = passes(rows[i], needle);
      rows[i].classList.toggle("hide", !ok);
      if (ok) n++;
    }
    count.textContent = n === rows.length
      ? n + " Wörter"
      : n + " von " + rows.length + " Wörtern";
  }

  q.addEventListener("input", function () {
    clearTimeout(timer);
    timer = setTimeout(apply, 90);
  });

  Array.prototype.forEach.call(document.querySelectorAll(".f"), function (btn) {
    btn.addEventListener("click", function () {
      var f = btn.dataset.f;
      active[f] = !active[f];
      // the pairs are mutually exclusive; turning one on releases its opposite
      var opposite = { target: "glue", glue: "target", used: "open", open: "used" }[f];
      if (active[f] && opposite) {
        active[opposite] = false;
        var other = document.querySelector('.f[data-f="' + opposite + '"]');
        if (other) other.classList.remove("on");
      }
      btn.classList.toggle("on", !!active[f]);
      apply();
    });
  });

  // "/" focuses the search box, the way every list you actually use behaves
  document.addEventListener("keydown", function (ev) {
    if (ev.key === "/" && document.activeElement !== q) {
      ev.preventDefault();
      q.focus();
      q.select();
    }
  });
})();
