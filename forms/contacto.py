import re
import streamlit as st
import time


def is_valid_email(email):
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(email_pattern, email) is not None

#
def contact_form():
        with st.form("contact_form"):
                email = st.text_input("Correo electrónico:", placeholder="email@gmail.com")
                name = st.text_input("Nombre:", placeholder="Escriba su nombre")
                message = st.text_area("Mensaje:")
                submit_button = st.form_submit_button("Enviar")

        if submit_button:
                if not name:
                        st.error("Por favor escriba su nombre", icon="🧑")
                        st.stop()
                if not is_valid_email(email):
                        st.error("Por favor su dirección de correo electrónico no es correcto.", icon="📧")
                        st.stop()
                if not email:
                        st.error("Su dirección de correo electrónico no es correcta",   icon="📨")
                        st.stop()
                if not message:
                        st.error("Por favor escriba un mensaje", icon="💬")
                        st.stop()
                if submit_button:
                        st.success("Se envió sastisfactoriamente")
                        time.sleep(2)
                        st.rerun()

