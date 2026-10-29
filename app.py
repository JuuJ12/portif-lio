import html

import streamlit as st

st.set_page_config(
    page_title="Julio Vitor dos Santos | IA, agentes e dados",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ======================================================================
# CONTEÚDO (edite só esta parte para atualizar o portfólio)
# ======================================================================
EMAIL = "juliovitortb99@gmail.com"
GITHUB = "https://github.com/JuuJ12"
LOCAL = "Recife, PE, Brasil"
TELEFONE = "(55) 81 983365989"  # deixe "" para não exibir no site público

INTRO = (
    "Construo agentes de IA que respondem perguntas de negócio com dados reais: "
    "orquestração em LangGraph, RAG, Text-to-SQL, APIs em FastAPI e pipelines em Databricks. "
    "Estudo Sistemas de Informação na UFRPE e sou bolsista de pesquisa PIBIC-CNPq."
)

FATOS = [
    "Agente LangGraph de 12 nós sobre 15 tabelas Gold em PostgreSQL",
    "RAG com pgvector e Text-to-SQL com validação e autocorreção",
    "Pipeline medalhão (Bronze, Silver, Gold) em Databricks a partir de 5 CSVs sujos",
    "3 certificações AWS Academy",
]

ATUACAO = [
    ("Agentes de IA", "Orquestração em LangGraph com roteamento, autocorreção, guardrails e recusa honesta quando faltam dados."),
    ("RAG e Text-to-SQL", "Perguntas em linguagem natural viram consultas seguras e respostas com fonte, usando pgvector, embeddings multilíngues e conferência numérica."),
    ("Engenharia de dados", "ETL em arquitetura medalhão com PySpark e Delta Lake, Star Schema e Databricks Workflow."),
    ("APIs e produtividade com IA", "APIs FastAPI com auditoria e feedback para portais web, e agentes de código (Claude Code, OpenCode, Copilot CLI) para acelerar refatorações, testes e migrações."),
]

FLUXO = [
    ("Pergunta", "linguagem natural"),
    ("Guardrails", "segurança, follow-up e escopo"),
    ("Roteador", "escolhe o caminho"),
    [("Text-to-SQL", "cache, geração, validação, execução"), ("RAG", "busca vetorial com pgvector")],
    ("Síntese", "conferência numérica"),
    ("Auditoria", "trilha e feedback"),
]

DESTAQUE = {
    "titulo": "V-Energy Grid 360: agente de IA com Text-to-SQL e RAG",
    "selo": "Case final, em equipe",
    "resumo": "Agente que responde perguntas das áreas comercial, de atendimento, de perdas e de operação de uma distribuidora de energia. Ele decide entre consultar o banco, buscar conhecimento regulatório ou recusar.",
    "pontos": [
        "Grafo LangGraph de 12 nós com roteamento entre SQL, RAG e recusa, sobre uma camada Gold de 15 tabelas em PostgreSQL.",
        "RAG com pgvector e embeddings multilíngues sobre regras ANEEL/PRODIST, glossário e dicionário de dados.",
        "Guardrails em camadas: filtro de prompt injection sem custo de LLM, verificação de escopo, validação de SQL e recusa honesta.",
        "Autocorreção de SQL, cache de perguntas certificadas e conferência numérica para evitar números inventados.",
        "Auditoria ponta a ponta com mascaramento de dados pessoais (LGPD), selos de confiança e API FastAPI para portal React.",
    ],
    "stack": ["Python", "LangGraph", "LangChain", "FastAPI", "PostgreSQL", "pgvector", "RAG", "Docker", "Pytest"],
}

PROJETOS = [
    {
        "titulo": "Agente Text-to-SQL para análise de filmes (CineData)",
        "resumo": "Agente em LangGraph sobre um Data Lakehouse com 95 mil filmes e 424 mil pessoas.",
        "pontos": [
            "Guardrail de escopo, geração de SQL com schema injetado, validação, execução e síntese da resposta.",
            "Executor seguro em camadas: parser AST com sqlglot, SQLite somente leitura, LIMIT automático e timeout.",
            "Testes com agentes simulados e interface Streamlit com gráficos e rastro das decisões.",
        ],
        "stack": ["LangGraph", "LangChain", "Python", "SQLite", "Pydantic", "Streamlit", "Pytest"],
        "links": [],
    },
    {
        "titulo": "Pipeline de engenharia de dados (CineData Analytics)",
        "resumo": "ETL em arquitetura medalhão que transforma 5 CSVs sujos (TMDB e IMDb) em um Star Schema pronto para análise e RAG.",
        "pontos": [
            "Deduplicação, datas em vários formatos, colunas deslocadas e validações de regras de negócio.",
            "API PTAX do Banco Central com forward fill para converter orçamento, receita e lucro para BRL.",
            "Tabela de contexto em linguagem natural para Vector Search, orquestrada com Databricks Workflow.",
        ],
        "stack": ["Databricks", "PySpark", "Delta Lake", "SQL", "Star Schema"],
        "links": [],
    },
    {
        "titulo": "Agentes IA Conversando (Agents Scientist)",
        "resumo": "Sistema multiagente em que agentes especializados geram hipóteses, revisam, classificam, evoluem e sintetizam resultados.",
        "pontos": [],
        "stack": ["Python", "Streamlit", "LLMs", "Groq", "LangChain"],
        "links": [("Abrir projeto", "https://agentesiaconversando.streamlit.app/agents_scientist")],
    },
    {
        "titulo": "Quantum Agents (Vibe Coding)",
        "resumo": "Pesquisa aplicada: LLMs, agentes e RAG geram circuitos quânticos a partir de linguagem natural, com fidelidade de 0,98 a 1,0 em benchmark de 5 casos.",
        "pontos": [],
        "stack": ["Python", "LangChain", "Qiskit", "RAG"],
        "links": [("Abrir projeto", "https://quantum-agents-vibe-coding.streamlit.app/")],
    },
]

COMPETENCIAS = [
    ("IA e LLMs", ["Agentes de IA", "LangGraph", "LangChain", "RAG", "Text-to-SQL", "Prompt Engineering", "Saída estruturada (Pydantic)", "pgvector", "sentence-transformers", "Guardrails", "Groq", "Google Gemini", "OpenRouter", "MCP", "Machine Learning", "Data Mining"], True),
    ("Agentes de código", ["Claude Code", "OpenCode", "GitHub Copilot CLI", "Orquestração multiagente", "Vibe coding", "Automação de processos", "Análise de dados com IA"], False),
    ("Engenharia de dados", ["Databricks", "PySpark", "Delta Lake", "Arquitetura Medalhão", "Star Schema", "ETL", "SQL", "PostgreSQL", "MySQL", "SQLite", "Pentaho", "Modelagem de dados"], False),
    ("Backend, web e cloud", ["Python", "FastAPI", "APIs REST", "Streamlit", "Next.js", "AWS", "Docker"], False),
    ("Qualidade e ferramentas", ["Git", "GitHub", "Pytest", "Jupyter", "MySQL Workbench", "Desenvolvimento ágil"], False),
    ("Pesquisa", ["Computação quântica (Qiskit)", "Pesquisa aplicada", "Documentação técnica"], False),
]

EXPERIENCIA = [
    ("Desenvolvedor de Sistemas e IA, projetos autorais", "Python, AWS, Streamlit, MySQL, FastAPI, Next.js",
     "Sistemas web multiagentes de IA com RAG, modelos de Machine Learning e Data Mining, e aplicações escaláveis na AWS e em Streamlit com MySQL (dashboards interativas e CRUD completo)."),
    ("Bolsista de Iniciação Científica (PIBIC-CNPq), UFRPE", "IA, LLMs, computação quântica",
     "Soluções baseadas em IA e computação quântica para geração inteligente de código, com pesquisa, testes e documentação técnica."),
    ("Pesquisador Aplicado, Quantum Vibe Coding", "LLMs, agentes de IA, LangChain, Qiskit",
     "Sistema multiagente (Gerador, Verificador e Revisor) com RAG para gerar circuitos quânticos a partir de linguagem natural."),
]

FORMACAO = [
    ("Bacharelado em Sistemas de Informação", "UFRPE, em curso"),
    ("Tecnólogo em Análise e Desenvolvimento de Sistemas", "Concluído"),
    ("Certificações AWS Academy Graduate", "Cloud Foundations, Machine Learning Foundations, Cloud Web Application Builder"),
    ("Idiomas", "Português nativo, inglês intermediário/avançado (programa Ganhe o Mundo), espanhol básico"),
]

# ======================================================================
# ESTILO
# ======================================================================
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800&family=Inter:wght@400;500;600&display=swap');
:root{--bg:#f4f6f8;--ink:#0f1b2d;--muted:#55657a;--line:#d6dee8;--accent:#0f766e;--dark:#0f1b2d;--dark-line:#27384f;--dark-muted:#a9b8cc;--mint:#5eead4}
html{scroll-behavior:smooth}
html,body,[class*="css"]{font-family:'Inter',sans-serif}
.stApp{background:var(--bg);color:var(--ink)}
[data-testid="stHeader"],[data-testid="stToolbar"],[data-testid="stDecoration"],[data-testid="stSidebar"],[data-testid="collapsedControl"],#MainMenu,footer{display:none!important}
.block-container{max-width:1040px;padding:5rem 1.25rem 3rem}
.stApp a{text-decoration:none!important}
.nav{position:fixed;top:0;left:0;right:0;z-index:999;display:flex;gap:1.4rem;align-items:center;overflow-x:auto;white-space:nowrap;padding:.85rem max(1.25rem,calc((100vw - 1040px)/2));background:rgba(244,246,248,.92);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
.nav b{font-family:'Bricolage Grotesque',sans-serif;font-weight:800;margin-right:auto;color:var(--ink)}
.nav a{color:var(--muted)!important;font-size:.9rem;font-weight:500}
.nav a:hover{color:var(--accent)!important}
.sec{scroll-margin-top:72px;padding-top:3.2rem}
.sec h2{font-family:'Bricolage Grotesque',sans-serif;font-weight:800;font-size:2rem;margin:0 0 .4rem;color:var(--ink)}
.sec .sub{color:var(--muted);margin:0 0 1.6rem;max-width:62ch;line-height:1.6}
.hero{padding:2.2rem 0 .5rem}
.hero h1{font-family:'Bricolage Grotesque',sans-serif;font-weight:800;font-size:clamp(2.6rem,6.5vw,4.6rem);line-height:1.02;margin:0 0 .8rem;color:var(--ink)}
.hero .role{font-size:1.25rem;font-weight:600;color:var(--accent);margin:0 0 1rem}
.hero .intro{font-size:1.08rem;line-height:1.7;color:var(--muted);max-width:62ch;margin:0 0 1.4rem}
.btns{display:flex;flex-wrap:wrap;gap:.6rem}
.btn{display:inline-block;padding:.62rem 1.1rem;border-radius:8px;font-weight:600;font-size:.92rem;border:1px solid var(--ink);color:var(--ink)!important;background:transparent}
.btn.main{background:var(--ink);color:#fff!important}
.btn:hover{border-color:var(--accent);color:var(--accent)!important}
.btn.main:hover{background:var(--accent);color:#fff!important}
.facts{list-style:none;padding:0;margin:1.8rem 0 0;display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:0;border-top:1px solid var(--line)}
.facts li{padding:1rem 1rem 1rem 0;color:var(--ink);font-size:.95rem;line-height:1.5;font-weight:500}
.duo{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.6rem 2.4rem}
.duo div{border-top:2px solid var(--accent);padding-top:.8rem}
.duo h3{font-size:1.08rem;margin:0 0 .35rem;color:var(--ink)}
.duo p{margin:0;color:var(--muted);line-height:1.65}
.tags{display:flex;flex-wrap:wrap;gap:.4rem;margin-top:.9rem}
.tag{padding:.22rem .6rem;border-radius:6px;border:1px solid var(--line);background:#fff;color:var(--ink);font-size:.8rem;font-weight:500}
.dark .tag{background:transparent;border-color:var(--dark-line);color:#dbe5f2}
.dark{background:var(--dark);color:#fff;border-radius:16px;padding:2rem}
.dark h3{font-family:'Bricolage Grotesque',sans-serif;font-size:1.6rem;margin:.3rem 0 .6rem;color:#fff}
.dark .badge{display:inline-block;padding:.2rem .6rem;border-radius:6px;background:var(--mint);color:#06201d;font-size:.78rem;font-weight:600}
.dark p.lead{color:var(--dark-muted);line-height:1.65;max-width:70ch;margin:0 0 1rem}
.dark ul{margin:0;padding-left:1.1rem;color:#dbe5f2;line-height:1.65}
.dark li{margin-bottom:.35rem}
.flowt{color:var(--dark-muted);font-size:.85rem;margin:1.6rem 0 .6rem;font-weight:500}
.flow{display:flex;flex-wrap:wrap;align-items:center;gap:.5rem}
.step{border:1px solid var(--dark-line);border-radius:8px;padding:.55rem .8rem;min-width:110px}
.step b{display:block;font-size:.88rem;color:#fff}
.step span{font-size:.76rem;color:var(--dark-muted)}
.branch{display:flex;flex-direction:column;gap:.4rem}
.branch .step{border-color:var(--mint)}
.arrow{color:var(--mint);font-weight:700}
.proj{border-top:1px solid var(--line);padding:1.6rem 0;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.5fr);gap:1.2rem 2.4rem}
.proj h3{font-size:1.12rem;margin:0 0 .4rem;color:var(--ink)}
.proj p{margin:0;color:var(--muted);line-height:1.65}
.proj ul{margin:0 0 .4rem;padding-left:1.1rem;color:var(--ink);line-height:1.65}
.proj .btn{margin-top:.9rem}
.skill{display:grid;grid-template-columns:200px 1fr;gap:.4rem 1.6rem;padding:1rem 0 1rem .9rem;border-top:1px solid var(--line);border-left:3px solid transparent}
.skill.hl{border-left-color:var(--accent);background:#fff}
.skill h3{font-size:1rem;margin:.1rem 0;color:var(--ink)}
.skill .tags{margin:0}
.tl{border-left:2px solid var(--line);padding-left:1.4rem;margin-left:.3rem}
.tl div{margin-bottom:1.6rem}
.tl h3{font-size:1.05rem;margin:0;color:var(--ink)}
.tl em{display:block;font-style:normal;color:var(--accent);font-weight:600;font-size:.88rem;margin:.15rem 0 .4rem}
.tl p{margin:0;color:var(--muted);line-height:1.65}
.edu{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:1.4rem 2rem}
.edu div{border-top:1px solid var(--line);padding-top:.8rem}
.edu h3{font-size:1rem;margin:0 0 .25rem;color:var(--ink)}
.edu p{margin:0;color:var(--muted);line-height:1.55;font-size:.92rem}
.foot{margin-top:3rem;padding-top:1.2rem;border-top:1px solid var(--line);color:var(--muted);font-size:.85rem}
@media(max-width:760px){.proj,.skill{grid-template-columns:1fr}.arrow{display:none}.step{flex:1 1 100%}}
</style>
"""

# ======================================================================
# COMPONENTES (HTML em uma linha para o Markdown não quebrar o bloco)
# ======================================================================
def e(texto):
    return html.escape(str(texto))


def tags(itens):
    return "".join(f'<span class="tag">{e(i)}</span>' for i in itens)


def botao(rotulo, url, principal=False):
    classe = "btn main" if principal else "btn"
    ext = "" if url.startswith(("#", "mailto:")) else ' target="_blank" rel="noopener noreferrer"'
    alvo = ' target="_self"' if url.startswith("#") else ext
    return f'<a class="{classe}" href="{e(url)}"{alvo}>{e(rotulo)}</a>'


def secao(id_, titulo, subtitulo, corpo):
    sub = f'<p class="sub">{e(subtitulo)}</p>' if subtitulo else ""
    return f'<section class="sec" id="{id_}"><h2>{e(titulo)}</h2>{sub}{corpo}</section>'


def fluxo_html():
    partes = []
    for item in FLUXO:
        if isinstance(item, list):
            ramos = "".join(f'<div class="step"><b>{e(t)}</b><span>{e(d)}</span></div>' for t, d in item)
            partes.append(f'<div class="branch">{ramos}</div>')
        else:
            partes.append(f'<div class="step"><b>{e(item[0])}</b><span>{e(item[1])}</span></div>')
    return '<span class="arrow">&rarr;</span>'.join(partes)


def destaque_html(p):
    pontos = "".join(f"<li>{e(x)}</li>" for x in p["pontos"])
    return (
        f'<article class="dark"><span class="badge">{e(p["selo"])}</span>'
        f'<h3>{e(p["titulo"])}</h3><p class="lead">{e(p["resumo"])}</p><ul>{pontos}</ul>'
        f'<div class="tags">{tags(p["stack"])}</div>'
        f'<p class="flowt">Como o agente processa uma pergunta</p><div class="flow">{fluxo_html()}</div></article>'
    )


def projeto_html(p):
    pontos = f'<ul>{"".join(f"<li>{e(x)}</li>" for x in p["pontos"])}</ul>' if p["pontos"] else ""
    links = "".join(botao(r, u) for r, u in p["links"])
    return (
        f'<article class="proj"><div><h3>{e(p["titulo"])}</h3><p>{e(p["resumo"])}</p>{links}</div>'
        f'<div>{pontos}<div class="tags" style="margin-top:.2rem">{tags(p["stack"])}</div></div></article>'
    )


def competencia_html(nome, itens, destaque):
    classe = "skill hl" if destaque else "skill"
    return f'<div class="{classe}"><h3>{e(nome)}</h3><div class="tags">{tags(itens)}</div></div>'


# ======================================================================
# PÁGINA ÚNICA
# ======================================================================
def render(bloco):
    st.markdown(bloco, unsafe_allow_html=True)


render(CSS)

render(
    '<nav class="nav"><b>Julio Vitor</b>'
    '<a href="#atuacao" target="_self">Atuação</a><a href="#projetos" target="_self">Projetos</a>'
    '<a href="#competencias" target="_self">Competências</a><a href="#experiencia" target="_self">Experiência</a>'
    '<a href="#formacao" target="_self">Formação</a><a href="#contato" target="_self">Contato</a></nav>'
)

render(
    '<header class="hero" id="inicio"><h1>Julio Vitor dos Santos</h1>'
    '<p class="role">Desenvolvedor de IA: agentes, LLMs, RAG e engenharia de dados</p>'
    f'<p class="intro">{e(INTRO)}</p>'
    f'<div class="btns">{botao("Ver projetos", "#projetos", True)}{botao("GitHub", GITHUB)}{botao("Enviar e-mail", "mailto:" + EMAIL)}</div>'
    f'<ul class="facts">{"".join(f"<li>{e(f)}</li>" for f in FATOS)}</ul></header>'
)

render(secao(
    "atuacao", "O que eu faço com IA", "Do dado bruto à resposta confiável, com agentes que sabem quando responder e quando recusar.",
    '<div class="duo">' + "".join(f"<div><h3>{e(t)}</h3><p>{e(d)}</p></div>" for t, d in ATUACAO) + "</div>",
))

render(secao(
    "projetos", "Projetos", "Começando pelo agente que melhor representa meu trabalho.",
    destaque_html(DESTAQUE) + "".join(projeto_html(p) for p in PROJETOS),
))

render(secao(
    "competencias", "Competências", "Tecnologias que uso nos projetos acima, de IA a dados e backend.",
    "".join(competencia_html(*c) for c in COMPETENCIAS),
))

render(secao(
    "experiencia", "Experiência e pesquisa", None,
    '<div class="tl">' + "".join(f"<div><h3>{e(t)}</h3><em>{e(s)}</em><p>{e(d)}</p></div>" for t, s, d in EXPERIENCIA) + "</div>",
))

render(secao(
    "formacao", "Formação, certificações e idiomas", None,
    '<div class="edu">' + "".join(f"<div><h3>{e(t)}</h3><p>{e(d)}</p></div>" for t, d in FORMACAO) + "</div>",
))

contato = f"{LOCAL}. Aberto a oportunidades remotas." + (f" Telefone: {TELEFONE}." if TELEFONE else "")
render(secao(
    "contato", "Contato", contato,
    f'<div class="btns">{botao("Enviar e-mail", "mailto:" + EMAIL, True)}{botao("GitHub", GITHUB)}</div>'
    '<div class="foot">Julio Vitor dos Santos. Feito com Python e Streamlit.</div>',
))