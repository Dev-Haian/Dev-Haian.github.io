"""Gera as 4 páginas de case com o mesmo esqueleto."""
from pathlib import Path

OUT = Path(__file__).parent / 'cases'
OUT.mkdir(exist_ok=True)

P, Q = '#8b9cff', '#6fd3b8'
SURF, RAISED, LINE, TEXT, MUTED = '#15181d', '#1c2027', '#2e343d', '#f5f5f5', '#9ca3af'

HEAD = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Haian Vilas Boas</title>
<meta name="description" content="{desc}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%230b0d10'/%3E%3Crect x='7' y='9' width='18' height='3' rx='1.5' fill='%238b9cff'/%3E%3Crect x='7' y='20' width='18' height='3' rx='1.5' fill='%236fd3b8'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/style.css?v=4">
</head>
<body class="{lane}-page">
<nav class="nav" aria-label="Principal"><div class="wrap">
  <a class="brand" href="../">Haian Vilas Boas</a>
  <ul><li><a href="../#cases">Cases</a></li><li><a href="../#contato">Contato</a></li></ul>
</div></nav>
"""

FOOT = """<footer><div class="wrap">Haian Vilas Boas · Case descrito em nível conceitual, sem dados, regras proprietárias ou endereços internos da empresa.</div></footer>
</body></html>"""


def box(x, y, w, h, label, sub='', color=None, fill=SURF):
    stroke = color or LINE
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>'
    cy = y + h / 2 + (-8 if sub else 6)
    s += f'<text x="{x + w / 2}" y="{cy}" text-anchor="middle" font-size="17" font-weight="700" fill="{TEXT}">{label}</text>'
    if sub:
        s += f'<text x="{x + w / 2}" y="{cy + 21}" text-anchor="middle" font-size="14" fill="{MUTED}">{sub}</text>'
    return s


def arrow(x1, y1, x2, y2, color=MUTED, dash=False):
    d = ' stroke-dasharray="5 5"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="1.6"{d} marker-end="url(#a)"/>'


def svg(w, h, body, color):
    return (f'<svg viewBox="0 0 {w} {h}" role="img" xmlns="http://www.w3.org/2000/svg"><defs>'
            f'<marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0 0 L10 5 L0 10z" fill="{MUTED}"/></marker></defs>{body}</svg>')


def page(slug, lane, title, desc, lead, meta, sections, prev, nxt):
    lane_name = 'Produto' if lane == 'p' else 'Qualidade'
    meta_html = ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in meta)
    toc = ''.join(f'<a href="#{sid}">{st}</a>' for sid, st, _ in sections)
    body = ''.join(f'<section id="{sid}"><h2>{st}</h2>{html}</section>' for sid, st, html in sections)
    nav = (f'<div class="next"><a href="{prev[0]}"><small>Case anterior</small><strong>{prev[1]}</strong></a>'
           f'<a href="{nxt[0]}"><small>Próximo case</small><strong>{nxt[1]}</strong></a></div>')
    html = (HEAD.format(title=title, desc=desc, lane=lane) +
            f"""<header class="case-hero"><div class="wrap">
  <a class="back" href="../#cases">Voltar para os cases</a><br>
  <span class="lane {lane}"><i></i>{lane_name}</span>
  <h1>{title}</h1>
  <p class="lead">{lead}</p>
  <dl class="meta">{meta_html}</dl>
</div></header>
<main class="article"><div class="wrap">
  <aside aria-label="Nesta página">{toc}</aside>
  <div>{body}{nav}</div>
</div></main>
""" + FOOT)
    (OUT / f'{slug}.html').write_text(html, encoding='utf-8')


# ------------------------------------------------------------------ PRODUTO 1
d1 = svg(1000, 130, ''.join([
    box(5, 30, 150, 70, 'Entender', 'o produto', P),
    arrow(155, 65, 172, 65),
    box(175, 30, 150, 70, 'Simular', 'carta e parcela', P),
    arrow(325, 65, 342, 65),
    box(345, 30, 150, 70, 'Explorar', 'estratégias', P),
    arrow(495, 65, 512, 65),
    box(515, 30, 150, 70, 'Contemplação', 'expectativa', P),
    arrow(665, 65, 682, 65),
    box(685, 30, 150, 70, 'Lances', 'impacto no crédito', P),
    arrow(835, 65, 852, 65),
    box(855, 30, 140, 70, 'Decidir', 'proposta', P, '#20263b'),
]), P)

d1b = svg(1000, 420, ''.join([
    box(400, 10, 200, 56, 'Simulação', '', P, '#20263b'),
    arrow(450, 66, 200, 110), arrow(500, 66, 500, 110), arrow(550, 66, 800, 110),
    box(110, 112, 180, 56, 'Carta', 'valor do crédito'),
    box(410, 112, 180, 56, 'Parcela', 'quanto cabe no bolso'),
    box(710, 112, 180, 56, 'Prazo', 'meses do grupo'),
    arrow(200, 168, 470, 208), arrow(500, 168, 500, 208), arrow(800, 168, 530, 208),
    box(380, 210, 240, 56, 'Estratégia', 'objetivo do cliente', P),
    arrow(450, 266, 200, 306), arrow(500, 266, 500, 306), arrow(550, 266, 800, 306),
    box(110, 308, 180, 56, 'Sorteio', 'sem custo extra'),
    box(410, 308, 180, 56, 'Lance livre', 'recurso próprio'),
    box(710, 308, 180, 56, 'Lance embutido', 'usa parte da carta'),
    arrow(290, 336, 405, 395, MUTED, True), arrow(800, 364, 600, 395, MUTED, True),
    box(400, 370, 200, 46, 'Crédito líquido', '', P, '#20263b'),
]), P)

def funnel():
    rows = [('simulações', '958', 'R$ 1,64 bi em crédito simulado', 960, ''),
            ('propostas', '124', 'R$ 32,7 mi em propostas', 560, '12,9% das simulações'),
            ('contratos', '36', 'R$ 12,0 mi em contratos fechados', 300, '29,0% das propostas')]
    out = ''
    for i, (lab, num, val, w, conv) in enumerate(rows):
        y = 26 + i * 96
        x = (1000 - w) / 2
        out += f'<rect x="{x}" y="{y}" width="{w}" height="70" rx="10" fill="#20263b" stroke="{P}" stroke-width="1.5"/>'
        out += f'<text x="500" y="{y + 32}" text-anchor="middle" font-size="24" font-weight="800" fill="{TEXT}">{num} {lab}</text>'
        out += f'<text x="500" y="{y + 55}" text-anchor="middle" font-size="14" fill="{MUTED}">{val}</text>'
        if conv:
            out += f'<text x="{x + w + 16}" y="{y + 40}" font-size="15" font-weight="700" fill="{P}">{conv}</text>'
    return svg(1000, 310, out, P)

d1c = funnel()

FONTES = ('<p class="small muted">Fontes: ABAC, <a href="https://blog.abac.org.br/drops-de-mercado/sistema-de-consorcios-em-dezembro-2025-dados-economicos">Sistema de Consórcios em dezembro de 2025</a> e '
          '<a href="https://blog.abac.org.br/drops-de-mercado/sistema-de-consorcios-em-maio-2026-dados-economicos">Sistema de Consórcios em maio de 2026</a>.</p>')

page('consorcio-como-investimento', 'p', 'Consórcio como investimento: de uma jornada de venda para uma jornada de decisão',
     'Case de produto: como transformar conhecimento de consórcio em uma experiência digital de decisão.',
     'O desafio não era só digitalizar a venda de consórcio. Era colocar dentro da jornada o conhecimento necessário para o cliente e o vendedor entenderem o que estavam contratando.',
     [('Empresa', 'Teddy Open Finance'), ('Meu papel', 'Produto, negócio e QA'), ('Lançamento', 'março de 2026'), ('Com quem', 'PO, Tech Lead, devs, negócio')],
     [
         ('mercado', 'O mercado', '<p>O consórcio vive o melhor momento da sua história no Brasil. Em 2025, o sistema passou pela primeira vez de <strong>12 milhões de participantes ativos</strong>, vendeu <strong>5,16 milhões de cotas</strong> (15% a mais que em 2024) e somou <strong>R$ 500 bilhões em créditos comercializados</strong>, alta de 32%. De janeiro a maio de 2026, foram mais 2,36 milhões de adesões, 14% acima do mesmo período do ano anterior.</p><p>Junto com o volume, mudou o discurso: o consórcio passou a ser apresentado também como ferramenta de <strong>planejamento financeiro</strong>, e não só como forma de comprar um bem.</p>' + FONTES),
         ('contexto', 'Contexto', '<p>A empresa já tinha forte atuação em educação sobre consórcio e decidiu ampliar o portfólio com uma nova modalidade: <strong>Consórcio como Investimento</strong>.</p><p>O desafio é que esse produto só faz sentido para quem entende contemplação, lances, crédito e regras do grupo. Uma tela de simulação comum não resolvia.</p>'),
         ('problema', 'O problema', '<div class="callout"><p>O mercado já vendia consórcio. O desafio era vender conhecimento suficiente para que a pessoa entendesse o que estava contratando.</p></div><p>A jornada tradicional seguia uma lógica simples: escolher carta, escolher prazo, ver parcela, enviar proposta. Para o novo produto, cliente e vendedor precisavam responder perguntas que essa jornada não respondia:</p><ul><li>Qual carta faz sentido para o meu objetivo, e qual parcela consigo assumir?</li><li>Como funciona a contemplação, e quanto tempo pode levar?</li><li>O que acontece se eu ofertar um lance? Qual percentual faz sentido?</li><li>Como cada estratégia muda o resultado, e qual o impacto do lance no crédito que recebo?</li></ul>'),
         ('insight', 'O insight', '<p>O problema não estava na falta de funcionalidades. Estava na <strong>falta de contexto para interpretar as informações</strong>. O usuário via uma carta e uma parcela, mas não entendia o comportamento daquela escolha.</p><div class="callout"><p>A proposta mudou de "vamos criar uma calculadora de consórcio" para "vamos criar uma ferramenta que ajude a entender e comparar estratégias".</p></div>'),
         ('solucao', 'A solução', f'<p>A jornada passou a juntar educação, simulação e análise, em vez de terminar na parcela:</p><figure class="diagram">{d1}<figcaption>Cada etapa responde uma dúvida antes de o cliente chegar à proposta.</figcaption></figure><ul><li><strong>Simulação por crédito ou por parcela</strong>, partindo do que o cliente sabe responder.</li><li><strong>Estratégias comparadas lado a lado</strong>, cada uma com resultado estimado, valor investido até a contemplação e percentual de retorno.</li><li><strong>Expectativa de contemplação</strong> a partir de dados históricos dos grupos, em vez de prometer uma data.</li><li><strong>Lances explicados:</strong> o lance embutido, por exemplo, usa parte da própria carta e reduz o crédito líquido. A tela mostra esse efeito antes da decisão.</li></ul><figure class="shot"><img src="../assets/conkey-estrategias.png" alt="Tela de resultado da simulação com as estratégias Venda da carta, Alavancagem Patrimonial e Previdência Exponencial lado a lado" loading="lazy" width="1154" height="500"><figcaption>Resultado da simulação: a mesma carta de R$ 102,5 mil apresentada em três estratégias (venda da carta, alavancagem patrimonial e previdência), com retorno estimado de 67% a 247%.</figcaption></figure>'),
         ('complexidade', 'O que existe por trás de uma simulação', f'<p>Uma tela que parece simples esconde uma árvore de regras. Cada combinação precisava estar certa na tela, na API e no documento gerado.</p><figure class="diagram">{d1b}<figcaption>Carta, parcela e prazo definem a estratégia. A forma de contemplação muda o crédito que o cliente realmente recebe.</figcaption></figure>'),
         ('atuacao', 'Minha atuação', '<p>Atuei conectando Produto, Negócio, Desenvolvimento e Qualidade, principalmente na tradução das regras do mercado de consórcio para uma experiência digital compreensível e validável.</p><ul><li><strong>Produto:</strong> entendimento do problema, necessidades de cliente e vendedor, definição da jornada, regras de negócio, cenários e critérios de aceite, discussão de alternativas de solução.</li><li><strong>Negócio:</strong> regras das administradoras, análise das estratégias de lance, comportamento de contemplação, alinhamento com stakeholders.</li><li><strong>Qualidade:</strong> análise de riscos, validação dos cálculos, testes funcionais, exploratórios e de cenários extremos, validação de integrações e conferência entre tela, cálculo e documentos.</li></ul>'),
         ('resultado', '6 meses depois do lançamento', f'<p>De março a setembro de 2026, considerando só a finalidade Investimento no painel de vendas:</p><figure class="diagram">{d1c}<figcaption>Funil da modalidade Consórcio como Investimento, de 1º de março a 25 de setembro de 2026.</figcaption></figure><div class="numbers"><div><b>958</b><span>simulações, somando R$ 1,64 bilhão em crédito simulado</span></div><div><b>12,9%</b><span>das simulações viraram proposta (124 propostas)</span></div><div><b>R$ 12 mi</b><span>em 36 contratos fechados, 29% das propostas</span></div></div><p>Quase 3 em cada 10 propostas viraram contrato, num produto que o cliente precisava entender antes de comprar. É o sinal de que a jornada fez o trabalho de explicar: quem chegava à proposta já sabia o que estava contratando.</p><figure class="shot"><img src="../assets/conkey-hub-vendas.png" alt="Painel de vendas filtrado pela finalidade Investimento: 958 simulações, 124 propostas e 36 ganhos" loading="lazy" width="991" height="344"><figcaption>Painel de vendas filtrado pela finalidade Investimento.</figcaption></figure>'),
         ('aprendizado', 'O que aprendi', '<p>Em produto financeiro, a parte difícil não é a tela, é a regra. E o cliente não compra o que não entende. Colocar o conhecimento dentro da jornada foi o que transformou uma calculadora em uma ferramenta de decisão.</p><div class="callout"><p>O desafio não era colocar o consórcio na tela. Era colocar dentro da jornada o conhecimento necessário para tomar uma decisão.</p></div>'),
     ],
     ('plataforma-de-automacao.html', 'Plataforma de automação E2E'), ('compra-de-bens-e-servicos.html', 'Compra de bens e serviços'))

# ------------------------------------------------------------------ PRODUTO 2
d2 = svg(1000, 290, ''.join([
    box(10, 110, 170, 70, 'Objetivo do cliente', 'valor, prazo, parcela', P),
    arrow(180, 130, 255, 70), arrow(180, 160, 255, 220),
    box(260, 35, 230, 70, 'Busca inteligente', 'o sistema sugere as cotas', P, '#20263b'),
    box(260, 185, 230, 70, 'Busca manual', 'o cliente escolhe a cota', P),
    arrow(490, 70, 560, 130), arrow(490, 220, 560, 160),
    box(565, 110, 190, 70, 'Simulação', 'uma regra só', P),
    arrow(755, 145, 805, 145),
    box(810, 110, 180, 70, 'Proposta', 'cota reservada'),
]), P)

page('compra-de-bens-e-servicos', 'p', 'Jornada de compra de bens e serviços',
     'Case de produto: jornada de busca inteligente e busca manual de cotas, da simulação à proposta.',
     'Uma mesma necessidade, dois tipos de cliente: quem quer que o sistema encontre a melhor opção e quem já sabe o que quer. O desafio foi atender os dois sem duplicar regras.',
     [('Empresa', 'Teddy Open Finance'), ('Meu papel', 'Regras, fluxos e critérios'), ('Período', '2025 – 2026'), ('Com quem', 'PO, design, devs, negócio')],
     [
         ('contexto', 'Contexto', '<p>O cliente chega com um objetivo concreto: um carro, um imóvel, uma reforma, um serviço. Para chegar lá pelo consórcio, ele precisa encontrar uma cota compatível com o valor, o prazo e a parcela que cabe no bolso.</p>'),
         ('problema', 'O problema', '<div class="callout"><p>Parte dos clientes quer uma recomendação pronta. Outra parte, geralmente mais experiente, quer comparar e escolher. Duas jornadas separadas teriam o risco de calcular a mesma coisa de dois jeitos diferentes.</p></div>'),
         ('o-que-fiz', 'O que eu fiz', '<ul><li><strong>Estruturei as duas jornadas</strong>: a busca inteligente, que sugere cotas a partir do objetivo, e a busca manual, em que o cliente filtra e escolhe.</li><li><strong>Defini uma única fonte de regras</strong> para a simulação, usada pelos dois caminhos, para que o mesmo cenário sempre gere o mesmo resultado.</li><li><strong>Mapeei as exceções</strong>: cota indisponível no meio do fluxo, valor fora da faixa, troca de caminho no meio da jornada.</li><li><strong>Escrevi os critérios de aceite</strong> de cada etapa, da busca à proposta, e validei os protótipos com o time de design.</li><li><strong>Levei essas jornadas para a automação</strong>: simulação e proposta pelos dois caminhos entraram na suíte de jornadas críticas.</li></ul>' + f'<figure class="diagram">{d2}<figcaption>Dois caminhos de entrada, uma regra de simulação. É o que garante que a recomendação e a escolha manual mostrem o mesmo valor.</figcaption></figure>'),
         ('resultado', 'Resultado', '<div class="numbers"><div><b>2</b><span>caminhos de compra para perfis diferentes de cliente</span></div><div><b>1</b><span>regra de simulação compartilhada, sem cálculo duplicado</span></div><div><b>4</b><span>jornadas (simulação e proposta × 2) cobertas por automação</span></div></div>'),
         ('aprendizado', 'O que aprendi', '<p>Dar opção ao cliente é bom; duplicar a lógica por trás das opções é caro. A decisão de produto mais importante deste case não aparece na tela: é a regra única por baixo das duas jornadas.</p>'),
     ],
     ('consorcio-como-investimento.html', 'Consórcio como investimento'), ('simulakey.html', 'Simulakey'))

# ------------------------------------------------------------------ QUALIDADE 1
d3 = svg(1000, 260, ''.join([
    box(10, 40, 140, 66, 'Commit', 'mudança no código'),
    arrow(150, 73, 185, 73),
    box(190, 40, 140, 66, 'Build', 'pipeline'),
    arrow(330, 73, 365, 73),
    box(370, 25, 220, 96, 'Suíte de regressão', 'cálculos e fluxo de simulação', Q, '#17302b'),
    arrow(590, 55, 665, 40, Q), arrow(590, 95, 665, 165, '#e07a7a'),
    box(670, 10, 150, 60, 'Passou', 'deploy segue', Q),
    box(670, 135, 150, 60, 'Falhou', 'deploy barrado', '#e07a7a'),
    arrow(820, 40, 855, 40, Q),
    box(860, 10, 130, 60, 'Produção'),
    box(370, 180, 220, 62, 'Health check', 'serviço no ar em HML e PROD'),
    arrow(480, 180, 480, 123, MUTED, True),
]), Q)

page('simulakey', 'q', 'Simulakey: proteger um sistema frágil a cada deploy',
     'Case de qualidade: automação de regressão na pipeline de um simulador com arquitetura frágil.',
     'O Simulakey era o simulador de consórcio: o primeiro número que o cliente vê. A arquitetura era ruim e qualquer mudança podia quebrar um cálculo em outro lugar. A reescrita não ia acontecer tão cedo, então era preciso proteger o que existia.',
     [('Empresa', 'Teddy Open Finance'), ('Meu papel', 'QA responsável pela estratégia'), ('Período', '2025 – 2026'), ('Ferramentas', 'Playwright, CI, health check')],
     [
         ('contexto', 'Contexto', '<p>Sistemas legados com alto acoplamento têm um sintoma clássico: uma correção em um ponto causa erro em outro, sem relação aparente. No Simulakey, isso significava risco de mostrar ao cliente uma parcela ou um crédito errado.</p>'),
         ('problema', 'O problema', '<div class="callout"><p>Testar manualmente tudo a cada deploy não escalava. Depender de reescrita também não era uma opção. Como dar segurança ao time para continuar entregando num sistema em que ninguém confiava?</p></div>'),
         ('o-que-fiz', 'O que eu fiz', '<ul><li><strong>Mapeei onde o sistema mais quebrava</strong>: os cálculos e os passos da simulação que mais geravam regressão.</li><li><strong>Criei uma suíte de regressão automatizada</strong> focada nesses pontos, com cenários orientados a dados para cobrir as combinações de regra.</li><li><strong>Coloquei a suíte na pipeline</strong>: ela roda a cada deploy e, se falhar, o deploy não segue.</li><li><strong>Adicionei health check do serviço</strong> em homologação e produção, para separar na hora "o sistema caiu" de "o teste achou um bug".</li><li><strong>Documentei os riscos de arquitetura</strong> que os testes revelaram, como insumo para a priorização da reescrita.</li></ul>' + f'<figure class="diagram">{d3}<figcaption>A suíte funciona como um portão: nenhum deploy chega a produção sem passar pela regressão dos cálculos.</figcaption></figure>'),
         ('resultado', 'Resultado', '<div class="numbers"><div><b>Cada deploy</b><span>passa pela regressão automática antes de produção</span></div><div><b>Antes do cliente</b><span>regressões de cálculo barradas na pipeline</span></div><div><b>HML e PROD</b><span>com health check do serviço</span></div></div><p>O time voltou a entregar com confiança num sistema frágil, e a discussão sobre reescrever passou a ter dados: onde quebra, quanto e por quê.</p>'),
         ('aprendizado', 'O que aprendi', '<p>Nem todo problema de qualidade se resolve com mais testes manuais ou com uma reescrita. Às vezes, a melhor decisão é uma rede de segurança no lugar certo da pipeline, enquanto a solução definitiva não chega.</p>'),
     ],
     ('compra-de-bens-e-servicos.html', 'Compra de bens e serviços'), ('plataforma-de-automacao.html', 'Plataforma de automação E2E'))

# ------------------------------------------------------------------ QUALIDADE 2
d4 = svg(1000, 330, ''.join([
    box(10, 20, 200, 64, 'Agendador', 'a cada 5 min e a cada 6 h'),
    box(10, 133, 200, 64, 'GitHub Actions', 'a cada mudança'),
    arrow(210, 52, 275, 85), arrow(210, 165, 275, 125),
    box(280, 20, 220, 64, 'Web · Playwright', '8 jornadas, 4 resoluções', Q, '#17302b'),
    box(280, 120, 220, 64, 'Mobile · Appium', 'app Android', Q, '#17302b'),
    box(280, 220, 220, 64, 'Health check', 'microsserviços HML e PROD', Q, '#17302b'),
    arrow(500, 52, 575, 140), arrow(500, 152, 575, 152), arrow(500, 252, 575, 165),
    box(580, 115, 170, 76, 'Resultados', 'histórico e tempos'),
    arrow(750, 135, 815, 60), arrow(750, 172, 815, 240),
    box(820, 25, 170, 70, 'Portal', 'saúde em tempo real'),
    box(820, 205, 170, 70, 'Teams', 'ao cair e ao voltar', '#e07a7a'),
]), Q)

page('plataforma-de-automacao', 'q', 'Plataforma de automação E2E com monitoramento',
     'Case de qualidade: automação E2E web e mobile com alertas no Teams, insights de performance, arquitetura de testes e monitoramento em tempo real.',
     'Os resultados de automação estavam espalhados, a regressão era manual e ninguém sabia que algo tinha quebrado até um cliente reclamar. Construí uma plataforma que testa, monitora e avisa sozinha.',
     [('Empresa', 'Teddy Open Finance'), ('Meu papel', 'Arquitetura e desenvolvimento'), ('Período', '2025 – 2026'), ('Stack', 'Playwright, TS, Appium, React, Node')],
     [
         ('contexto', 'Contexto', '<p>A squad tinha jornadas críticas para a receita (login, simulação e criação de proposta, por três caminhos diferentes) e um aplicativo Android. A regressão completa era feita à mão e levava horas, e falhas em produção eram descobertas tarde.</p>'),
         ('problema', 'O problema', '<div class="callout"><p>Como saber, a qualquer momento, se o produto está funcionando? E como fazer isso sem depender de alguém rodar testes manualmente e sem encher o time de alertas que ninguém lê?</p></div>'),
         ('arquitetura', 'Arquitetura de testes', '<p>Organizei tudo em um monorepo com quatro partes que conversam entre si:</p><ul><li><strong>Web:</strong> Playwright + TypeScript, Page Objects, fixtures, login reaproveitado e as jornadas rodando em 4 resoluções (Full HD, notebook, tablet e celular).</li><li><strong>Mobile:</strong> WebdriverIO + Appium para o app Android, com evidências em vídeo e logs.</li><li><strong>Health check:</strong> verificação dos microsserviços em homologação e produção, com uma regra clara de DOWN (HTTP 408, 500, 502, 504 ou timeout).</li><li><strong>Portal:</strong> React + Node.js reunindo execuções, histórico e evidências por squad e ambiente.</li></ul>' + f'<figure class="diagram">{d4}<figcaption>Execução agendada e por evento, resultados centralizados, e só dois destinos para a informação: o portal para quem quer olhar, o Teams para quando algo muda.</figcaption></figure>'),
         ('monitoramento', 'Monitoramento e alertas', '<ul><li><strong>Tempo real:</strong> smoke e health check a cada 5 minutos, jornadas críticas a cada 6 horas.</li><li><strong>Alertas no Teams só em mudanças</strong>: quando um serviço cai e quando volta. Alerta repetido vira ruído e o time para de ler.</li><li><strong>Evidência junto do alerta</strong>: o link leva direto ao trace, ao vídeo e aos logs da falha.</li></ul>'),
         ('insights', 'Insights de performance', '<p>Cada jornada registra quanto tempo leva automatizada e quanto levaria manualmente. O portal transforma isso em indicadores para a liderança: tempo por jornada, tendência de lentidão e economia gerada pela automação.</p><div class="numbers"><div><b>~2 h → 15 min</b><span>regressão das 8 jornadas críticas (estimativa do próprio relatório)</span></div><div><b>5 min</b><span>intervalo do smoke e do health check</span></div><div><b>Web + mobile</b><span>em um só painel, com histórico</span></div></div>'),
         ('aprendizado', 'O que aprendi', '<p>Automação só gera valor quando alguém usa o resultado. Mais do que escrever testes, o trabalho foi decidir o que medir, quando avisar e para quem, para que a informação chegasse ao time na hora certa.</p><p>Uma versão pública da mesma arquitetura, sem dados da empresa, está no meu GitHub: <a href="https://github.com/Dev-Haian/playwright-e2e-api">playwright-e2e-api</a>, com o <a href="https://dev-haian.github.io/playwright-e2e-api/">relatório</a> e o <a href="https://dev-haian.github.io/playwright-e2e-api/health/">painel de health check</a> no ar.</p>'),
     ],
     ('simulakey.html', 'Simulakey'), ('consorcio-como-investimento.html', 'Consórcio como investimento'))

print('ok')
