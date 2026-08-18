import streamlit as st
import streamlit.components.v1 as components
import random

st.set_page_config(page_title="Gestão de Energia: Pomerode", layout="centered")

# Lista de perguntas aleatórias sobre o cotidiano da cidade
perguntas = [
    {"q": "Dia frio em Pomerode: Ligar aquecedor ao máximo ou usar uma blusa de lã?", "custo": 12},
    {"q": "Lavagem de roupas: Acionar a máquina com carga parcial ou aguardar acumular?", "custo": 8},
    {"q": "Iluminação da casa: Deixar lâmpadas acesas nos cômodos vazios ou apagar?", "custo": 3},
    {"q": "Uso de eletrodomésticos no pico de energia: Evitar ou usar tudo junto?", "custo": 10}
]

# Inicializa o estado do jogo
if "etapa" not in st.session_state:
    st.session_state.etapa = "questionario"
    st.session_state.consumo = 0.0
    st.session_state.producao = 20.0
    st.session_state.pergunta_atual = random.choice(perguntas)

# --- ETAPA 1: O QUESTIONÁRIO DINÂMICO ---
if st.session_state.etapa == "questionario":
    st.title("⚡ Etapa 1: Diagnóstico de Consumo - Pomerode")
    st.write(f"**Situação:** {st.session_state.pergunta_atual['q']}")
    
    col1, col2 = st.columns(2)
    
    if col1.button("Opção Consciente (Baixo Gasto)"):
        st.session_state.consumo += 3.0
        st.session_state.etapa = "minijogo"
        st.rerun()
        
    if col2.button("Opção Desperdiçadora (Alto Gasto)"):
        st.session_state.consumo += st.session_state.pergunta_atual['custo']
        st.session_state.etapa = "minijogo"
        st.rerun()

# --- ETAPA 2: O MINIJOGO DE POMERODE (LENDO O HTML QUE VOCÊ SALVOU) ---
elif st.session_state.etapa == "minijogo":
    st.title("🎮 Etapa 2: Missão Sustentável")
    st.write("Jogue abaixo para coletar energia limpa e equilibrar o CO₂ da cidade!")
    
    # Puxa automaticamente o arquivo minijogo.html que você acabou de criar
    try:
        with open("minijogo.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=620, scrolling=False)
    except FileNotFoundError:
        st.error("⚠️ O arquivo 'minijogo.html' não foi encontrado na mesma pasta. Certifique-se de que o nome está exato.")

    if st.button("📊 Finalizar e Ver Relatório Final"):
        st.session_state.etapa = "resultado"
        st.rerun()

# --- ETAPA 3: RELATÓRIO MATEMÁTICO FINAL ---
elif st.session_state.etapa == "resultado":
    st.title("📊 Relatório Final de Sustentabilidade")
    
    # Fórmula exigida pelo professor: Saldo = Produção + Armazenamento - Consumo
    armazenamento = 15.0
    saldo = st.session_state.producao + armazenamento - st.session_state.consumo
    
    st.write(f"**Energia Produzida (Eólica):** {st.session_state.producao} kWh")
    st.write(f"**Energia Armazenada (Bateria):** {armazenamento} kWh")
    st.write(f"**Energia Consumida (Decisões):** {st.session_state.consumo:.1f} kWh")
    st.write(f"### Saldo Energético Final: {saldo:.1f} kWh")
    
    st.warning("⚠️ **Nota Metodológica:** Os valores utilizados no sistema são didáticos e servem para representar o fluxo energético de forma simplificada.")
    
    if saldo >= 10:
        st.success("Resultado: Excedente / Cidade Sustentável com ótimo desempenho!")
    elif saldo >= 0:
        st.info("Resultado: Equilíbrio Energético mantido.")
    else:
        st.error("Resultado: Déficit energético! O consumo ultrapassou a capacidade.")
        
    if st.button("🔄 Reiniciar Simulação"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
