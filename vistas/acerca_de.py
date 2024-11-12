import streamlit as  st
from forms.contacto import contact_form
@st.dialog("contacto") 
def ver_form_contacto():
    contact_form()


c1, c2 = st.columns(2, gap="small", vertical_alignment="center")

with c1: 
    st.image("img/fotoJu.jpg", width=230)
with c2: 
    st.title("Julissa Julieth Alvarez Suárez.")
    st.write("Analista de datos senior, que ayuda a las empresas apoyando la toma de decisiones basada en datos. Como Ciencia de Datos.")

if st.button("Contacto"):
    ver_form_contacto()

st.subheader("Experiencias y Calificaciones", anchor= False)
st.write(
        """ 
        - 7 años de experiencia extrayendo información útil a partir de datos.
        - Fuerte experiencia práctica y conocimiento en Python y Excel.
        - Buen conocimiento de los principios estadísticos y sus respectivas aplicaciones.
        - Excelente jugador de equipo y con un fuerte sentido de iniciativa en las tareas.

        """
        )

st.subheader("Habilidades", anchor= False)
st.write(
        """ 
        - 7 años de experiencia extrayendo información útil a partir de datos.
        - Fuerte experiencia práctica y conocimiento en Python y Excel.
        - Buen conocimiento de los principios estadísticos y sus respectivas aplicaciones.
        - Excelente jugador de equipo y con un fuerte sentido de iniciativa en las tareas.

        """
        )
