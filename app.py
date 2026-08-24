import streamlit as st

# ============================================================
# JULIO VITOR DOS SANTOS — PORTFÓLIO
# ============================================================

st.set_page_config(
    page_title="Julio Vitor | AI & Software",
    page_icon="IA",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- CSS ----------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at 85% 5%, rgba(99,102,241,.16), transparent 25%),
            radial-gradient(circle at 10% 20%, rgba(14,165,233,.10), transparent 22%),
            #0b1020;
    }

    .block-container {
        max-width: 1180px;
        padding-top: 2.5rem;
        padding-bottom: 4rem;
    }

    .hero {
        padding: 3.5rem 2.8rem;
        border: 1px solid rgba(148,163,184,.18);
        border-radius: 28px;
        background: linear-gradient(135deg, rgba(30,41,59,.92), rgba(15,23,42,.76));
        box-shadow: 0 20px 70px rgba(0,0,0,.28);
    }

    .eyebrow {
        color: #38bdf8;
        font-size: .85rem;
        font-weight: 800;
        letter-spacing: .16em;
        text-transform: uppercase;
    }

    .hero h1 {
        font-size: clamp(2.5rem, 6vw, 5rem);
        line-height: 1;
        margin: .6rem 0 1rem;
        font-weight: 800;
    }

    .hero h2 {
        color: #cbd5e1;
        font-size: clamp(1.15rem, 2vw, 1.55rem);
        font-weight: 500;
        margin-bottom: 1.2rem;
    }

    .hero p {
        color: #94a3b8;
        max-width: 760px;
        font-size: 1.05rem;
        line-height: 1.75;
    }

    .tag {
        display: inline-block;
        margin: .25rem .25rem .25rem 0;
        padding: .42rem .75rem;
        border-radius: 999px;
        background: rgba(56,189,248,.09);
        border: 1px solid rgba(56,189,248,.25);
        color: #bae6fd;
        font-size: .82rem;
    }

    .section-title {
        margin-top: 3.5rem;
        margin-bottom: 1.2rem;
        font-size: 1.8rem;
        font-weight: 800;
    }

    .section-subtitle {
        color: #94a3b8;
        margin-top: -.7rem;
        margin-bottom: 1.8rem;
    }

    .card {
        height: 100%;
        padding: 1.5rem;
        border-radius: 20px;
        background: rgba(15,23,42,.72);
        border: 1px solid rgba(148,163,184,.15);
        transition: .2s ease;
    }

    .card:hover {
        border-color: rgba(56,189,248,.42);
        transform: translateY(-2px);
    }

    .card h3 {
        margin-top: 0;
        margin-bottom: .6rem;
    }

    .card p, .card li {
        color: #aeb9ca;
        line-height: 1.65;
    }

    .metric {
        text-align: center;
        padding: 1.2rem;
        border-radius: 18px;
        background: rgba(15,23,42,.6);
        border: 1px solid rgba(148,163,184,.14);
    }

    .metric strong {
        display: block;
        font-size: 1.7rem;
        color: #f8fafc;
    }

    .metric span {
        color: #94a3b8;
        font-size: .85rem;
    }

    .timeline {
        border-left: 2px solid rgba(56,189,248,.35);
        padding-left: 1.5rem;
        margin-left: .5rem;
    }

    .timeline-item {
        margin-bottom: 2rem;
    }

    .timeline-item h3 {
        margin-bottom: .2rem;
    }

    .timeline-item .role {
        color: #38bdf8;
        font-weight: 600;
        font-size: .9rem;
    }

    .timeline-item p {
        color: #aeb9ca;
        line-height: 1.7;
    }

    .footer {
        text-align: center;
        color: #64748b;
        padding-top: 4rem;
    }

    a {
        text-decoration: none !important;
    }

    [data-testid="stSidebar"] {
        background: #080d1a;
        border-right: 1px solid rgba(148,163,184,.12);
    }
</style>
""", unsafe_allow_html=True)

# ---------- Sidebar ----------
with st.sidebar:
    st.markdown("##  Julio Vitor")
    st.caption("AI • Software • Data • Quantum")
    st.divider()

    page = st.radio(
        "Navegação",
        ["Início", "Competências", "Projetos", "Experiência", "Formação"],
        label_visibility="collapsed",
    )

    st.divider()
    st.markdown("### Contato")
    st.markdown("📍 Recife, PE — Brasil")
    st.markdown("📧 [juliovitortb99@gmail.com](mailto:juliovitortb99@gmail.com)")
    st.markdown("💻 [GitHub](https://github.com/JuuJ12)")
    st.caption("Disponível para oportunidades remotas.")

# ---------- Helpers ----------
def title(text, subtitle=None):
    st.markdown(f'<div class="section-title">{text}</div>', unsafe_allow_html=True)
    if subtitle:
        st.markdown(f'<div class="section-subtitle">{subtitle}</div>', unsafe_allow_html=True)

def tech_tags(items):
    return "".join(f'<span class="tag">{x}</span>' for x in items)

# ---------- HOME ----------
if page == "Início":
    st.markdown("""
    <div class="hero">
        <div class="eyebrow">Portfólio • Inteligência Artificial & Software</div>
        <h1>Julio Vitor<br>dos Santos</h1>
        <h2>Desenvolvedor de Sistemas & IA · Pesquisador em IA e Computação Quântica</h2>
        <p>
            Construo aplicações que combinam Python, Inteligência Artificial Generativa,
            LLMs, agentes de IA, Machine Learning, dados e computação quântica.
            Meu foco está em transformar pesquisa e tecnologia em soluções funcionais.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    c1, c2, c3, c4 = st.columns(4)
    for col, value, label in [
        (c1, "AI/LLMs", "Foco técnico"),
        (c2, "Python", "Principal linguagem"),
        (c3, "AWS", "Cloud"),
        (c4, "Sistemas de Informação", "Formação atual"),
    ]:
        with col:
            st.markdown(f'<div class="metric"><strong>{value}</strong><span>{label}</span></div>', unsafe_allow_html=True)

    title("O que eu faço", "Uma combinação entre desenvolvimento, dados, IA aplicada e pesquisa.")

    cols = st.columns(3)
    cards = [
        ("🤖 Inteligência Artificial",
         "Desenvolvimento de aplicações com LLMs, agentes de IA, RAG, Machine Learning e IA Generativa."),
        ("🧠 Pesquisa & Inovação",
         "Pesquisa aplicada em IA e computação quântica, com experimentação, testes e documentação técnica."),
        ("⚙️ Engenharia de Software",
         "Construção de aplicações web com Python, Streamlit, FastAPI, SQL, AWS e integração de dados."),
    ]
    for col, (h, p) in zip(cols, cards):
        with col:
            st.markdown(f'<div class="card"><h3>{h}</h3><p>{p}</p></div>', unsafe_allow_html=True)

    title("Destaques")
    st.markdown("""
    <div class="card">
        <h3>🚀 Dois projetos que representam meu trabalho</h3>
        <p>
            <b>Quantum Agents — Vibe Coding</b>: aplicação voltada à integração entre
            LLMs, agentes de IA e computação quântica para geração de circuitos a partir
            de linguagem natural.
        </p>
        <p>
            <b>Agentes IA Conversando</b>: sistema multiagente em que agentes especializados
            colaboram para analisar problemas, revisar hipóteses e sintetizar resultados.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ---------- COMPETÊNCIAS ----------
elif page == "Competências":
    title("Competências", "Tecnologias e áreas em que venho desenvolvendo experiência.")

    groups = [
        ("🤖 AI & Machine Learning",
         ["Python", "LangChain", "Groq", "LLMs", "Agentes de IA", "Machine Learning",
          "Data Mining", "IA Generativa", "Computação Quântica"]),
        ("🗄️ Data & Backend",
         ["SQL", "MySQL", "FastAPI", "Streamlit", "ETL", "Pentaho",
          "Modelagem de Dados", "Engenharia de Dados"]),
        ("☁️ Web & Cloud",
         ["Next.js", "AWS", "Cloud Computing", "Web Applications"]),
        ("🛠️ Developer Tools",
         ["Git", "Jupyter", "MySQL Workbench", "Automação de Processos", "Desenvolvimento Ágil"]),
    ]

    for i in range(0, len(groups), 2):
        cols = st.columns(2)
        for col, (h, items) in zip(cols, groups[i:i+2]):
            with col:
                st.markdown(
                    f'<div class="card"><h3>{h}</h3>{tech_tags(items)}</div>',
                    unsafe_allow_html=True
                )
        st.write("")

    title("Arquitetura de interesse")
    st.code("""
Usuário
   │
   ▼
Aplicação Web (Streamlit / Next.js)
   │
   ├──► LLM / API
   │       │
   │       ├──► Agentes especializados
   │       └──► RAG / conhecimento
   │
   ├──► Dados (SQL / MySQL / ETL)
   │
   └──► Cloud (AWS)
            │
            ▼
      Solução escalável
""", language="text")

# ---------- PROJETOS ----------
elif page == "Projetos":
    title("Projetos em destaque", "Aplicações práticas que unem IA, agentes, RAG e computação quântica.")

    st.markdown("""
    <div class="card">
        <h3>⚛️ Quantum Agents — Vibe Coding</h3>
        <p>
            Projeto relacionado à pesquisa aplicada em <b>LLMs + agentes de IA +
            computação quântica</b>. A proposta utiliza linguagem natural como
            interface para auxiliar a construção de circuitos quânticos,
            explorando o conceito de vibe coding.
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    st.link_button(
        "Abrir projeto no Streamlit →",
        "https://quantum-agents-vibe-coding.streamlit.app/",
        use_container_width=True,
    )

    st.write("")
    st.markdown("""
    <div class="card">
        <h3>🧪 Agentes IA Conversando — Agents Scientist</h3>
        <p>
            Sistema baseado em <b>multiagentes de IA</b>, no qual diferentes agentes
            possuem responsabilidades específicas e colaboram na resolução de
            problemas. O projeto explora geração de hipóteses, revisão, classificação,
            evolução, organização e síntese de resultados.
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    st.link_button(
        "Abrir projeto no Streamlit →",
        "https://agentesiaconversando.streamlit.app/agents_scientist",
        use_container_width=True,
    )

    title("Stack dos projetos")
    st.markdown(
        tech_tags(["Python", "Streamlit", "LLMs", "Agentes de IA", "RAG",
                   "Groq", "LangChain", "Computação Quântica"]),
        unsafe_allow_html=True
    )

# ---------- EXPERIÊNCIA ----------
elif page == "Experiência":
    title("Experiência & Pesquisa", "Projetos e experiências destacados no currículo.")

    st.markdown('<div class="timeline">', unsafe_allow_html=True)

    items = [
        ("Bolsista de Iniciação Científica — PIBIC/CNPq | UFRPE",
         "IA & Computação Quântica · Python · LLMs · Pesquisa Aplicada",
         "Desenvolvimento de soluções baseadas em IA e computação quântica voltadas à geração inteligente de código. Pesquisa, testes e documentação técnica."),
        ("Pesquisador Aplicado — Quantum Vibe Coding",
         "LLMs · Computação Quântica · Agentes de IA · Python",
         "Aplicação de LLMs na programação quântica e implementação de agentes de IA com RAG para geração de circuitos quânticos a partir de linguagem natural."),
        ("Desenvolvedor de Sistemas e IA — Projetos Autorais",
         "Python · AWS · Streamlit · MySQL · FastAPI · Next.js · Machine Learning",
         "Criação de sistemas web multiagentes com RAG, modelos de Machine Learning e Data Mining, além de aplicações Python/Streamlit conectadas a MySQL."),
    ]

    for h, role, p in items:
        st.markdown(
            f'<div class="timeline-item"><h3>{h}</h3>'
            f'<div class="role">{role}</div><p>{p}</p></div>',
            unsafe_allow_html=True
        )

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- FORMAÇÃO ----------
elif page == "Formação":
    title("Formação & Certificações")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class="card">
            <h3>🎓 Bacharelado em Sistemas de Informação</h3>
            <p><b>Universidade Federal Rural de Pernambuco — UFRPE</b></p>
            <p>Curso em andamento.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card">
            <h3>💻 Tecnólogo em ADS</h3>
            <p><b>Análise e Desenvolvimento de Sistemas</b></p>
            <p>Formação tecnológica em desenvolvimento de sistemas.</p>
        </div>
        """, unsafe_allow_html=True)

    title("Certificações")
    certs = [
        "AWS Academy Graduate — Cloud Foundations",
        "AWS Academy Graduate — Machine Learning Foundations",
        "AWS Academy Graduate — Cloud Web Application Builder",
        "Programa Ganhe o Mundo — Inglês",
    ]
    for cert in certs:
        st.markdown(f"- {cert}")

    title("Idiomas")
    st.markdown("""
    <div class="card">
        <p><b>🇧🇷 Português:</b> Nativo</p>
        <p><b>🇺🇸 Inglês:</b> Intermediário/Avançado</p>
        <p><b>🇪🇸 Espanhol:</b> Básico</p>
    </div>
    """, unsafe_allow_html=True)

# ---------- Footer ----------
st.markdown("""
<div class="footer">
    <p>Julio Vitor dos Santos · Recife, PE, Brasil · Disponível para oportunidades remotas</p>
    <p>Construído com Python + Streamlit</p>
</div>
""", unsafe_allow_html=True)
