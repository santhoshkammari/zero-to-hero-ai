/* Zero to Hero AI — Site JS */
(function () {
  'use strict';

  /* ── Determine base path to site root ── */
  const path = window.location.pathname;
  let basePath = './';
  if (path.includes('/chapters/ch')) {
    basePath = '../../';
  }

  /* ── Make sidebar links navigable ── */
  document.querySelectorAll('.nav-section').forEach(el => {
    const href = el.getAttribute('data-href');
    if (href) el.setAttribute('href', basePath + 'chapters/' + href);
  });
  document.querySelectorAll('.nav-chapter').forEach(el => {
    const href = el.getAttribute('data-href');
    if (href) el.setAttribute('data-index', basePath + 'chapters/' + href + '/index.html');
  });

  /* ── Theme toggle ── */
  const saved = localStorage.getItem('theme');
  if (saved) document.documentElement.setAttribute('data-theme', saved);

  document.addEventListener('click', e => {
    if (e.target.closest('.theme-toggle')) {
      const current = document.documentElement.getAttribute('data-theme');
      const next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('theme', next);
      const btn = e.target.closest('.theme-toggle');
      btn.textContent = next === 'dark' ? '☀️' : '🌙';
    }
  });

  /* ── Sidebar chapter expand/collapse ── */
  document.addEventListener('click', e => {
    const ch = e.target.closest('.nav-chapter');
    if (!ch) return;
    const sections = ch.nextElementSibling;
    if (sections && sections.classList.contains('nav-sections')) {
      const isExpanded = ch.classList.contains('expanded');
      if (isExpanded) {
        // Collapse — navigate to chapter index
        const indexUrl = ch.getAttribute('data-index');
        if (indexUrl) window.location.href = indexUrl;
      } else {
        // Expand sections
        ch.classList.add('expanded');
        sections.classList.add('open');
      }
    }
  });

  /* ── Mobile sidebar toggle ── */
  document.addEventListener('click', e => {
    if (e.target.closest('.sidebar-toggle')) {
      document.querySelector('.sidebar').classList.toggle('open');
    }
    // Close sidebar when clicking main content on mobile
    if (e.target.closest('.main') && window.innerWidth <= 900) {
      document.querySelector('.sidebar').classList.remove('open');
    }
  });

  /* ── Reading progress bar ── */
  const fill = document.querySelector('.progress-bar .fill');
  if (fill) {
    window.addEventListener('scroll', () => {
      const h = document.documentElement;
      const pct = (h.scrollTop / (h.scrollHeight - h.clientHeight)) * 100;
      fill.style.width = Math.min(100, pct) + '%';
    }, { passive: true });
  }

  /* ── Highlight active sidebar link ── */
  function setActive() {
    const loc = window.location.pathname;
    document.querySelectorAll('.nav-section, .nav-chapter').forEach(el => {
      el.classList.remove('active');
    });
    // Match section links
    document.querySelectorAll('.nav-section').forEach(el => {
      const dh = el.getAttribute('data-href');
      if (dh && loc.includes(dh)) {
        el.classList.add('active');
        const parent = el.closest('.nav-sections');
        if (parent) {
          parent.classList.add('open');
          const ch = parent.previousElementSibling;
          if (ch) ch.classList.add('expanded', 'active');
        }
      }
    });
    // Match chapter index pages
    document.querySelectorAll('.nav-chapter').forEach(el => {
      const dh = el.getAttribute('data-href');
      if (dh && loc.includes(dh + '/')) {
        el.classList.add('active', 'expanded');
        const sections = el.nextElementSibling;
        if (sections) sections.classList.add('open');
      }
    });
  }
  setActive();
})();
