import install_private_packages

# Ya puedes importar lo que necesites del paquete
from private_module.core import private_function

# Streamlit app
import streamlit as st

st.title("Usando paquete privado sin permisos root")
user_input = st.text_input("Introduce un valor para private_function:", value="5")

if st.button("Calcular"):
    try:
        input_value = int(user_input)
        result = private_function(input_value)
        st.success(f"Resultado: {result}")
    except Exception as e:
        st.error(f"Error: {e}")
