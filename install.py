import os
from dotenv import load_dotenv
import subprocess

load_dotenv()

token = os.getenv("GITHUB_TOKEN")
user = os.getenv("GITHUB_USER")
url = f"git+https://{token}@github.com/{user}/private-repo.git#egg=private_module"

subprocess.check_call(["pip", "install", "streamlit", "python-dotenv"])
subprocess.check_call(["pip", "install", url])
