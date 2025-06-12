import subprocess
import sys
import os
import site

LOCAL_PACKAGE_DIR = os.path.join(os.path.dirname(__file__), "external_packages")
os.makedirs(LOCAL_PACKAGE_DIR, exist_ok=True)

repo_url = "git+https://<TOKEN_PERSONAL>@github.com/luiscaballeroramos/private-repo.git#egg=private_module"

try:
    from private_module.core import private_function
except ImportError:
    subprocess.check_call([
        sys.executable, "-m", "pip", "install", "--target", LOCAL_PACKAGE_DIR, repo_url
    ])
    sys.path.append(LOCAL_PACKAGE_DIR)
    from private_module.core import private_function

# Ahora sí, usar Streamlit
import streamlit as st

st.title("Usando paquete privado sin permisos root")
st.write("Resultado de private_function():")
st.code(private_function())
