(function () {
  'use strict';

  var TIER_COLORS = {
    '01-Foundation':    '#16a34a',
    '02-Ascent':        '#2563eb',
    '03-Expedition':    '#d97706',
    '04-Summit':        '#ea580c',
    '05-Battleground':  '#dc2626'
  };

  var CONCEPT_BUCKETS = [
    '02-Core-Concepts',
    '03-Caching',
    '04-Storage-and-Databases',
    '05-Messaging-and-Event-Driven',
    '06-Distributed-Systems'
  ];

  /* ── helpers ───────────────────────────────────────────── */

  function getTierColor() {
    var path = window.location.pathname;
    for (var tier in TIER_COLORS) {
      if (path.indexOf(tier) !== -1) return TIER_COLORS[tier];
    }
    return '#059669';
  }

  function getSectionText(labelEl) {
    var ellipsis = labelEl.querySelector('.md-ellipsis');
    if (ellipsis) return ellipsis.textContent.trim();
    var clone = labelEl.cloneNode(true);
    var icon = clone.querySelector('.md-nav__icon');
    if (icon) icon.remove();
    return clone.textContent.trim();
  }

  function getSectionHref(section) {
    var direct = section.querySelector(':scope > a.md-nav__link');
    if (direct) return direct.getAttribute('href');
    var nested = section.querySelector('.md-nav a.md-nav__link');
    return nested ? nested.getAttribute('href') : null;
  }

  /* Find the deepest active nested nav that has ≥2 nested children */
  function findContextNav(sidebar) {
    var activeItems = Array.from(
      sidebar.querySelectorAll('.md-nav__item--nested.md-nav__item--active')
    );
    for (var i = activeItems.length - 1; i >= 0; i--) {
      var cn = activeItems[i].querySelector(':scope > .md-nav');
      if (!cn) continue;
      var cl = cn.querySelector(':scope > .md-nav__list');
      if (!cl) continue;
      if (cl.querySelectorAll(':scope > .md-nav__item--nested').length >= 2) {
        return cn;
      }
    }
    return null;
  }

  function buildTabs(navEl, color) {
    var navList = navEl.querySelector(':scope > .md-nav__list');
    if (!navList) return;

    var sections = Array.from(
      navList.querySelectorAll(':scope > .md-nav__item--nested')
    );
    if (sections.length === 0) return;

    var tabsList = document.querySelector('.md-tabs__list');
    if (!tabsList) return;

    var tabHtml = sections.map(function (section) {
      var labelEl = section.querySelector(':scope > label.md-nav__link') ||
                    section.querySelector(':scope > a.md-nav__link');
      if (!labelEl) return '';

      var text = getSectionText(labelEl);
      if (!text) return '';

      var href = getSectionHref(section);
      if (!href) return '';

      var isActive = section.classList.contains('md-nav__item--active');
      var colorStyle = isActive
        ? ' style="color:' + color + '; border-bottom: 2px solid ' + color + '; font-weight: 650; opacity: 1;"'
        : ' style="color: var(--md-default-fg-color--lighter);"';

      return '<li class="md-tabs__item">' +
        '<a href="' + href + '" class="md-tabs__link' + (isActive ? ' md-tabs__link--active' : '') + '"' +
        colorStyle + '>' + text + '</a></li>';
    }).join('');

    if (tabHtml) {
      tabsList.innerHTML = tabHtml;
    }
  }

  /* ── Deep-Dives handler (case studies) ─────────────────── */

  function replaceTabsWithDeepDives() {
    var path = window.location.pathname;
    if (path.indexOf('Deep-Dives') === -1) return;

    var sidebar = document.querySelector('.md-sidebar--primary');
    if (!sidebar) return;

    var deepDivesNav = sidebar.querySelector('.md-nav[aria-label="Deep Dives"]')
                     || findContextNav(sidebar);
    if (!deepDivesNav) return;

    buildTabs(deepDivesNav, getTierColor());
  }

  /* ── Concept-bucket handler ─────────────────────────────── */

  function replaceTabsWithConceptBucket() {
    var path = window.location.pathname;

    // Must be inside a bucket sub-path, not the bucket index itself
    var activeBucket = null;
    for (var i = 0; i < CONCEPT_BUCKETS.length; i++) {
      var marker = '/' + CONCEPT_BUCKETS[i] + '/';
      var idx = path.indexOf(marker);
      if (idx !== -1 && path.slice(idx + marker.length).length > 0) {
        activeBucket = CONCEPT_BUCKETS[i];
        break;
      }
    }
    if (!activeBucket) return;

    var sidebar = document.querySelector('.md-sidebar--primary');
    if (!sidebar) return;

    var sectionNav = findContextNav(sidebar);
    if (!sectionNav) return;

    buildTabs(sectionNav, '#059669'); // brand green for all concept buckets
  }

  /* ── init ───────────────────────────────────────────────── */

  function init() {
    replaceTabsWithDeepDives();
    replaceTabsWithConceptBucket();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
