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

    # Añadir el directorio site-packages al path
    from site import getsitepackages, getusersitepackages
    sys.path.extend(getsitepackages())
    sys.path.append(getusersitepackages())

    # Importar de nuevo usando importlib
    private_module = importlib.import_module("private_module.core")
    private_function = private_module.private_function
