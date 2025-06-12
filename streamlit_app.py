import os
import subprocess

# Leer secretos
token = os.getenv("GITHUB_TOKEN")
user = os.getenv("GITHUB_USER")

# Instalar el paquete privado si no está ya instalado
repo_url = f"git+https://{token}@github.com/{user}/private-repo.git#egg=private_module"
try:
    import private_module
except ImportError:
    subprocess.check_call(["pip", "install", repo_url])
    import private_module


import streamlit as st
from private_module.private_module import private_function

st.title("🔐 Streamlit + Código Privado")

valor = st.number_input("Introduce un número:", value=1)
if st.button("Ejecutar función privada"):
    resultado = private_function(valor)
    st.success(f"Resultado: {resultado}")
