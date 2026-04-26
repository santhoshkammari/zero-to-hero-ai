/* Zero to Hero AI — Site JS */
(function () {
  'use strict';

  /* ── Determine base path to site root ── */
  const path = window.location.pathname;
  let basePath = './';
  if (path.includes('/chapters/ch')) {
    basePath = '../../';
  }

  /* ── Theme toggle (default: dark, persists across pages) ── */
  const theme = localStorage.getItem('theme') || 'dark';
  document.documentElement.setAttribute('data-theme', theme);
  if (!localStorage.getItem('theme')) localStorage.setItem('theme', 'dark');

  // Sync all toggle buttons on page load
  document.querySelectorAll('.theme-toggle').forEach(btn => {
    btn.textContent = theme === 'dark' ? '☀️' : '🌙';
  });

  document.addEventListener('click', e => {
    if (e.target.closest('.theme-toggle')) {
      const current = document.documentElement.getAttribute('data-theme');
      const next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('theme', next);
      document.querySelectorAll('.theme-toggle').forEach(btn => {
        btn.textContent = next === 'dark' ? '☀️' : '🌙';
      });
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
    document.querySelectorAll('.nav-chapter').forEach(el => {
      el.classList.remove('active');
    });
    document.querySelectorAll('.nav-chapter').forEach(el => {
      const dh = el.getAttribute('data-href');
      if (dh && loc.includes('/' + dh + '/')) {
        el.classList.add('active');
      }
    });
  }
  setActive();
})();
