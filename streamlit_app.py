import subprocess
import sys
import os

# import site
from dotenv import load_dotenv

load_dotenv()

# token = os.getenv("GITHUB_TOKEN")
# user = os.getenv("GITHUB_USER")
# if not token or not user:
#     raise EnvironmentError("Faltan GITHUB_TOKEN o GITHUB_USER en el archivo .env")

# repo_url = f"git+https://{token}@github.com/{user}/private-repo.git#egg=private_module"
# LOCAL_PACKAGE_DIR = os.path.join(os.path.dirname(__file__), "external_packages")
# os.makedirs(LOCAL_PACKAGE_DIR, exist_ok=True)

# try:
#     from private_module.core import private_function
# except ImportError:
#     subprocess.check_call(
#         [
#             sys.executable,
#             "-m",
#             "pip",
#             "install",
#             "--target",
#             LOCAL_PACKAGE_DIR,
#             repo_url,
#         ]
#     )
#     sys.path.append(LOCAL_PACKAGE_DIR)
#     from private_module.core import private_function
from private_module.core import private_function

# Ahora sí, usar Streamlit
import streamlit as st

st.title("Usando paquete privado sin permisos root")
st.write("Resultado de private_function():")
st.code(private_function(5))
