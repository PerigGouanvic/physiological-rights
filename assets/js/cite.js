// Source pop-ups: a.cite[data-sid] opens the source record in a dialog.
// Without JavaScript the link simply leads to /sources/<sid>/.
(function () {
  var links = document.querySelectorAll('a.cite[data-sid]');
  if (!links.length || typeof HTMLDialogElement === 'undefined') return;

  var cache = {};
  function load(url) {
    if (!cache[url]) {
      cache[url] = fetch(url, { credentials: 'same-origin' })
        .then(function (r) { if (!r.ok) throw new Error(r.status); return r.text(); })
        .then(function (html) {
          var doc = new DOMParser().parseFromString(html, 'text/html');
          var card = doc.querySelector('.source-card');
          if (!card) throw new Error('no card');
          return card;
        });
      cache[url].catch(function () { delete cache[url]; });
    }
    return cache[url];
  }

  var dlg = document.createElement('dialog');
  dlg.className = 'cite-dialog';
  dlg.setAttribute('aria-labelledby', 'cite-dialog-title');
  dlg.innerHTML =
    '<div class="cd-bar"><span class="cd-num" id="cite-dialog-title"></span>' +
    '<button type="button" class="cd-close" aria-label="Close">×</button></div>' +
    '<div class="cd-body"></div>';
  document.body.appendChild(dlg);
  var body = dlg.querySelector('.cd-body');
  var num = dlg.querySelector('.cd-num');
  var opener = null;

  dlg.querySelector('.cd-close').addEventListener('click', function () { dlg.close(); });
  dlg.addEventListener('click', function (e) { if (e.target === dlg) dlg.close(); });
  dlg.addEventListener('close', function () {
    document.documentElement.classList.remove('cite-open');
    if (opener) opener.focus();
  });

  function render(card, link) {
    var c = card.cloneNode(true);
    var h = c.querySelector('h1');
    if (h) { var p = document.createElement('p'); p.className = h.className; p.innerHTML = h.innerHTML; h.replaceWith(p); }
    var kick = c.querySelector('.sc-kicker');
    if (kick) kick.remove();
    var keys = (link.getAttribute('data-ex') || '').split(',').map(function (k) { return k.trim(); }).filter(Boolean);
    var exs = Array.prototype.slice.call(c.querySelectorAll('.sc-ex'));
    exs.forEach(function (ex) { ex.removeAttribute('id'); });
    if (keys.length) {
      var rest = exs.filter(function (ex) { return keys.indexOf(ex.getAttribute('data-key')) < 0; });
      if (rest.length) {
        var det = document.createElement('details');
        det.className = 'sc-more';
        det.innerHTML = '<summary>Other passages from this source (' + rest.length + ')</summary>';
        rest.forEach(function (ex) { det.appendChild(ex); });
        var anchor = c.querySelector('.sc-note') || c.querySelector('.sc-links');
        c.insertBefore(det, anchor);
      }
      var sel = exs.filter(function (ex) { return keys.indexOf(ex.getAttribute('data-key')) >= 0; });
      sel.sort(function (a, b) { return keys.indexOf(a.getAttribute('data-key')) - keys.indexOf(b.getAttribute('data-key')); });
      var first = c.querySelector('.sc-ex, .sc-more, .sc-note, .sc-links');
      sel.forEach(function (ex) { c.insertBefore(ex, first); });
    }
    body.innerHTML = '';
    body.appendChild(c);
    body.scrollTop = 0;
  }

  function open(link) {
    opener = link;
    num.textContent = 'Source ' + link.textContent.trim();
    body.innerHTML = '<p class="cd-loading">Loading the source…</p>';
    document.documentElement.classList.add('cite-open');
    if (!dlg.open) dlg.showModal();
    var url = link.href.split('#')[0];
    load(url).then(function (card) { render(card, link); }, function () {
      body.innerHTML = '<p class="cd-loading">The source could not be loaded. <a href="' + url + '">Open its record</a>.</p>';
    });
  }

  Array.prototype.forEach.call(links, function (a) {
    a.addEventListener('click', function (e) {
      if (e.metaKey || e.ctrlKey || e.shiftKey || e.button === 1) return;
      e.preventDefault();
      open(a);
    });
    var pre = function () { load(a.href.split('#')[0]).catch(function () {}); };
    a.addEventListener('pointerenter', pre, { once: true });
    a.addEventListener('focus', pre, { once: true });
  });
})();
