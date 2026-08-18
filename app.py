import streamlit as st
import streamlit.components.v1 as components
import random

st.set_page_config(page_title="Gestão de Energia: Pomerode", layout="centered")

# Banco de 15 perguntas divididas internamente em níveis (Fácil, Média, Reflexiva, Complexa, Hard)
# sem mostrar nenhum rótulo para o usuário.
banco_niveis = {
    "facil": [
        {
            "id": 1,
            "q": "Ao sair para a escola em uma manhã ensolarada em Pomerode, qual a atitude mais adequada com as luzes dos cômodos vazios?",
            "opcoes": [
                "Deixar as lâmpadas acesas para que a casa não fique totalmente escura.",
                "Desligar todas as luzes dos cômodos que não estão sendo ocupados.",
                "Manter apenas a luz da sala ligada por segurança."
            ],
            "pesos": [8.0, 2.0, 6.0]
        },
        {
            "id": 2,
            "q": "No dia a dia, como você costuma carregar o seu celular em casa?",
            "opcoes": [
                "Deixar o carregador plugado na tomada o dia todo, mesmo sem o celular conectado.",
                "Conectar o aparelho apenas pelo tempo necessário e retirar o carregador da tomada.",
                "Colocar para carregar apenas quando for dormir e deixar a noite inteira."
            ],
            "pesos": [5.0, 2.0, 7.0]
        },
        {
            "id": 3,
            "q": "Para ventilar um quarto numa tarde quente de verão, qual opção você escolhe?",
            "opcoes": [
                "Ligar o ventilador no máximo e fechar totalmente as cortinas e janelas.",
                "Abrir a janela para aproveitar a circulação natural do ar e usar o ventilador de forma moderada.",
                "Deixar o ar-condicionado e o ventilador ligados ao mesmo tempo."
            ],
            "pesos": [9.0, 3.0, 14.0]
        }
    ],
    "media": [
        {
            "id": 4,
            "q": "No final de semana, há uma quantidade moderada de roupas acumuladas para lavar. O que você faz?",
            "opcoes": [
                "Ligar a máquina de lavar várias vezes ao longo do dia com pouca roupa.",
                "Esperar juntar a carga completa recomendada pelo fabricante para fazer um único ciclo.",
                "Lavar à mão utilizando água quente em grande volume."
            ],
            "pesos": [12.0, 4.0, 10.0]
        },
        {
            "id": 5,
            "q": "Como você gerencia a abertura da geladeira na hora de preparar um lanche rápido?",
            "opcoes": [
                "Deixar a porta aberta por vários segundos enquanto decide o que vai pegar.",
                "Verificar rapidamente o que deseja antes de abrir, mantendo o tempo de abertura mínimo.",
                "Guardar alimentos ainda quentes diretamente nas prateleiras internas."
            ],
            "pesos": [10.0, 3.0, 11.0]
        },
        {
            "id": 6,
            "q": "Para realizar as tarefas escolares no computador durante a tarde, qual a sua escolha de iluminação?",
            "opcoes": [
                "Manter as cortinas fechadas e acender todas as luminárias do teto.",
                "Aproveitar ao máximo a luz solar natural posicionando a mesa perto da janela.",
                "Utilizar lâmpadas de alta potência mesmo com boa claridade natural."
            ],
            "pesos": [8.0, 2.0, 13.0]
        }
    ],
    "reflexiva": [
        {
            "id": 7,
            "q": "Em um dia frio de inverno em Pomerode, qual a melhor forma de iniciar o aquecimento do ambiente de convivência?",
            "opcoes": [
                "Ativar o sistema de climatização em potência máxima em todos os cômodos da casa.",
                "Utilizar roupas térmicas adequadas e aquecer de forma concentrada apenas o espaço de uso comum.",
                "Abrir as janelas de manhã cedo para renovar o ar, ignorando o frio externo."
            ],
            "pesos": [15.0, 5.0, 3.0]
        },
        {
            "id": 8,
            "q": "Ao utilizar o ferro elétrico para passar o uniforme da semana, qual rotina otimiza o consumo?",
            "opcoes": [
                "Ligar o ferro e passar cada peça separadamente nos dias em que for usar.",
                "Acumular as peças e passar todas de uma só vez em um fluxo contínuo e organizado.",
                "Deixar o ferro ligado na tomada enquanto faz outras pausas longas pela casa."
            ],
            "pesos": [13.0, 4.0, 16.0]
        },
        {
            "id": 9,
            "q": "Como proceder com os aparelhos de entretenimento (videogame, TV, som) ao sair para passar o dia fora?",
            "opcoes": [
                "Deixar todos em modo de espera (stand-by) para ligarem mais rápido na volta.",
                "Desligar completamente os aparelhos da tomada ou do filtro de linha.",
                "Manter caixas de som conectadas à rede elétrica sem reproduzir áudio."
            ],
            "pesos": [7.0, 2.0, 6.0]
        }
    ],
    "complexa": [
        {
            "id": 10,
            "q": "No preparo das refeições principais da família, como você planeja o uso simultâneo de eletrodomésticos de alto consumo?",
            "opcoes": [
                "Utilizar o forno elétrico e o micro-ondas ao mesmo tempo sem planejamento prévio de carga.",
                "Organizar os horários de preparo para evitar picos excessivos na rede elétrica.",
                "Descongelar alimentos direto no micro-ondas por ciclos longos repetidos."
            ],
            "pesos": [14.0, 4.0, 9.0]
        },
        {
            "id": 11,
            "q": "Em um dia ensolarado e seco de primavera na região, qual o método ideal para secar as roupas recém-lavadas?",
            "opcoes": [
                "Utilizar a secadora elétrica em ciclo completo por comodidade.",
                "Estender as peças ao ar livre no varal, aproveitando a energia solar e o vento natural.",
                "Utilizar o modo aquecido do ar-condicionado direcionado para as roupas em um cômodo fechado."
            ],
            "pesos": [14.0, 2.0, 12.0]
        },
        {
            "id": 12,
            "q": "Como você escolhe a iluminação para corredores e áreas de circulação interna durante a noite?",
            "opcoes": [
                "Manter lâmpadas principais de teto acesas em todos os corredores por precaução.",
                "Utilizar balizamento ou iluminação pontual de baixa potência apenas nos locais de passagem.",
                "Deixar luminárias decorativas de alto consumo acesas nos andares superiores sem uso."
            ],
            "pesos": [9.0, 2.0, 11.0]
        }
    ],
    "hard": [
        {
            "id": 13,
            "q": "Considerando o perfil climático de Pomerode e a eficiência energética residencial, qual conduta reflete melhor um planejamento sustentável de longo prazo?",
            "opcoes": [
                "Priorizar materiais construtivos e isolamento térmico passivo, reduzindo a dependência de climatizadores artificiais.",
                "Manter sistemas de refrigeração e aquecimento ligados ininterruptamente para estabilizar a temperatura interna exata.",
                "Substituir toda a ventilação natural por exaustores mecânicos automatizados contínuos."
            ],
            "pesos": [2.0, 16.0, 12.0]
        },
        {
            "id": 14,
            "q": "Ao avaliar o impacto indireto de atualizações pesadas de softwares em computadores durante horários de pico, qual decisão minimiza a sobrecarga na matriz?",
            "opcoes": [
                "Programar downloads e processos intensivos para períodos de menor demanda energética na rede.",
                "Deixar atualizações automáticas rodando em segundo plano durante o horário de pico comercial.",
                "Manter o computador com o monitor em brilho máximo durante longas ausências."
            ],
            "pesos": [3.0, 12.0, 10.0]
        },
        {
            "id": 15,
            "q": "No contexto de uma comunidade urbana sustentável, qual é a métrica mais crítica para equilibrar a microgeração eólica local com o consumo residencial?",
            "opcoes": [
                "Sincronizar os hábitos de alto gasto com os picos reais de geração e armazenamento em bateria, evitando o déficit.",
                "Desconsiderar a capacidade da bateria e focar apenas no conforto imediato individual.",
                "Aumentar o consumo base fixo para forçar a concessionária a expandir a rede."
            ],
            "pesos": [4.0, 15.0, 11.0]
        }
    ]
}

# Inicialização e Sorteio Garantindo 1 Pergunta de Cada Nível (Total de 5, sem repetir)
if "etapa" not in st.session_state:
    st.session_state.etapa = "questionario"
    st.session_state.consumo_questionario = 0.0
    st.session_state.producao = 25.0
    
    # Sorteia exatamente uma de cada categoria para garantir diversidade e níveis ocultos
    perguntas_sorteadas = [
        random.choice(banco_niveis["facil"]),
        random.choice(banco_niveis["media"]),
        random.choice(banco_niveis["reflexiva"]),
        random.choice(banco_niveis["complexa"]),
        random.choice(banco_niveis["hard"])
    ]
    # Embaralha a ordem para que o nível não siga uma sequência previsível
    random.shuffle(perguntas_sorteadas)
    
    st.session_state.perguntas_jogo = perguntas_sorteadas
    st.session_state.indice_pergunta = 0

# --- ETAPA 1: QUESTIONÁRIO DINÂMICO E ÀS CEGAS ---
if st.session_state.etapa == "questionario":
    idx = st.session_state.indice_pergunta
    total_p = len(st.session_state.perguntas_jogo)
    
    st.title("⚡ Etapa 1: Diagnóstico de Consumo Cotidiano")
    st.progress((idx) / total_p)
    st.write(f"**Situação {idx + 1} de {total_p} (Análise Estratégica):**")
    
    pergunta_atual = st.session_state.perguntas_jogo[idx]
    st.info(pergunta_atual["q"])
    
    st.write("*(Nota: Escolha com base no seu bom senso. O impacto energético é computado de forma oculta).*")
    
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
        components.html(html_content, height=680, scrolling=False)
    except FileNotFoundError:
        st.error("⚠️ O arquivo 'minijogo.html' não foi encontrado. Verifique se o nome está exato no GitHub.")

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
    st.write(f"**Energia Consumida Total (Decisões + Jogo):** {consumo_total:.1f} kWh")
    st.write(f"### Saldo Energético Final: {saldo:.1f} kWh")
    
    st.warning("⚠️ **Nota Metodológica:** Os valores utilizados no sistema integram o diagnóstico comportamental com o desempenho urbano na simulação.")
    
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
