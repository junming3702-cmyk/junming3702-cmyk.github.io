// Progressive enhancement: all navigation and content work without JavaScript.
const links = [...document.querySelectorAll('nav a[href^="#"]')];
if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver(entries => {
    for (const entry of entries) {
      if (entry.isIntersecting) {
        for (const link of links) {
          if (link.hash === `#${entry.target.id}`) link.setAttribute('aria-current', 'location');
          else link.removeAttribute('aria-current');
        }
      }
    }
  }, { rootMargin: '-20% 0px -60% 0px' });
  document.querySelectorAll('#research, #project, #approach, #opportunities').forEach(section => observer.observe(section));
}

// Progressive enhancement: every example is readable if JavaScript is disabled.
const tablist = document.querySelector('.example-tabs');
if (tablist) {
  const tabs = [...tablist.querySelectorAll('[role="tab"]')];
  const activate = tab => {
    for (const item of tabs) {
      const selected = item === tab;
      item.setAttribute('aria-selected', String(selected));
      item.tabIndex = selected ? 0 : -1;
      const panel = document.getElementById(item.getAttribute('aria-controls'));
      panel.hidden = !selected;
      panel.setAttribute('role', 'tabpanel');
      panel.setAttribute('aria-labelledby', item.id);
      panel.tabIndex = 0;
    }
  };
  tablist.hidden = false;
  activate(tabs[0]);
  for (const tab of tabs) {
    tab.addEventListener('click', () => activate(tab));
    tab.addEventListener('keydown', event => {
      const current = tabs.indexOf(tab);
      const positions = { ArrowRight: (current + 1) % tabs.length, ArrowLeft: (current + tabs.length - 1) % tabs.length, Home: 0, End: tabs.length - 1 };
      if (Object.prototype.hasOwnProperty.call(positions, event.key)) {
        event.preventDefault();
        const target = tabs[positions[event.key]];
        activate(target);
        target.focus();
      }
    });
  }
}
