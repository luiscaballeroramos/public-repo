import os
from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import install
from private_module.private_module import private_function

st.title("🔐 Streamlit + Código Privado")

valor = st.number_input("Introduce un número:", value=1)
if st.button("Ejecutar función privada"):
    resultado = private_function(valor)
    st.success(f"Resultado: {resultado}")
