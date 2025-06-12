import os
import subprocess
import streamlit as st

# Leer token y usuario desde los secretos
token = st.secrets["GITHUB_TOKEN"]
user = st.secrets["GITHUB_USER"]
repo_url = f"git+https://{token}@github.com/{user}/private-repo.git#egg=private_module"

# Intentar importar, si falla, instalar e importar
try:
    from private_module.core import private_function
except ImportError:
    subprocess.check_call(["pip", "install", repo_url])
    from private_module.core import private_function

# UI Streamlit
st.title("🔐 App con módulo privado")

valor = st.number_input("Introduce un número:", value=1)
if st.button("Ejecutar función privada"):
    resultado = private_function(valor)
    st.success(f"Resultado: {resultado}")
