import streamlit as st
import streamlit.components.v1 as components

# Configuração da página para o jogo ficar largo e bonito
st.set_page_config(page_title="Nosso Slope Romântico 💚", layout="wide")

st.title("🎮 Slope do Nosso Amor")
st.write("Jogue e descubra uma mensagem especial no final!")

# Criando duas colunas: uma para o jogo e outra para a surpresa
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Clique na tela e use as setas do teclado para jogar:")
    # Link de um clone idêntico e funcional do Slope 3D
    slope_url = "https://github.io"
    components.iframe(slope_url, height=600, scrolling=False)

with col2:
    st.subheader("🏆 Sua Pontuação")
    
    # Campo para você ou seu namorado digitarem o score que tiraram no jogo
    score = st.number_input("Digite os pontos que fez ao morrer:", min_value=0, step=1, value=0)
    
    st.divider()
    
    # Sistema inteligente que escolhe a foto e o texto com base nas suas faixas
    if 0 <= score <= 10:
        st.image("https://i.postimg.cc/4xLgJsXS/1.jpg", caption="Nossa primeira foto") # COLOQUE O LINK DA FOTO 1
        st.subheader("❤️ De 0 a 10 pontos:")
        st.write("Escreva aqui o seu primeiro texto romântico para quando o score for baixo...") # COLOQUE SEU TEXTO 1

    elif 11 <= score <= 20:
        st.image("https://i.postimg.cc/sf9bjsc1/2.jpg", caption="Nossa segunda foto") # COLOQUE O LINK DA FOTO 2
        st.subheader("❤️ De 11 a 20 pontos:")
        st.write("Escreva aqui o seu segundo texto romântico...") # COLOQUE SEU TEXTO 2

    elif 21 <= score <= 30:
        st.image("https://i.postimg.cc/Hs6KMzFC/3.jpg", caption="Nossa terceira foto") # COLOQUE O LINK DA FOTO 3
        st.subheader("❤️ De 21 a 30 pontos:")
        st.write("Escreva aqui o seu terceiro texto romântico...") # COLOQUE SEU TEXTO 3

    elif 31 <= score <= 40:
        st.image("https://i.postimg.cc/7ZcWs6Hq/4.jpg", caption="Nossa quarta foto") # COLOQUE O LINK DA FOTO 4
        st.subheader("❤️ De 31 a 40 pontos:")
        st.write("Escreva aqui o seu quarto texto romântico...") # COLOQUE SEU TEXTO 4

    elif 41 <= score <= 50:
        st.image("https://i.postimg.cc/9MHN2nwv/5.jpg", caption="Nossa quinta foto") # COLOQUE O LINK DA FOTO 5
        st.subheader("❤️ De 41 a 50 pontos:")
        st.write("Escreva aqui o seu quinto texto romântico...") # COLOQUE SEU TEXTO 5

    elif 51 <= score <= 70:
        st.image("https://i.postimg.cc/6601szWg/6.jpg", caption="Nossa sexta foto") # COLOQUE O LINK DA FOTO 6
        st.subheader("❤️ De 51 a 70 pontos:")
        st.write("Escreva aqui o seu sexto texto romântico...") # COLOQUE SEU TEXTO 6

    elif score >= 71:
        st.image("https://i.postimg.cc/8CMtZmXJ/7.jpg", caption="Nossa foto especial") # COLOQUE O LINK DA FOTO 7
        st.subheader("👑 Acima de 71 pontos - Você é incrível!")
        st.write("Escreva aqui o texto mais romântico de todos para a pontuação máxima!") # COLOQUE SEU TEXTO 7
