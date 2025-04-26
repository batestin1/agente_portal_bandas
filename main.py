import streamlit as st
import requests
import urllib.parse
from datetime import datetime
import os

# Função para chamar a API da Groq
def gerar_texto(prompt):
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GROQ_API_KEY}"
    }
    payload = {
        "model": "meta-llama/llama-4-scout-17b-16e-instruct",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.ok:
        return response.json()['choices'][0]['message']['content']
    else:
        return "Erro ao gerar resposta."

# Função para buscar link do YouTube
def buscar_youtube_link(query):
    if query and "Erro ao gerar resposta" not in query:
        query_encoded = urllib.parse.quote_plus(query)
        return f"https://www.youtube.com/results?search_query={query_encoded}"
    return None

# Função para buscar imagens no Google
def buscar_imagens_google(query):
    query_encoded = urllib.parse.quote_plus(query)
    return f"https://www.google.com/search?tbm=isch&q={query_encoded}"

# Função para gerar descrição da capa
def gerar_descricao_capa(banda):
    prompt_capa = f"Imagine uma capa de álbum para uma banda chamada {banda}, no estilo de rock alternativo ou grunge. Descreva em 2-3 linhas como seria essa capa."
    return gerar_texto(prompt_capa)

# Configuração Streamlit
st.set_page_config(page_title="Portal das Bandas", page_icon="🥁", layout="wide")

# Inicializa sessão
if "historico" not in st.session_state:
    st.session_state["historico"] = []
if "sessao_selecionada" not in st.session_state:
    st.session_state["sessao_selecionada"] = None

# Sidebar - Histórico
with st.sidebar:
    st.title("🥁 Portal das Bandas")
    st.write("Histórico de Explorações")
    if st.session_state["historico"]:
        for idx, sessao in enumerate(reversed(st.session_state["historico"])):
            label = f"{sessao['timestamp']} - {sessao['banda']}"
            if st.button(label, key=idx):
                # Seleciona o histórico sem criar novo
                st.session_state["sessao_selecionada"] = sessao
    else:
        st.info("Nenhuma exploração ainda.")
    st.markdown("---")
    st.caption("Feito com 💙 no ritmo do rock!")

# Área principal
st.title("🎶 Descubra Novos Sons")

if st.session_state["sessao_selecionada"]:
    sessao = st.session_state["sessao_selecionada"]

    # Mensagem de Opinião
    st.subheader(f"🎤 O que achei de {sessao['banda']}:")
    st.write(sessao["opiniao"])

    # Layout dos blocos com sombra e recolhíveis
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        with st.expander("🖼️ Fotos & Curiosidades"):
            st.markdown(f"[Veja imagens de {sessao['banda']}]({buscar_imagens_google(sessao['banda'])})")
            st.caption("Clique para ver imagens relacionadas no Google.")

    with col2:
        with st.expander("🌟 Bandas Similares"):
            st.write(sessao["sugestoes"])

    with col3:
        with st.expander("🎵 Playlist Indicada + Capa Fake"):
            st.markdown(f"**Capa do álbum:** {sessao['descricao_capa']}")
            st.markdown(f"[Veja imagens inspiradas nessa capa]({sessao['link_imagens']})")
            st.markdown("---")
            for musica, link in sessao["playlist"]:
                if link:
                    st.markdown(f"- [{musica}]({link})")
                else:
                    st.markdown(f"- {musica}")

    with col4:
        with st.expander("🚀 Nerdice Radical"):
            st.write(sessao["viagem"])

# Exibe histórico e impede a criação de nova sessão
if not st.session_state["sessao_selecionada"]:
    banda_favorita = st.text_input("Digite o nome de uma banda ou artista que você curte:")

    if banda_favorita:
        with st.spinner("Explorando novos sons... 🎶"):
            prompt_opiniao = f"Você gosta da banda {banda_favorita}? Responda em 2-3 linhas no estilo de um amigo roqueiro sincero."
            opiniao = gerar_texto(prompt_opiniao)

            prompt_similares = f"Baseado na banda {banda_favorita}, sugira 5 bandas similares, descreva o estilo de cada uma em 2 linhas."
            sugestoes = gerar_texto(prompt_similares)

            prompt_playlist = f"Crie uma playlist de 5 músicas, incluindo uma música do {banda_favorita} e músicas das bandas similares."
            playlist_raw = gerar_texto(prompt_playlist)

            prompt_extra = f"Se {banda_favorita} fosse um personagem da Marvel ou Star Wars, quem seria? Explique em poucas linhas."
            viagem_sonora = gerar_texto(prompt_extra)

            descricao_capa = gerar_descricao_capa(banda_favorita)

        # Trata a playlist
        playlist_itens = []
        if playlist_raw and "Erro ao gerar resposta" not in playlist_raw:
            for linha in playlist_raw.split('\n'):
                if linha.strip():
                    musica = linha.strip("- ").strip()
                    link = buscar_youtube_link(musica)
                    playlist_itens.append((musica, link))

        nova_sessao = {
            "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "banda": banda_favorita,
            "opiniao": opiniao,
            "sugestoes": sugestoes,
            "playlist": playlist_itens,
            "viagem": viagem_sonora,
            "descricao_capa": descricao_capa,
            "link_imagens": buscar_imagens_google(descricao_capa)
        }
        st.session_state["historico"].append(nova_sessao)
        st.session_state["sessao_selecionada"] = nova_sessao

# Estilo de sombra para os blocos (adicionado via markdown)
st.markdown("""
<style>
section[data-testid="stExpander"] > div > div {
    box-shadow: 0px 4px 10px rgba(0,0,0,0.15);
    border-radius: 10px;
    padding: 10px;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)
