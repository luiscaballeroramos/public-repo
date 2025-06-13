import install_private_packages

# Ya puedes importar lo que necesites del paquete
from private_module.core import private_function
from private_module2.core2 import private_function2

# Streamlit app
import streamlit as st

st.title("Usando paquete privado sin permisos root")
user_input = st.text_input("Introduce un valor para private_function:", value="5")

if st.button("Calcular"):
    try:
        input_value = int(user_input)
        st.success(f"Resultado de private_function: {private_function(input_value)}")
        st.success(
            f"Resultado de private_function2: {private_function2(float(input_value))}"
        )
    except Exception as e:
        st.error(f"Error: {e}")
