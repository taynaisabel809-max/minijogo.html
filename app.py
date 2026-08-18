import streamlit as st
import random

st.set_page_config(page_title="Gestão de Energia: Pomerode", layout="centered")

# Banco amplo com 15 perguntas diferentes sobre o cotidiano
banco_perguntas_total = [
    {
        "id": 1,
        "q": "Você acorda às 6h da manhã em um dia de inverno rigoroso em Pomerode. Como decide iniciar o aquecimento da casa?",
        "opcoes": [
            "Ativar o sistema de climatização em potência máxima em todos os cômodos.",
            "Utilizar roupas térmicas de lã e aquecer apenas o ambiente de uso comum.",
            "Abrir as janelas para a ventilação natural logo cedo, independentemente da temperatura."
        ],
        "pesos": [15.0, 5.0, 2.0]
    },
    {
        "id": 2,
        "q": "No final de semana, há uma grande quantidade de roupas para lavar. Qual é a sua escolha operacional?",
        "opcoes": [
            "Acionar a máquina de lavar roupas várias vezes com cargas parciais ao longo do dia.",
            "Esperar acumular o volume máximo recomendado para realizar um único ciclo completo.",
            "Lavar as roupas manualmente utilizando água quente em abundância."
        ],
        "pesos": [12.0, 4.0, 10.0]
    },
    {
        "id": 3,
        "q": "Durante o período noturno, como você gerencia a iluminação e os eletrônicos em sua residência?",
        "opcoes": [
            "Deixar lâmpadas e televisores ligados em cômodos vazios para manter o ambiente iluminado.",
            "Desligar os aparelhos da tomada em stand-by e iluminar apenas os espaços ocupados.",
            "Manter luzes decorativas externas acesas a noite inteira por segurança."
        ],
        "pesos": [9.0, 3.0, 8.0]
    },
    {
        "id": 4,
        "q": "No preparo das refeições diárias, qual prática você adota em relação aos eletrodomésticos?",
        "opcoes": [
            "Utilizar o forno elétrico e o micro-ondas simultaneamente sem planejamento prévio.",
            "Planejar o uso do fogão e dos eletrodomésticos de forma otimizada para evitar picos.",
            "Descongelar alimentos direto no micro-ondas por longos períodos em vez de antecipar o processo."
        ],
        "pesos": [11.0, 4.0, 7.0]
    },
    {
        "id": 5,
        "q": "Em relação à ventilação e refrigeração da casa nos dias quentes de verão, qual a sua decisão?",
        "opcoes": [
            "Manter o ar-condicionado ligado continuamente com portas e janelas abertas.",
            "Aproveitar a circulação cruzada de ar abrindo janelas estrategicamente e usar ventiladores econômicos.",
            "Deixar todos os ventiladores da casa girando no máximo mesmo sem ninguém no ambiente."
        ],
        "pesos": [14.0, 4.0, 8.0]
    },
    {
        "id": 6,
        "q": "Como você lida com o carregamento de dispositivos eletrônicos (celulares, notebooks) em casa?",
        "opcoes": [
            "Deixar os carregadores plugados na tomada permanentemente, mesmo sem aparelhos conectados.",
            "Conectar os aparelhos apenas durante o tempo necessário para a carga completa e retirar da tomada.",
            "Manter múltiplos dispositivos carregando simultaneamente durante toda a madrugada."
        ],
        "pesos": [5.0, 2.0, 8.0]
    },
    {
        "id": 7,
        "q": "No que diz respeito ao aquecimento de água para banho e uso doméstico, qual a sua conduta?",
        "opcoes": [
            "Optar por banhos longos com o chuveiro elétrico na potência máxima de temperatura.",
            "Controlar o tempo do banho e utilizar o chuveiro em modo econômico/moderado.",
            "Aquecer grandes volumes d'água excedentes por precaução sem necessidade real."
        ],
        "pesos": [16.0, 6.0, 9.0]
    },
    {
        "id": 8,
        "q": "Ao utilizar o ferro de passar roupas para o uniforme da semana, qual o procedimento adotado?",
        "opcoes": [
            "Ligar o ferro e passar cada peça separadamente ao longo da semana à medida que for usar.",
            "Acumular as peças e passar todas de uma só vez de forma organizada e contínua.",
            "Deixar o ferro ligado na tomada enquanto realiza outras tarefas domésticas demoradas."
        ],
        "pesos": [13.0, 4.0, 15.0]
    },
    {
        "id": 9,
        "q": "Como você gerencia o uso da geladeira e do freezer na sua rotina de armazenamento de alimentos?",
        "opcoes": [
            "Deixar a porta da geladeira aberta por tempo prolongado escolhendo o que vai consumir.",
            "Verificar rapidamente o que deseja antes de abrir, mantendo o tempo de abertura mínimo.",
            "Guardar alimentos ainda quentes diretamente no interior do refrigerador."
        ],
        "pesos": [10.0, 3.0, 11.0]
    },
    {
        "id": 10,
        "q": "Para a iluminação de áreas de estudo ou trabalho em casa durante o dia, qual sua escolha?",
        "opcoes": [
            "Manter as cortinas fechadas e acender todas as lâmpadas do teto e abajures.",
            "Aproveitar ao máximo a luz solar natural abrindo cortinas e janelas.",
            "Utilizar refletores de alta potência mesmo com boa claridade natural disponível."
        ],
        "pesos": [8.0, 2.0, 14.0]
    },
    {
        "id": 11,
        "q": "Em um dia ensolarado de primavera em Pomerode, como você decide secar as roupas lavadas?",
        "opcoes": [
            "Utilizar a secadora elétrica em ciclo completo independentemente do clima.",
            "Estender as roupas ao ar livre no varal aproveitando a energia solar e o vento natural.",
            "Utilizar o modo aquecido do ar-condicionado direcionado para as peças em um quarto fechado."
        ],
        "pesos": [14.0, 2.0, 12.0]
    },
    {
        "id": 12,
        "q": "Como você procede com os equipamentos de entretenimento (videogames, caixas de som, TVs) ao sair para a escola?",
        "opcoes": [
            "Deixar todos os aparelhos em modo de espera (stand-by) prontos para uso imediato.",
            "Desligar completamente os aparelhos do estabilizador ou da tomada.",
            "Manter sistemas de som conectados à rede elétrica sem reproduzir áudio."
        ],
        "pesos": [7.0, 2.0, 6.0]
    },
    {
        "id": 13,
        "q": "Na hora de ventilar a casa após a limpeza diária, qual método você prioriza?",
        "opcoes": [
            "Acionar exaustores elétricos e ventiladores simultaneamente com as portas fechadas.",
            "Promover a ventilação natural cruzada abrindo portas opostas da residência.",
            "Deixar ventiladores portáteis ligados nos cantos dos cômodos sem circulação externa."
        ],
        "pesos": [9.0, 3.0, 8.0]
    },
    {
        "id": 14,
        "q": "Como você escolhe o método de iluminação para corredores e áreas de circulação à noite?",
        "opcoes": [
            "Manter lâmpadas principais acesas em todos os corredores da casa por precaução.",
            "Utilizar iluminação pontual de baixa potência apenas nos locais de passagem imediata.",
            "Deixar luminárias de alto consumo acesas nos andares superiores sem circulação."
        ],
        "pesos": [8.0, 2.0, 11.0]
    },
    {
        "id": 15,
        "q": "Ao planejar o uso de computadores e notebooks para tarefas escolares, qual sua conduta energética?",
        "opcoes": [
            "Deixar o computador ligado com o monitor em brilho máximo durante longas pausas e intervalos.",
            "Configurar o modo de economia de energia e desligar o monitor nos momentos de ausência.",
            "Manter atualizações pesadas rodando em segundo plano durante o horário de pico de consumo."
        ],
        "pesos": [10.0, 3.0, 12.0]
    }
]

# Inicialização e Sorteio Randômico Único por Sessão
if "etapa" not in st.session_state:
    st.session_state.etapa = "questionario"
    st.session_state.consumo_questionario = 0.0
    st.session_state.producao = 25.0
    # Sorteia exatamente 5 perguntas diferentes do banco total de forma aleatória a cada início
    st.session_state.perguntas_jogo = random.sample(banco_perguntas_total, 5)
    st.session_state.indice_pergunta = 0

# --- ETAPA 1: QUESTIONÁRIO DINÂMICO E Às CEGAS ---
if st.session_state.etapa == "questionario":
    idx = st.session_state.indice_pergunta
    total_p = len(st.session_state.perguntas_jogo)
    
    st.title("⚡ Etapa 1: Diagnóstico de Consumo Cotidiano")
    st.progress((idx) / total_p)
    st.write(f"**Situação {idx + 1} de {total_p} (Perguntas Dinâmicas Exclusivas):**")
    
    pergunta_atual = st.session_state.perguntas_jogo[idx]
    st.info(pergunta_atual["q"])
    
    st.write("*(Nota: Escolha com base no seu bom senso. O impacto energético é computado de forma oculta pelo sistema).*")
    
    # Exibe as opções sem mostrar valores prévios
    escolha = st.radio("Selecione a sua decisão:", pergunta_atual["opcoes"], key=f"pergunta_dinamica_{idx}")
    
    if st.button("Confirmar Decisão e Avançar"):
        escolha_idx = pergunta_atual["opcoes"].index(escolha)
        gasto_oculto = pergunta_atual["pesos"][escolha_idx]
        st.session_state.consumo_questionario += gasto_oculto
        
        if idx + 1 < total_p:
            st.session_state.indice_pergunta += 1
            st.rerun()
        else:
            st.session_state.etapa = "minijogo"
            st.rerun()

# --- ETAPA 2: MINIJOGO DE POMERODE ---
elif st.session_state.etapa == "minijogo":
    st.title("🎮 Etapa 2: Missão Sustentável - Pomerode")
    st.write("Gerencie os recursos coletando elementos positivos e evitando a pegada excessiva de CO₂!")
    
    try:
        with open("minijogo.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=650, scrolling=False)
    except FileNotFoundError:
        st.error("⚠️ O arquivo 'minijogo.html' não foi encontrado. Verifique se o nome está correto no GitHub.")

    if st.button("📊 Finalizar Missão e Ver Saldo Energético Final"):
        st.session_state.etapa = "resultado"
        st.rerun()

# --- ETAPA 3: RELATÓRIO MATEMÁTICO E RESULTADOS ---
elif st.session_state.etapa == "resultado":
    st.title("📊 Relatório Final de Sustentabilidade")
    
    armazenamento_bateria = 20.0
    consumo_total = st.session_state.consumo_questionario
    
    saldo = st.session_state.producao + armazenamento_bateria - consumo_total
    
    st.write(f"**Energia Produzida (Eólica):** {st.session_state.producao} kWh")
    st.write(f"**Energia Armazenada (Bateria):** {armazenamento_bateria} kWh")
    st.write(f"**Energia Consumida Total (Decisões):** {consumo_total:.1f} kWh")
    st.write(f"### Saldo Energético Final: {saldo:.1f} kWh")
    
    st.warning("⚠️ **Nota Metodológica:** Os valores utilizados no sistema são modelos didáticos simplificados para representar o fluxo energético.")
    
    if saldo > 15:
        st.success("Resultado: Excedente Energético (Cidade altamente sustentável e equilibrada!)")
    elif saldo >= 0:
        st.info("Resultado: Equilíbrio Energético mantido com planejamento.")
    else:
        st.error("Resultado: Déficit Energético! O consumo excedeu a capacidade de suporte.")
        
    if st.button("🔄 Reiniciar Simulação Completa (Novas Perguntas Sorteadas)"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
