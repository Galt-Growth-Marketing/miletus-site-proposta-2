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
if (burger) burger.addEventListener('click', () => {
  const open = hdr.classList.toggle('open');
  burger.setAttribute('aria-expanded', open);
});
document.querySelectorAll('.mmenu a').forEach(a => a.addEventListener('click', () => hdr.classList.remove('open')));

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
  const from = Math.round(target * 0.92), t0 = performance.now(), dur = 1100;
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
