import os
import sys
import subprocess
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
token = os.getenv("GITHUB_TOKEN")
user = os.getenv("GITHUB_USER")

if not token or not user:
    raise EnvironmentError("Faltan GITHUB_TOKEN o GITHUB_USER en el archivo .env")

# Carpeta de instalación local
package_dir = os.path.join(os.path.dirname(__file__), "external_packages")
os.makedirs(package_dir, exist_ok=True)
sys.path.append(package_dir)


# Función reutilizable para asegurar que el módulo esté disponible
def ensure_private_package(module_name: str, repo_name: str):
    try:
        __import__(module_name)
    except ImportError:
        repo_url = (
            f"git+https://{token}@github.com/{user}/{repo_name}.git#egg={module_name}"
        )
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "--target", package_dir, repo_url]
        )
        __import__(module_name)


# Asegurar paquete privado (reutilizable)
ensure_private_package("private_module", "private-repo")

# Ya puedes importar lo que necesites del paquete
from private_module.core import private_function

# Streamlit app
import streamlit as st

st.title("Usando paquete privado sin permisos root")
st.write("Resultado de private_function(5):")
st.code(private_function(5))
