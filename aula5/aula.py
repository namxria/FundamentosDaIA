import streamlit as st

st.title("My ChatBot AI")
with st.sidebar:

    st.markdown("##  Configurações")
    st.markdown("---")

    groq_key = st.text_input(
        "Groq API Key",
        type="password",
        placeholder="gsk_...",
        help="Crie sua chave em console.groq.com/keys"
    )
