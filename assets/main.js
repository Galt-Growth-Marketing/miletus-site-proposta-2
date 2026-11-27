// Miletus - interacoes do site estatico
// Seguranca: se qualquer coisa falhar, mostra todo o conteudo (nada fica escondido)
const revealAll = () => {
  document.documentElement.classList.remove('js');
  document.querySelectorAll('.rv,.rv-img,.words,.zoom-in,.nc').forEach(e => e.classList.add('in'));
};
window.addEventListener('error', revealAll);
document.documentElement.classList.add('js');

// menu do celular
const hdr = document.querySelector('.top');
const burger = document.querySelector('.burger');
if (hdr && burger) {
  const setMenu = open => {
    hdr.classList.toggle('open', open);
    burger.setAttribute('aria-expanded', String(open));
    burger.setAttribute('aria-label', open ? 'Fechar menu' : 'Abrir menu');
  };
  burger.addEventListener('click', () => setMenu(!hdr.classList.contains('open')));
  hdr.querySelectorAll('.mmenu a').forEach(link => link.addEventListener('click', () => setMenu(false)));
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && hdr.classList.contains('open')) {
      setMenu(false);
      burger.focus();
    }
  });
  matchMedia('(max-width: 900px)').addEventListener('change', () => setMenu(false));
}

// A coluna ocupa os primeiros 426 px da marca de 2285 px.
// O recorte termina no espaco entre o simbolo e o lettering.
const headerBrand = hdr?.querySelector('.logo');
if (headerBrand) {
  const artwork = headerBrand.querySelector('img');
  let assembly;
  const assemble = () => {
    if (!artwork.animate || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    assembly?.cancel();
    const contour = level =>
      'polygon(0 ' + level + '%,22% ' + level + '%,22% 0,100% 0,100% 100%,0 100%)';
    assembly = artwork.animate([
      {clipPath: contour(100)}, {clipPath: contour(0)}
    ], {duration: 1600, easing: 'cubic-bezier(.35,0,.2,1)'});
  };
  assemble();
  headerBrand.addEventListener('pointerenter', event => {
    if (event.pointerType === 'mouse') assemble();
  });
  headerBrand.addEventListener('focus', () => { if (headerBrand.matches(':focus-visible')) assemble(); });
}

// abas de servicos (a ancora da URL abre a aba certa)
const tabs = [...document.querySelectorAll('.tabs a')];
if (tabs.length) {
  const panels = [...document.querySelectorAll('.panel')];
  const show = (slug, scroll) => {
    if (!panels.some(p => p.id === slug)) slug = panels[0].id;
    tabs.forEach(t => t.classList.toggle('on', t.dataset.tab === slug));
    panels.forEach(p => p.classList.toggle('on', p.id === slug));
    if (scroll) document.querySelector('.tabs').scrollIntoView({ behavior: 'smooth', block: 'start' });
  };
  tabs.forEach(t => t.addEventListener('click', e => {
    e.preventDefault();
    history.replaceState(null, '', '#' + t.dataset.tab);
    show(t.dataset.tab, false);
  }));
  const initial = location.hash.slice(1);
  show(initial, !!initial);
  addEventListener('hashchange', () => show(location.hash.slice(1), true));
}

// galeria das fichas
document.querySelectorAll('.gallery').forEach(g => {
  const imgs = [...g.querySelectorAll('.gview img')];
  const count = g.querySelector('.gcount');
  let i = 0;
  const go = d => {
    imgs[i].classList.remove('on');
    i = (i + d + imgs.length) % imgs.length;
    imgs[i].classList.add('on');
    if (count) count.textContent = String(i + 1).padStart(2, '0') + ' / ' + String(imgs.length).padStart(2, '0');
  };
  g.querySelector('.gprev')?.addEventListener('click', () => go(-1));
  g.querySelector('.gnext')?.addEventListener('click', () => go(1));
});

// formulario: enquanto nao houver integracao, abre o e-mail ja preenchido
document.querySelectorAll('.cform').forEach(f => f.addEventListener('submit', e => {
  e.preventDefault();
  const data = new FormData(f);
  const body = [...data.entries()].filter(([, v]) => v).map(([k, v]) => `${k}: ${v}`).join('\n');
  location.href = `mailto:${f.dataset.mail}?subject=${encodeURIComponent('Contato pelo site')}&body=${encodeURIComponent(body)}`;
}));

// hero com 3 banners: troca a cada 10 s
const hero = document.querySelector('.hero2');
if (hero) {
  const slides = [...hero.querySelectorAll('.slide')];
  const dots = [...hero.querySelectorAll('.bar-i')];
  let i = 0, timer;
  const go = n => {
    slides[i].classList.remove('on'); dots[i]?.classList.remove('on');
    i = (n + slides.length) % slides.length;
    void slides[i].offsetWidth;
    slides[i].classList.add('on'); dots[i]?.classList.add('on');
    schedule();
  };
  const schedule = () => { clearTimeout(timer); timer = setTimeout(() => go(i + 1), 10000); };
  dots.forEach(d => d.addEventListener('click', () => go(+d.dataset.i)));
  // arrastar para o lado no celular
  let x0 = null;
  hero.addEventListener('touchstart', e => { x0 = e.touches[0].clientX; }, { passive: true });
  hero.addEventListener('touchend', e => {
    if (x0 === null) return;
    const dx = e.changedTouches[0].clientX - x0;
    if (Math.abs(dx) > 50) go(i + (dx < 0 ? 1 : -1));
    x0 = null;
  });
  if (!matchMedia('(prefers-reduced-motion: reduce)').matches) schedule();
}

// titulos de secao: palavras sobem uma a uma
document.querySelectorAll('.shead h2, .stext h2, .cbody h2, .ptxt h2, .finfo h1, .phero h1').forEach(h => {
  let n = 0;
  const wrap = (txt, bold) => txt.split(/(\s+)/).map(w => /^\s+$/.test(w) || !w ? w :
    `<span class="w"><span style="transition-delay:${(n++) * 70}ms">${bold ? '<b>' + w + '</b>' : w}</span></span>`).join('');
  h.innerHTML = [...h.childNodes].map(c => c.nodeType === 3 ? wrap(c.textContent, false) : wrap(c.textContent, true)).join('');
  h.classList.add('words');
});

// animacoes ao rolar: secoes e cards entram em sequencia
const calm = matchMedia('(prefers-reduced-motion: reduce)').matches;
const groups = ['.shead', '.ncards', '.tiles5', '.stiles', '.ogrid', '.stext', '.cbody', '.cer', '.finfo', '.tabs'];
const items = [];
groups.forEach(sel => document.querySelectorAll(sel).forEach(g => {
  const kids = g.matches('.ncards,.tiles5,.stiles,.ogrid,.cer') ? [...g.children] : [...g.children];
  kids.forEach((k, n) => { k.classList.add('rv'); k.style.transitionDelay = Math.min(n, 6) * 90 + 'ms'; items.push(k); });
}));
document.querySelectorAll('.sphoto, .cphoto, .gview, .pimg').forEach(el => { el.classList.add('rv-img'); items.push(el); });
document.querySelectorAll('.loop').forEach(el => { el.classList.add('rv'); items.push(el); });
document.querySelectorAll('.logos').forEach(g => [...g.children].forEach((k, n) => { k.classList.add('rv'); k.style.transitionDelay = (n % 6) * 70 + 'ms'; items.push(k); }));
document.querySelectorAll('.words').forEach(h => items.push(h));
document.querySelectorAll('.tile, .stile, .ophoto').forEach(el => { el.classList.add('zoom-in'); items.push(el); });

// contador dos numeros (so na faixa da home)
const countUp = el => {
  const node = el.firstChild;
  if (!node || node.nodeType !== 3) return;
  const raw = node.textContent.trim();
  const target = parseInt(raw.replace(/\D/g, ''), 10);
  if (!target || calm) return;
  const plus = raw.startsWith('+') ? '+' : '';
  // contagem curta e suave: so os ultimos 8% do valor
  const from = 0, t0 = performance.now(), dur = 1500;
  const step = t => {
    const p = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - p, 4);
    node.textContent = plus + Math.round(from + (target - from) * e).toLocaleString('pt-BR');
    if (p < 1) requestAnimationFrame(step);
  };
  node.textContent = plus + from.toLocaleString('pt-BR');
  requestAnimationFrame(step);
};

if ('IntersectionObserver' in window && !calm) {
  const io = new IntersectionObserver(entries => entries.forEach(e => {
    if (!e.isIntersecting) return;
    e.target.classList.add('in');
    if (e.target.closest('#numeros') && e.target.classList.contains('nc')) countUp(e.target.querySelector('b'));
    io.unobserve(e.target);
  }), { threshold: .15, rootMargin: '0px 0px -40px 0px' });
  items.forEach(el => io.observe(el));
} else items.forEach(el => el.classList.add('in'));

// leve movimento das fotos grandes ao rolar
const par = [...document.querySelectorAll('.sphoto img, .cphoto img')];
if (par.length && !calm) {
  let ticking = false;
  const move = () => {
    par.forEach(img => {
      const r = img.parentElement.getBoundingClientRect();
      const off = Math.max(-28, Math.min(28, (r.top + r.height / 2 - innerHeight / 2) * -0.06));
      img.style.transform = `scale(1.12) translateY(${off.toFixed(1)}px)`;
    });
    ticking = false;
  };
  addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(move); } }, { passive: true });
  move();
}

// cabecalho compacta ao rolar
const hdrEl = document.querySelector('.top');
const onScrollHdr = () => hdrEl && hdrEl.classList.toggle('compact', scrollY > 40);
addEventListener('scroll', onScrollHdr, { passive: true }); onScrollHdr();
// paginas internas: titulo do topo aparece logo
document.querySelectorAll('.phero .words, .finfo .words').forEach(h => setTimeout(() => h.classList.add('in'), 150));

// fallback final: se o observador de rolagem nao disparar em 6 s, revela o que ja passou na tela
setTimeout(() => {
  document.querySelectorAll('.rv,.rv-img,.words,.zoom-in').forEach(e => {
    if (e.getBoundingClientRect().top < innerHeight) e.classList.add('in');
  });
}, 6000);

// proposta 2: anima o grafismo da coluna quando a secao Empresa aparece
const emp = document.getElementById('empresa');
if (emp && 'IntersectionObserver' in window) {
  const io2 = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { emp.classList.add('seen'); io2.disconnect(); } }), { threshold: .25 });
  io2.observe(emp);
} else if (emp) emp.classList.add('seen');

document.querySelectorAll('.nc').forEach((card) => {
  card.addEventListener('pointermove', (event) => {
    const rect = card.getBoundingClientRect();
    card.style.setProperty('--mx', `${event.clientX - rect.left}px`);
    card.style.setProperty('--my', `${event.clientY - rect.top}px`);
  });
  card.addEventListener('pointerleave', () => {
    card.style.removeProperty('--mx');
    card.style.removeProperty('--my');
  });
});
// A textura acompanha o ponteiro dentro do painel de setores.
const sectorPanel = document.querySelector('.sector-copy');
if (sectorPanel && matchMedia('(hover: hover) and (pointer: fine)').matches) {
  const section = sectorPanel.closest('.sectors');
  sectorPanel.addEventListener('pointermove', event => {
    const bounds = sectorPanel.getBoundingClientRect();
    const x = (event.clientX - bounds.left) / bounds.width - .5;
    const y = (event.clientY - bounds.top) / bounds.height - .5;
    section.style.setProperty('--map-x', (x * 24).toFixed(1) + 'px');
    section.style.setProperty('--map-y', (y * 24).toFixed(1) + 'px');
  });
  sectorPanel.addEventListener('pointerleave', () => {
    section.style.removeProperty('--map-x');
    section.style.removeProperty('--map-y');
  });
}

// Navegação dos carrosséis de cards no celular e tablet.
document.querySelectorAll('.tiles5, .ogrid').forEach((track, groupIndex) => {
  const cards = Array.from(track.children);
  if (cards.length < 2) return;

  const controls = document.createElement('div');
  controls.className = 'card-pagination';
  controls.setAttribute('role', 'group');
  controls.setAttribute('aria-label', track.matches('.tiles5') ? 'Escolher serviço' : 'Escolher obra');
  track.id ||= 'card-track-' + groupIndex;
  track.after(controls);

  function positions() {
    const left = track.getBoundingClientRect().left;
    const inset = parseFloat(getComputedStyle(track).scrollPaddingLeft) || 0;
    const limit = track.scrollWidth - track.clientWidth;
    return cards.map(card => Math.max(0, Math.min(limit,
      card.getBoundingClientRect().left - left + track.scrollLeft - inset)));
  }

  const buttons = cards.map((card, i) => {
    const button = document.createElement('button');
    button.type = 'button';
    button.setAttribute('aria-controls', track.id);
    button.setAttribute('aria-label', (i + 1) + ' de ' + cards.length + ': ' + card.querySelector('h3').textContent);
    button.addEventListener('click', () => {
      track.scrollTo({ left: positions()[i],
        behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth' });
    });
    controls.append(button);
    return button;
  });

  function update() {
    const scrollable = track.scrollWidth > track.clientWidth + 1;
    controls.hidden = !scrollable;
    if (!scrollable) {
      cards.forEach(card => card.classList.remove('is-current'));
      return;
    }
    const stops = positions();
    const current = stops.reduce((best, stop, i) =>
      Math.abs(stop - track.scrollLeft) < Math.abs(stops[best] - track.scrollLeft) ? i : best, 0);
    buttons.forEach((button, i) => {
      cards[i].classList.toggle('is-current', i === current);
      if (i === current) button.setAttribute('aria-current', 'true');
      else button.removeAttribute('aria-current');
    });
  }

  track.addEventListener('scroll', update, { passive: true });
  if ('ResizeObserver' in window) new ResizeObserver(update).observe(track);
  else window.addEventListener('resize', update);
  update();
});

// Cada desenho toca uma vez ao entrar na tela e pode ser repetido.
const sectorCards = document.querySelectorAll('.sector-chip');
const reducedSectorMotion = matchMedia('(prefers-reduced-motion: reduce)');
function drawSector(card) {
  if (reducedSectorMotion.matches) return;
  card.classList.remove('is-drawing');
  void card.offsetWidth;
  card.classList.add('is-drawing');
}
const sectorEntrance = 'IntersectionObserver' in window
  ? new IntersectionObserver(entries => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        drawSector(entry.target);
        sectorEntrance.unobserve(entry.target);
      }
    }, { threshold: .6 })
  : null;

sectorCards.forEach(card => {
  sectorEntrance?.observe(card);
  card.addEventListener('pointerenter', event => {
    if (event.pointerType !== 'touch') drawSector(card);
  });
  card.addEventListener('pointerup', event => {
    if (event.pointerType === 'touch') drawSector(card);
  });
});
