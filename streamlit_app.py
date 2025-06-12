import subprocess
import sys
import os
import importlib

# Configuración
token = os.getenv("GITHUB_TOKEN") or "ghp_xxx..."  # Usa tu token o variable de entorno
user = os.getenv("GITHUB_USER")
repo_url = f"git+https://{token}@github.com/{user}/private-repo.git#egg=private_module"

try:
    # Intentar importar directamente
    from private_module.core import private_function
except ImportError:
    # Instalar y recargar importación si falla
    subprocess.check_call([sys.executable, "-m", "pip", "install", repo_url])
# Asegurar que el path del site-packages del venv esté incluido
    for path in site.getsitepackages():
        if path not in sys.path:
            sys.path.append(path)

    # Intentar importar de nuevo
    from private_module.core import private_function


# Código de Streamlit
import streamlit as st

st.title("Ejemplo usando un paquete privado")
st.write("Resultado de `private_function()`:")
st.code(private_function())
