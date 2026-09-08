import streamlit as st
from pathlib import Path
import urllib.parse

st.set_page_config(
    page_title="PeritOne | Peritagem Técnica de Edifícios e Obras",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"

GREEN = "#075B35"
GREEN_DARK = "#034326"
ORANGE = "#F57C00"
LIGHT = "#F5F8F6"
DARK = "#17352A"

SERVICES = [
    ("01", "Inspeção técnica para compradores de imóveis",
     "Avaliação independente do estado técnico do imóvel antes da compra, ajudando a identificar patologias, defeitos, anomalias e necessidades de intervenção."),
    ("02", "Inspeção técnica para vendedores de imóveis",
     "Conheça o estado técnico do imóvel antes de o colocar no mercado e identifique problemas que possam influenciar a negociação ou a futura venda."),
    ("03", "Inspeção para investidores estrangeiros",
     "Uma avaliação técnica independente para quem investe à distância e precisa de uma leitura objetiva do estado de um imóvel em Portugal."),
    ("04", "Auditoria técnica ampliada — Due Diligence Técnica Total",
     "Análise técnica aprofundada do edifício, com levantamento de anomalias, estado de conservação, riscos técnicos e necessidades previsíveis de intervenção."),
    ("05", "Inspeção para alojamento local",
     "Avaliação técnica do imóvel, identificação de patologias e problemas que possam afetar a utilização, conservação e valorização do alojamento."),
    ("06", "Inspeções estruturais e relatórios de memória futura",
     "Registo técnico e fotográfico do estado de elementos construtivos e estruturais, criando uma referência para futuras comparações e intervenções."),
    ("07", "Inspeção técnica e diagnóstico para condomínios",
     "Avaliação técnica de fachadas, coberturas, zonas comuns, estruturas e outros elementos do edifício, com identificação de patologias e recomendações."),
]

st.markdown(f"""
<style>
html, body, [class*="css"] {{ font-family: Arial, sans-serif; }}
.block-container {{ max-width: 1180px; padding-top: 1rem; }}
.hero {{
    background: linear-gradient(120deg, {GREEN_DARK} 0%, {GREEN} 62%, #0A6D43 100%);
    border-radius: 22px; padding: 48px 42px; color: white; margin-bottom: 28px;
}}
.hero h1 {{ font-size: clamp(2.2rem, 5vw, 4.4rem); line-height: .98; margin: 0 0 14px; }}
.hero h1 span {{ color: #FF8A00; }}
.hero p {{ font-size: 1.2rem; max-width: 720px; line-height: 1.55; }}
.badge {{ display:inline-block; padding:7px 13px; border-radius:999px;
         background:#ffffff18; border:1px solid #ffffff38; font-weight:700; }}
.section-title {{ color:{GREEN_DARK}; font-size:2rem; font-weight:800; margin: 26px 0 8px; }}
.section-lead {{ color:#50645B; font-size:1.05rem; line-height:1.6; }}
.card {{
    background:white; border:1px solid #DCE7E1; border-radius:16px;
    padding:22px; margin:8px 0; box-shadow:0 4px 16px rgba(0,0,0,.04);
}}
.num {{ color:{ORANGE}; font-size:1.8rem; font-weight:900; }}
.card h3 {{ color:{GREEN_DARK}; margin:4px 0 8px; font-size:1.18rem; }}
.card p {{ color:#52645C; line-height:1.55; margin:0; }}
.info {{
    background:{LIGHT}; border-left:5px solid {ORANGE}; padding:24px 26px;
    border-radius:12px; margin:18px 0;
}}
.area {{
    background:{GREEN_DARK}; color:white; border-radius:18px; padding:30px;
}}
.area h3 {{ color:white; margin-top:0; }}
.cta {{
    background:linear-gradient(120deg, {GREEN_DARK}, {GREEN});
    color:white; border-radius:20px; padding:34px; margin-top:28px;
}}
footer {{ color:#718078; text-align:center; padding:35px 0 10px; font-size:.9rem; }}
div.stButton > button {{
    border-radius: 999px; font-weight: 800; border: 0; padding: .65rem 1.1rem;
}}
</style>
""", unsafe_allow_html=True)

# Header
logo = ASSETS / "logo_transparente.png"
if logo.exists():
    st.image(str(logo), width=250)

st.markdown("""
<div class="hero">
  <div class="badge">ALGARVE • ALENTEJO • REGIÃO SUL DE PORTUGAL</div>
  <h1>Peritagem Técnica<br><span>de Edifícios e Obras</span></h1>
  <p><b>Mais do que uma vistoria, um diagnóstico que protege o seu património.</b><br>
  Avaliação técnica independente para imóveis existentes, obras em curso, compradores,
  vendedores, investidores e condomínios.</p>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("### 🔎 Diagnóstico")
    st.write("Identificação de patologias, anomalias e defeitos construtivos.")
with c2:
    st.markdown("### 📋 Relatório técnico")
    st.write("Registo claro e estruturado das observações e conclusões.")
with c3:
    st.markdown("### 🏗️ Obras em curso")
    st.write("Inspeções e registos técnicos durante a execução dos trabalhos.")

st.markdown('<div class="section-title">Os nossos serviços de Peritagem Técnica</div>', unsafe_allow_html=True)
st.markdown('<div class="section-lead">Escolha o tipo de inspeção que melhor corresponde à sua situação.</div>', unsafe_allow_html=True)

for num, title, desc in SERVICES:
    st.markdown(f"""
    <div class="card">
      <div class="num">{num}</div>
      <h3>{title}</h3>
      <p>{desc}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-title">Porquê contratar uma Peritagem Técnica?</div>', unsafe_allow_html=True)
st.markdown("""
<div class="info">
<b>Comprar, vender ou investir num imóvel é uma decisão importante.</b><br><br>
Uma peritagem técnica permite conhecer melhor o estado real de um edifício ou obra
e reduzir o risco de surpresas, custos inesperados e problemas que poderiam passar
despercebidos numa visita normal.
</div>
""", unsafe_allow_html=True)

cols = st.columns(2)
with cols[0]:
    st.markdown("#### O que pode ajudar a identificar?")
    for x in [
        "Patologias e defeitos de construção",
        "Fissuras, humidades e infiltrações",
        "Anomalias construtivas",
        "Sinais de degradação",
        "Necessidades de reparação ou intervenção",
    ]:
        st.write("✓ " + x)
with cols[1]:
    st.markdown("#### Em que decisões pode ajudar?")
    for x in [
        "Comprar um imóvel com maior segurança",
        "Vender com conhecimento do estado do imóvel",
        "Avaliar um investimento à distância",
        "Planear intervenções e manutenção",
        "Documentar o estado de uma obra ou edifício",
    ]:
        st.write("✓ " + x)

st.markdown('<div class="section-title">Edifícios existentes e obras em curso</div>', unsafe_allow_html=True)
st.markdown("""
<div class="info">
A PeritOne realiza peritagens técnicas não apenas a edifícios concluídos, mas também
a <b>obras em curso</b>. O acompanhamento e registo de determinadas fases da obra
pode ajudar a documentar o estado dos trabalhos, identificar anomalias de execução
e criar uma memória técnica para futuras decisões.
<br><br>
O serviço pode ser aplicado a moradias, apartamentos, edifícios multifamiliares,
condomínios, imóveis para investimento, alojamento local e outras construções.
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">Área de intervenção</div>', unsafe_allow_html=True)
st.markdown("""
<div class="area">
<h3>Algarve e Alentejo — Região Sul de Portugal</h3>
<p><b>Algarve:</b> cobertura regional.</p>
<p><b>Alentejo:</b> Évora • Beja • Moura • Sines</p>
<p>Para outras localizações, contacte-nos para verificar disponibilidade.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">Solicitar uma avaliação</div>', unsafe_allow_html=True)
st.write("Preencha os dados abaixo. O pedido pode ser encaminhado por email ou WhatsApp.")

with st.form("pedido_peritagem"):
    nome = st.text_input("Nome")
    telefone = st.text_input("Telefone")
    local = st.text_input("Localização do imóvel / obra")
    servico = st.selectbox("Serviço pretendido", [f"{n} — {t}" for n,t,_ in SERVICES])
    mensagem = st.text_area("Descreva brevemente o que pretende avaliar")
    enviado = st.form_submit_button("Preparar pedido")

if enviado:
    resumo = f"""Pedido de Peritagem Técnica — PeritOne

Nome: {nome}
Telefone: {telefone}
Localização: {local}
Serviço: {servico}

Descrição:
{mensagem}
"""
    encoded = urllib.parse.quote(resumo)
    whatsapp = "351926257154"
    wa_url = f"https://wa.me/{whatsapp}?text={encoded}"
    mail_url = f"mailto:GeralFiscalia@proton.me?subject={urllib.parse.quote('Pedido de Peritagem Técnica — PeritOne')}&body={encoded}"

    st.success("Pedido preparado. Escolha como pretende enviá-lo:")
    a, b = st.columns(2)
    with a:
        st.link_button("Enviar por WhatsApp", wa_url, use_container_width=True)
    with b:
        st.link_button("Enviar por email", mail_url, use_container_width=True)

st.markdown("""
<div class="cta">
<h2>O seu edifício em boas mãos.</h2>
<p>Uma avaliação técnica pode fazer a diferença antes de comprar, vender,
investir ou avançar com uma intervenção.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("### Páginas legais")
legal_cols = st.columns(3)
with legal_cols[0]:
    st.page_link("pages/1_Politica_de_Privacidade.py", label="Política de Privacidade")
with legal_cols[1]:
    st.page_link("pages/2_Politica_de_Cookies.py", label="Política de Cookies")
with legal_cols[2]:
    st.page_link("pages/3_Termos_e_Condicoes.py", label="Termos e Condições")

st.markdown("""
<footer>
PeritOne — Peritagem Técnica de Edifícios e Obras<br>
Algarve e Alentejo • Região Sul de Portugal
</footer>
""", unsafe_allow_html=True)
