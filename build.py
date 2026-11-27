#!/usr/bin/env python3
"""Gera o site estático da Miletus (index, servicos, portfolio e fichas).
Toda a copy fica neste arquivo. Para alterar texto: edite aqui e rode `python3 build.py`.
"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
IMG = "assets/img/"
LOGOS = sorted(f for f in os.listdir(os.path.join(HERE, "assets/logos")) if f.endswith(".png"))
WHATS = "https://wa.me/5527992817520"
TEL, MAIL = "(27) 99281-7520", "vinicius@miletus.eng.br"

# ----------------------------------------------------------------- conteúdo
NUMS = [("+6.700", "m²", "de pontes projetadas"), ("+17.000", "m²", "de contenções projetadas"),
        ("+7.800", "m²", "de edificações projetadas"), ("+40", "", "barragens atendidas"),
        ("+17", "hm³", "de água reservada em barragens")]

SERVICOS = [
    dict(slug="estudos-e-projetos", nome="Estudos e projetos", frase="Projeto completo, pronto para licitar a obra.",
         desc="Da viabilidade ao executivo, com fundação, contenção e drenagem definidas a partir das condições reais do terreno.",
         img="svc-passarela-1920.jpg",
         entregas=["Estudos de viabilidade e topografia com drone", "Investigações geotécnicas", "Estudos hidrológicos e análises de estabilidade",
                   "Projetos de pontes, viadutos, contenções, rodovias e barragens", "Projetos básico e executivo em 3D e BIM",
                   "Quantitativos, orçamento e cronograma", "Estudos fundiários e licenciamento ambiental"]),
    dict(slug="engenharia-do-proprietario", nome="Engenharia do proprietário", frase="Acompanhamento técnico independente da obra.",
         desc="Supervisão em campo de materiais, métodos e cronograma, com solução de engenharia quando a obra encontra uma condição não prevista no projeto.",
         img="06_execucao-perfis-metalicos-em-balanco.jpg",
         entregas=["Validação e certificação técnica de projetos", "Supervisão da construção e do cronograma", "Controle tecnológico e ensaios",
                   "Readequação de projeto em obra", "Relatórios de inspeção", "Laudo de Barragem Construída para a Licença de Operação"]),
    dict(slug="consultoria-tecnica-civil", nome="Consultoria técnica civil", frase="Laudo conclusivo sobre estruturas existentes.",
         desc="Avaliação de pontes, edificações e estruturas em operação com inspeção, ensaios e modelagem estrutural completa.",
         img="svc-inspecao-1920.jpg",
         entregas=["Inspeções e perícias técnicas", "Ensaios não destrutivos", "Avaliação e modelagem estrutural", "Projeto de reforço",
                   "Análise de reinvestimento", "Projetos estruturais de edificações"]),
    dict(slug="apoio-a-construtoras", nome="Apoio a construtoras e consultorias", frase="Escopo técnico completo no seu contrato.",
         desc="Geotecnia, barragens, pontes e contenções assumidas por completo no contrato, da proposta à supervisão em campo.",
         img="06_execucao-armacao-contrafortes.jpg",
         entregas=["Projetos para propostas e licitações, inclusive RDC e contratações integradas",
                   "Projetos executivos de contenções e obras de arte especiais", "Supervisão e inspeções em campo", "Equipe técnica local"]),
    dict(slug="seguranca-de-barragens", nome="Segurança de barragens", frase="Barragem com a documentação de segurança em dia.",
         desc="Inspeções, planos de segurança e de emergência e análise da instrumentação, com a documentação da fiscalização sempre atualizada.",
         img="svc-dalmacio-1920.jpg",
         entregas=["Plano de Segurança de Barragens (PSB) e revisão periódica", "Plano de Ação Emergencial (PAE e PAEBM)", "Estudos de dam break",
                   "Inspeções regulares e especiais", "Análise de instrumentação e de comportamento"]),
]

SETORES = [("Infraestrutura", "setor-infraestrutura.jpg"), ("Rodoviário", "setor-rodoviario.jpg"),
           ("Construtoras", "setor-construtoras.jpg"), ("Consultorias", "setor-consultorias.jpg"),
           ("Energia", "setor-energia.jpg"), ("Mineração", "mineracao-mina-ceu-aberto.jpg")]

# Imagens de banco (Wikimedia Commons). As licenças CC BY / CC BY-SA exigem crédito: ver creditos.html.
CREDITOS = [
    ("Setor Infraestrutura", "Zhijiang Bridge", "Charlie fong", "CC BY-SA 4.0", "https://commons.wikimedia.org/wiki/File:Zhijiang_Bridge.jpg"),
    ("Setor Rodoviário", "Cruzamento da Rodovia dos Bandeirantes na SP 101", "Ana Perugini", "CC BY 2.0", "https://commons.wikimedia.org/wiki/File:Cruzamento_da_Rodovia_dos_Bandeirantes_na_SP_101_(8021079016).jpg"),
    ("Setor Construtoras", "Tower crane rising at hollywoodHUB construction site", "PortlandAppraisalBlog", "CC BY-SA 4.0", "https://commons.wikimedia.org/wiki/File:Tower_crane_rising_at_hollywoodHUB_construction_site,_Portland,_Oregon.jpg"),
    ("Setor Consultorias", "Mayhew levee repair inspection", "U.S. Army Corps of Engineers", "Domínio público", "https://commons.wikimedia.org/wiki/File:Mayhew_levee_repair_inspection_(16142964469).jpg"),
    ("Setor Energia", "Usina Hidrelétrica de Itá", "LeonardoG", "Domínio público", "https://commons.wikimedia.org/wiki/File:Usina_It%C3%A1.jpg"),
]

# Galerias: conferir com o designer se as fotos estão na obra certa.
OBRAS = [
    dict(slug="ponte-santa-maria-do-doce", tipo="Ampliação de ponte", nome="Ponte do Rio Santa Maria do Doce",
         destaque="86 m de extensão, sem demolição", local="São Roque do Canaã (ES)",
         contratante="AMF Engenharia, para a Prefeitura de São Roque do Canaã · 2024–2025",
         nums=[("86", "m", "de extensão"), ("978", "m²", "de tabuleiro"), ("11,30", "m", "de largura")],
         contexto="Ponte em arco dos anos 1940 que precisava ser alargada.",
         entrega="Inspeção e ensaios da estrutura existente e projeto de ampliação em estrutura mista de aço e concreto.",
         resultado="Ponte ampliada sem demolição.",
         galeria=["g-ponte-01-1920.jpg", "p09-1920.jpg", "04_ponte-existente-arcos-vista-lateral.jpg", "06_execucao-perfis-metalicos-em-balanco.jpg"]),
    dict(slug="pontes-presidente-kennedy", tipo="Projeto de pontes", nome="Pontes de Presidente Kennedy",
         destaque="3 pontes rodoviárias em concreto protendido", local="Presidente Kennedy (ES)",
         contratante="Lugare Engenharia, para a Prefeitura de Presidente Kennedy · 2024",
         nums=[("3", "", "pontes projetadas"), ("977,5", "m²", "de tabuleiro"), ("20", "m", "de maior vão")],
         contexto="Três travessias rodoviárias, cada uma com terreno e vão próprios.",
         entrega="Projeto executivo das três pontes em concreto armado sobre vigas protendidas, com fundações e detalhamento completo.",
         resultado="Três pontes detalhadas para execução, somando 76,6 m de extensão.",
         galeria=["o-kennedy-pesqueiros.jpg", "o-kennedy-pedra-branca.jpg", "o-kennedy-santa-lucia.jpg"]),
    dict(slug="entorno-sao-dalmacio", tipo="Urbanização e obras de arte", nome="Entorno da Barragem São Dalmácio",
         destaque="126,5 m de passarela estaiada", local="São Roque do Canaã (ES)",
         contratante="Prefeitura de São Roque do Canaã · 2024–2025",
         nums=[("126,5", "m", "de passarela estaiada"), ("7,5", "km", "de vias"), ("8.878", "m²", "de contenções")],
         contexto="Urbanizar o entorno do reservatório da nova barragem.",
         entrega="Passarela estaiada, ponte rodoviária, contenções e vias, num único projeto.",
         resultado="Todo o entorno resolvido num só contrato.",
         galeria=["03_vista-geral-aerea-reservatorio.jpg", "svc-passarela-1920.jpg", "01_passarela-estaiada-vista-lateral.jpg"]),
    dict(slug="hospital-jayme-dos-santos-neves", tipo="Avaliação estrutural", nome="Hospital Estadual Jayme dos Santos Neves",
         destaque="31.833 m² avaliados", local="Serra (ES)", contratante="AEBES, para a SESA-ES · 2022–2023",
         nums=[("31.833", "m²", "avaliados"), ("7", "", "blocos modelados"), ("144", "", "ensaios")],
         contexto="Avaliar a segurança estrutural de um hospital em funcionamento.",
         entrega="Inspeção, ensaios, modelagem dos sete blocos e proposta de reforço.",
         resultado="Laudo conclusivo, sem interromper a operação do hospital.",
         galeria=["g-hospital-01-1920.jpg", "04_modelo-tqs-bloco-f.jpg"]),
    dict(slug="barragem-sao-dalmacio", tipo="Projeto e supervisão", nome="Barragem São Dalmácio",
         destaque="309.902 m³ de reservatório", local="São Roque do Canaã (ES)", contratante="Prefeitura de São Roque do Canaã · 2022–2026",
         nums=[("12", "m", "de altura"), ("309.902", "m³", "de reservatório"), ("52", "dias", "de projeto, num prazo de 90")],
         contexto="Viabilizar a barragem e acompanhar a construção até a Licença de Operação.",
         entrega="Estudo de viabilidade, projeto executivo e supervisão da obra.",
         resultado="Projeto entregue antes do prazo contratual e barragem concluída.",
         galeria=["g-dalmacio-01-1920.jpg", "svc-dalmacio-1920.jpg", "p06-1920.jpg"]),
    dict(slug="barragem-piraque-acu", tipo="Consultoria em obra", nome="Barragem do Rio Piraquê-Açu",
         destaque="Vazão de projeto de 351 para 580 m³/s", local="Aracruz (ES)", contratante="Concremat, para a SEAG-ES · 2026",
         nums=[("351 → 580", "m³/s", "de vazão de projeto"), ("4", "", "módulos de vertedouro"), ("2026", "", "obra concluída")],
         contexto="Uma cheia durante a obra indicou vazão de projeto subestimada.",
         entrega="Novo estudo hidrológico e readequação do vertedouro em campo.",
         resultado="Vertedouro ampliado sem interromper a execução.",
         galeria=["g-piraque-01-1920.jpg", "hero-piraque-1920.jpg", "svc-piraque-1920.jpg", "03_drone-obra-vertedouro-labirinto-2026-04.jpg"]),
    dict(slug="barragens-rurais-marilandia", tipo="Supervisão e segurança de barragens", nome="Supervisão de 15 Barragens Rurais",
         destaque="15 barragens de terra acompanhadas", local="Marilândia (ES)",
         contratante="AA Administração de Bens e Negócios · 2025–2026",
         nums=[("15", "", "barragens de terra"), ("13", "", "projetos de adequação"), ("16", "", "relatórios de supervisão")],
         contexto="Obras de construção, alteamento e recuperação em 15 barragens rurais ao mesmo tempo.",
         entrega="Supervisão das obras com controle de topografia e compactação, inspeções de segurança, estudos de estabilidade e hidrologia, laudos e projetos de adequação.",
         resultado="Todas as barragens acompanhadas mês a mês, com a segurança documentada.",
         galeria=["o-marilandia-monte-azul-2.jpg", "o-marilandia-obra-raiz-4.jpg", "o-marilandia-lajinha.jpg", "01_drone-barragens-santa-barbara-entre-cafezais.jpg", "05_drone-barragem-monte-azul-1-reservatorio.jpg", "04_drone-obra-barragem-corrego-da-raiz-4-macico.jpg"]),
    dict(slug="barragens-mucurici", tipo="Projeto de barragens", nome="Barragens de Mucurici",
         destaque="3 barragens, 2,86 milhões de m³ de água", local="Mucurici (ES)",
         contratante="Prefeitura de Mucurici · 2022–2023",
         nums=[("3", "", "barragens projetadas"), ("2,86", "hm³", "de água reservada"), ("12", "m", "de altura na maior")],
         contexto="Ampliar a reserva de água do município com três novas barragens.",
         entrega="Projetos básico e executivo de uma barragem em concreto, com ponte sobre o vertedouro, e duas de terra compactada.",
         resultado="Três barragens projetadas, somando 2,86 milhões de m³ de água reservada.",
         galeria=["o-mucurici-render-jusante.jpg", "o-mucurici-render-aereo.jpg"]),
    dict(slug="barragem-bamburral", tipo="Projeto de barragem", nome="Barragem do Córrego Bamburral",
         destaque="7,83 milhões de m³ sobre solo mole", local="São Mateus (ES)",
         contratante="SEAG-ES · 2023–2025",
         nums=[("245", "m", "de barramento"), ("7,83", "hm³", "de reservatório"), ("3.720", "", "colunas de jet grouting")],
         contexto="Uma barragem de terra de 245 m sobre fundação em solo mole.",
         entrega="Projeto básico e executivo completo, com tratamento da fundação por jet grouting, vertedouro e projetos fundiário e ambiental.",
         resultado="Solução segura para construir sobre solo mole, com 184 ha de área de inundação.",
         galeria=["o-bamburral-vale.jpg", "o-bamburral-sondagem.jpg"]),
    dict(slug="barragem-panama", tipo="Projeto de barragem", nome="Barragem do Córrego Panamá",
         destaque="Barragem de concreto com vertedouro em degraus", local="Jerônimo Monteiro (ES)",
         contratante="SEAG-ES · 2023–2025",
         nums=[("14", "m", "de altura"), ("100", "m", "de barramento"), ("7.328", "m³", "de concreto")],
         contexto="Reservação de água para uso agropecuário com barragem de concreto por gravidade.",
         entrega="Projeto básico e executivo completo, com ensaios em rocha, dosagem de concreto, estabilidade e vertedouro com dissipação em escada hidráulica.",
         resultado="Reservatório de 147 mil m³ com vertedouro dimensionado para 31,3 m³/s.",
         galeria=["o-panama-perspectiva.jpg", "o-panama-elevacao.jpg", "o-panama-inundacao.jpg"]),
    dict(slug="barragem-moacir-avidos", tipo="Projeto de barragem", nome="Barragem de Moacir Avidos",
         destaque="Barragem de múltiplo uso", local="Governador Lindenberg (ES)",
         contratante="Prefeitura de Governador Lindenberg · 2023–2024",
         nums=[("12", "m", "de altura"), ("95", "m", "de barramento"), ("31.268", "m³", "de maciço")],
         contexto="Definir o melhor eixo para uma barragem de múltiplo uso.",
         entrega="Estudo de 3 alternativas de barramento e projeto básico e executivo, com sondagens, hidrologia, extravasor e plano de controle ambiental.",
         resultado="Alternativa escolhida com base técnica e projeto completo para execução.",
         galeria=["o-moacir-localizacao.jpg"]),
]
OBRAS_HOME = ["ponte-santa-maria-do-doce", "entorno-sao-dalmacio", "barragem-piraque-acu"]

# ----------------------------------------------------------------- componentes
ARROW = '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M12 5l7 7-7 7"/></svg>'

def head(title, desc, root):
    return f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@300;400;600&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/style.css"><link rel="stylesheet" href="{root}assets/theme-p2.css"></head><body>'''

def header(root, ativo):
    links = [("Home", "index.html"), ("Serviços", "servicos.html"), ("Obras", "portfolio.html"), ("Empresa", "index.html#empresa"), ("Contato", "index.html#contato")]
    li = ''.join(f'<li><a href="{root}{h}"{" class=on" if n == ativo else ""}>{n}</a></li>' for n, h in links)
    lis = [f'<li><a href="{root}{h}"{" class=on" if n == ativo else ""}>{n}</a></li>' for n, h in links]
    return f'''<header class="top"><div class="wrap bar">
<div class="lside"><nav class="nl"><ul>{''.join(lis[:2])}</ul></nav></div>
<a href="{root}index.html" class="logo"><img src="{root}assets/logo-h-dark.png" alt="Miletus Engenharia"></a>
<div class="nr"><nav><ul>{''.join(lis[2:4])}</ul></nav></div>
<button class="burger" aria-label="Abrir menu" aria-expanded="false"><span></span><span></span><span></span></button></div>
<div class="mmenu"><ul>{''.join(lis[:4])}</ul></div></header><main id="conteudo">'''

def footer(root):
    links = [("Home", "index.html"), ("Serviços", "servicos.html"), ("Obras", "portfolio.html"), ("Empresa", "index.html#empresa"), ("Contato", "index.html#contato")]
    li = ''.join(f'<li><a href="{root}{h}">{n}</a></li>' for n, h in links)
    return f'''</main><footer class="foot"><div class="wrap fgrid"><img class="flogo" src="{root}assets/logo-h-dark.png" alt="Miletus Engenharia">
<ul class="fnav">{li}</ul><ul class="fcont"><li><a href="tel:+5527992817520">{TEL}</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li><li><a href="{WHATS}" target="_blank" rel="noopener">WhatsApp</a></li></ul></div>
<div class="wrap fbase">© Miletus Engenharia · <a href="{root}creditos.html">Créditos das imagens</a></div></footer><script src="{root}assets/main.js"></script></body></html>'''

def eyebrow(t): return f'<p class="eyebrow">{t}</p>'
def ncards(ns, cls=""):
    return f'<div class="ncards {cls}">' + ''.join(f'<div class="nc"><b>{v}{f"<i>{u}</i>" if u else ""}</b><span>{t}</span></div>' for v, u, t in ns) + '</div>'
def svc_tile(s, root=""):
    return (f'<a class="tile" href="{root}servicos.html#{s["slug"]}"><img src="{root}{IMG}{s["img"]}" alt="" loading="lazy"><span class="shade"></span>'
            f'<h3>{s["nome"]}</h3><span class="more">Ver o serviço {ARROW}</span></a>')
def obra_card(o, root=""):
    return (f'<a class="ocard" href="{root}obras/{o["slug"]}.html"><div class="ophoto"><img src="{root}{IMG}{o["galeria"][0]}" alt="" loading="lazy"><span class="shade"></span>'
            f'<div class="otxt"><p class="eyebrow light">{o["tipo"]}</p><h3>{o["nome"]}</h3><p class="odest">{o["destaque"]} · {o["local"]}</p>'
            f'<span class="more">Ver a ficha da obra {ARROW}</span></div></div></a>')
# Hero da home: 3 banners com troca automática. <em> = destaque na serifada itálica dourada.
BANNERS = [
    dict(titulo="Segurança e rigor técnico <br>para <em>grandes estruturas.</em>",
         sub="Projeto e supervisão de obras de grande porte.", img="hero-piraque-1920.jpg", tag="Rigor técnico"),
    dict(titulo="Sua obra entregue com <br><em>segurança e precisão.</em>",
         sub="Acompanhamento técnico do estudo de viabilidade à obra concluída.", img="svc-passarela-1920.jpg", tag="Entrega"),
    dict(titulo="Engenharia consultiva <br>para pontes, contenções, <br>barragens e <em>infraestrutura.</em>",
         sub="Projeto, supervisão de obra e avaliação de estruturas.", img="g-ponte-01-1920.jpg", tag="Infraestrutura"),
]

def hero_slider():
    slides = ''
    for i, b in enumerate(BANNERS):
        h = "h1" if i == 0 else "p"
        slides += (f'<div class="slide{" on" if i == 0 else ""}"><img src="{IMG}{b["img"]}" alt="" {"fetchpriority=high" if i == 0 else ""}>'
                   f'<div class="wrap stxt"><{h} class="big"><span>{b["titulo"]}</span></{h}>'
                   f'<p class="lead"><span>{b["sub"]}</span></p><div class="hcta"><a class="btn" href="#contato">Falar com um especialista</a></div></div></div>')
    dots = ''.join(f'<button class="dot{" on" if i == 0 else ""}" data-i="{i}"><i></i><span>{i+1:02d}</span><b>{b["tag"]}</b></button>' for i, b in enumerate(BANNERS))
    return (f'<section class="hero2" aria-roledescription="carrossel"><div class="slides">{slides}</div><span class="layer"></span>'
            f'<div class="bars" role="tablist">' + ''.join(f'<button class="bar-i{" on" if i == 0 else ""}" data-i="{i}" aria-label="Banner {i+1}"><i></i></button>' for i in range(len(BANNERS))) + '</div>'
            f'<a class="mouse" href="#numeros" aria-label="Rolar para baixo"></a></section>')

def page_hero(label, title, sub, img, root=""):
    return (f'<section class="phero"><img src="{root}{IMG}{img}" alt=""><span class="layer"></span><div class="wrap">'
            f'<h1>{title}</h1><p class="lead">{sub}</p></div></section>')

def form():
    opts = ''.join(f'<option>{s["nome"]}</option>' for s in SERVICOS)
    return f'''<form class="cform" data-mail="{MAIL}"><div class="frow"><label>Nome<input name="Nome" required></label><label>E-mail<input name="E-mail" type="email" required></label></div>
<div class="frow"><label>Telefone<input name="Telefone"></label><label>Empresa<input name="Empresa"></label></div>
<label>Serviço<select name="Serviço"><option value="">Selecione</option>{opts}</select></label><label>Mensagem<textarea name="Mensagem" rows="5"></textarea></label>
<button class="btn" type="submit">Enviar mensagem</button></form>'''

# ----------------------------------------------------------------- páginas
def index():
    serv = ''.join(svc_tile(s) for s in SERVICOS)
    set_ = ''.join(f'<div class="stile"><img src="{IMG}{im}" alt="" loading="lazy"><span class="shade"></span><h3>{n}</h3><span class="sline"></span></div>' for n, im in SETORES)
    obras = ''.join(obra_card(next(o for o in OBRAS if o["slug"] == s)) for s in OBRAS_HOME)
    logos = ''.join(f'<span class="lg"><img src="assets/logos/{f}" alt="" loading="lazy"></span>' for f in LOGOS)
    return head("Miletus Engenharia | Pontes, contenções, barragens e infraestrutura",
                "Engenharia consultiva para pontes, contenções, barragens e infraestrutura: projeto, supervisão de obra e segurança de estruturas.", "") + header("", "Home") + f'''
{hero_slider()}

<section class="sec warm tight" id="numeros"><div class="wrap">{ncards(NUMS, "n5")}</div></section>

<section class="sec" id="servicos"><div class="wrap"><div class="shead"><div>{eyebrow("O que entregamos")}<h2>Nossos <b>serviços</b></h2><p class="sub">O que cada serviço entrega para a sua obra.</p></div>
<a class="btn ghost" href="servicos.html">Ver todos os serviços</a></div><div class="tiles5">{serv}</div></div></section>

<section class="sec warm topo"><div class="wrap"><div class="shead"><div>{eyebrow("Onde atuamos")}<h2>Setores <b>atendidos</b></h2></div></div><div class="stiles">{set_}</div></div></section>

<section class="sec" id="obras"><div class="wrap"><div class="shead"><div>{eyebrow("Portfólio")}<h2>Obras de <b>referência</b></h2></div><a class="btn ghost" href="portfolio.html">Ver todas as obras</a></div>
<div class="ogrid">{obras}</div></div></section>

<section class="sec warm" id="empresa"><div class="colgraf" aria-hidden="true"><i></i><i></i><i></i><i></i></div><div class="wrap split"><div class="sphoto"><img src="{IMG}team-1920.jpg" alt="Equipe da Miletus Engenharia em obra"></div>
<div class="stext">{eyebrow("Quem somos")}<h2>Grandes estruturas pedem <b>engenharia à altura.</b></h2><p class="lead">Rigor técnico e segurança em cada decisão, do primeiro cálculo à última inspeção.</p>
<p>Com mais de dez anos de experiência em barragens e projetos estruturais, levamos aos nossos clientes precisão nas soluções, previsibilidade de custo e prazo e a confiança de uma estrutura bem resolvida.</p>
<a class="btn" href="#contato">Conheça a Miletus</a></div></div></section>

<section class="sec"><div class="wrap"><div class="shead"><div>{eyebrow("Clientes")}<h2>Quem confia <b>na gente</b></h2></div></div></div>
<div class="loop"><div class="track">{logos}{logos}</div></div></section>

<section class="contact" id="contato"><div class="cphoto"><img src="{IMG}01_drone-barragens-santa-barbara-entre-cafezais.jpg" alt=""></div>
<div class="cbody">{eyebrow("Contato")}<h2>Fale com um <b>especialista</b></h2><p class="sub">Conte qual é a estrutura e em que momento está a obra.</p>{form()}
<p class="direct"><a href="{WHATS}" target="_blank" rel="noopener">WhatsApp {TEL}</a> · <a href="mailto:{MAIL}">{MAIL}</a></p></div></section>
''' + footer("")

def servicos():
    tabs = ''.join(f'<a role="tab" href="#{s["slug"]}" data-tab="{s["slug"]}">{s["nome"]}</a>' for s in SERVICOS)
    panels = ''
    for i, s in enumerate(SERVICOS, 1):
        ent = ''.join(f'<li>{e}</li>' for e in s["entregas"])
        panels += (f'<article class="panel" id="{s["slug"]}" role="tabpanel"><div class="pimg"><img src="{IMG}{s["img"]}" alt="{s["nome"]}"></div>'
                   f'<div class="ptxt"><p class="eyebrow">{i:02d}</p><h2>{s["nome"]}</h2><p class="frase">{s["frase"]}</p><p class="desc">{s["desc"]}</p>'
                   f'<h4 class="eyebrow">Entregas</h4><ul class="ent">{ent}</ul><a class="btn" href="index.html#contato">Falar com um especialista</a></div></article>')
    return (head("Serviços | Miletus Engenharia", "O que cada serviço da Miletus entrega para a sua obra.", "") + header("", "Serviços")
            + page_hero("Serviços", "Serviços", "O que cada serviço entrega para a sua obra.", "p09-1920.jpg")
            + f'<section class="sec"><div class="wrap"><div class="tabs" role="tablist">{tabs}</div>{panels}</div></section>' + footer(""))

def portfolio():
    cards = ''.join(obra_card(o) for o in OBRAS)
    return (head("Obras | Miletus Engenharia", "Projetos e supervisões da Miletus em pontes, contenções, edificações e barragens.", "") + header("", "Obras")
            + page_hero("Obras", "Obras", "Projetos e supervisões da Miletus em pontes, contenções, edificações e barragens.", "hero-piraque-1920.jpg")
            + f'<section class="sec"><div class="wrap"><div class="ogrid">{cards}</div><div class="cta"><a class="btn" href="index.html#contato">Falar com um especialista</a></div></div></section>'
            + footer(""))

def ficha(o):
    r = "../"
    slides = ''.join(f'<img src="{r}{IMG}{g}" alt="{o["nome"]}, imagem {i+1}" {"class=on" if i == 0 else ""}>' for i, g in enumerate(o["galeria"]))
    n = len(o["galeria"])
    nav = (f'<div class="gnav"><button class="gprev" aria-label="Imagem anterior">‹</button><button class="gnext" aria-label="Próxima imagem">›</button>'
           f'<span class="gcount">01 / {n:02d}</span></div>') if n > 1 else ''
    return (head(f'{o["nome"]} | Miletus Engenharia', f'{o["tipo"]}: {o["destaque"]}.', r) + header(r, "Obras")
            + f'''<section class="sec ficha"><div class="wrap"><a class="back" href="{r}portfolio.html">← Obras</a>
<div class="fgrid2"><div class="gallery" data-n="{n}"><div class="gview">{slides}</div>{nav}</div>
<div class="finfo"><p class="eyebrow">{o["tipo"]}</p><h1>{o["nome"]}</h1><p class="fmeta">{o["contratante"]}</p><p class="fmeta">{o["local"]}</p>
{ncards(o["nums"], "n3")}</div></div>
<div class="cer"><div><p class="eyebrow">Contexto</p><p>{o["contexto"]}</p></div><div><p class="eyebrow">Entrega</p><p>{o["entrega"]}</p></div>
<div><p class="eyebrow">Resultado</p><p>{o["resultado"]}</p></div></div>
<div class="cta"><a class="btn" href="{r}index.html#contato">Falar com um especialista</a></div></div></section>''' + footer(r))

def creditos():
    rows = ''.join(f'<li><b>{u}</b> · {t}, por {a} ({l}) · <a href="{h}" target="_blank" rel="noopener">fonte</a></li>' for u, t, a, l, h in CREDITOS)
    return (head("Créditos das imagens | Miletus Engenharia", "Créditos das imagens de banco usadas no site.", "") + header("", "")
            + f'<section class="sec"><div class="wrap"><h1 class="ctitle">Créditos das imagens</h1><ul class="creds">{rows}</ul></div></section>' + footer(""))

def write(path, html):
    # Acentos viram entidades HTML (&#233; etc.): o texto aparece certo em qualquer navegador/editor,
    # mesmo que o arquivo seja aberto com a codificação errada.
    safe = html.encode("ascii", "xmlcharrefreplace").decode("ascii")
    with open(os.path.join(HERE, path), "w", encoding="utf-8") as f: f.write(safe)

write("index.html", index())
write("servicos.html", servicos())
write("portfolio.html", portfolio())
write("creditos.html", creditos())
for o in OBRAS: write(f"obras/{o['slug']}.html", ficha(o))
print("ok:", 3 + len(OBRAS), "páginas")
