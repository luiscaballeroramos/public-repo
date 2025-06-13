import os
import sys
import subprocess
from dotenv import load_dotenv

TOKENS = {"private-repo": ("GITHUB_TOKEN", "GITHUB_USER")}
PACKAGES_MODULES = {"private-repo": ["private_module", "private_module2"]}
# Cargar variables de entorno
load_dotenv()

# Carpeta de instalación local
package_dir = os.path.join(os.path.dirname(__file__), "external_packages")
os.makedirs(package_dir, exist_ok=True)
sys.path.append(package_dir)


# Función reutilizable para asegurar que el módulo esté disponible
def ensure_private_package(module_name: str, repo_name: str):
    token = os.getenv(TOKENS[repo_name][0])
    user = os.getenv(TOKENS[repo_name][1])
    if not token or not user:
        raise EnvironmentError("Faltan GITHUB_TOKEN o GITHUB_USER en el archivo .env")
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
for repo, modules in PACKAGES_MODULES.items():
    for module in modules:
        ensure_private_package(module, repo)
