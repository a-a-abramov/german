/* site.js — the reader's gloss tips, and the word table's search and filters.
 *
 * Both surfaces work without this file: every table row is already in the HTML, and a
 * gloss tip opens on hover and on keyboard focus from CSS alone. What needs script is
 * the touch case and the right edge of the screen. No fetch, no build step, no framework.
 */
(function () {
  "use strict";

  // ------------------------------------------------------------------ gloss tips
  //
  // A finger has no hover and cannot un-focus: tapping a word focused it, CSS opened
  // the tip, and nothing short of tapping a *different* word ever closed it again. So
  // the tap path is driven from here instead — one tip open at a time, and tapping the
  // same word, the page, or Escape closes it.
  //
  // Opening also clamps the tip back inside the viewport. It is absolutely positioned
  // at the word's left edge, so a word near the end of a line hangs its tip off the
  // right of the document — which makes the page scroll sideways and the sticky band
  // stop short of the edge.
  var open = null;

  function shut() {
    if (!open) return;
    open.classList.remove("open");
    open = null;
  }

  function show(tw) {
    var tip = tw.querySelector(".tip");
    if (!tip) return;
    tip.style.left = "0px";
    tw.classList.add("open");
    open = tw;
    var pad = 10;
    var box = tip.getBoundingClientRect();
    var over = box.right - (document.documentElement.clientWidth - pad);
    // never drag it so far left that it runs off the other side
    if (over > 0) tip.style.left = "-" + Math.min(over, Math.max(box.left - pad, 0)) + "px";
  }

  // Pointer events, not click: iOS Safari only bubbles a synthesised click up to the
  // document for elements it already considers clickable, and a marked word is a bare
  // <span>. Opening on pointer*up* rather than down, and only if the finger stayed put,
  // keeps a scroll that happens to start on a marked word from opening its gloss.
  if (document.querySelector(".tw")) {
    var down = null;

    document.addEventListener("pointerdown", function (ev) {
      down = { x: ev.clientX, y: ev.clientY };
    });

    document.addEventListener("pointerup", function (ev) {
      var start = down;
      down = null;
      if (!start) return;
      if (Math.abs(ev.clientX - start.x) > 8 || Math.abs(ev.clientY - start.y) > 8) return;
      var tw = ev.target.closest ? ev.target.closest(".tw") : null;
      var was = open;
      shut();
      if (tw && tw !== was) show(tw);
    });

    document.addEventListener("keydown", function (ev) {
      if (ev.key === "Escape") shut();
    });

    // the clamp is measured once, at open time — a rotation invalidates it
    window.addEventListener("resize", shut);
  }

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
