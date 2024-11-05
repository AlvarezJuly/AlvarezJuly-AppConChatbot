import json

import streamlit as  st

from streamlit_lottie import st_lottie

def get(path: str):
    with open(path, "r") as p:
        return json.load(p)

#Inicio de pagina
with st.container():
    st.subheader("Bienvenidos, Somos SOFTIA👋😊")
    st.title("Creamos soluciones para acelerar tu negocio")
    st.write(
        "Somos unos apasionados de las tenologías y la innovación, especialización en el sector de la digitalización y automatización de negocios. Nos gusta crear soluciones para resolver problemas y mejorar procesos. "
    )
    st.write("[Saber más>](https://streamlit.io/)"
    )

#Sobre nosostros
with st.container():
    st.write("---")

    texto_columna, imagen_columna = st.columns((1,2))
    with texto_columna:
        st.subheader("Sobre nosotros 🔍⭐⭐")
        st.write(
            """
            Nuestro objetivo es poder aportar valor a los negocios ayudandoles a ahorrar tiempo y dinero a través de la implantación de nuevas tecnologías como la inteligencia artifical, analisis de datos o implantación de software de automatización.

Seguramente te vamos a poder ayudar si:

-Tienes un negocio y quieres mejorar tus procesos de trabajo para ahorrar tiempo y dinero Tienes trabajadores que emplean parte de su jornada a realizar tareas repetitivas sin valor añadido

para tu negocio

No tienes claras las métricas de tu negocio y quieres tomar decisiones basadas en datos

-Quieres mejorar la experiencia de tus clientes

Usas herramientas de software antiguas o poco eficientes o procesos en los que usas papel y boligrafo

***Si esto suena interesante para ti puedes contactarnos a través del formulario que encontrarás al final de la página***
    
    """
    )
    with imagen_columna:
        st.image("img/desarrolloApp.png")
    

#Servicios

with st.container():
    st.write("---")
    st.header("Servicios 👩‍💻👨‍💻")


    texto_columna, imagen_columna = st.columns((1,2))


with texto_columna:
    st.subheader("Diseño de aplicaciones")

    st.write(
        """
        Si en tus procesos diarios tienes que introducir información en diferentes fuentes de datos o bien tienes que 
        trabajar con documentación en papel, es hora de pensar en implementar una aplicación en tu negocio para potenciar y optimizar el funcionamiento de los procesos diarias
        """
    )
    st.write("[Ver servicios >](https://streamlit.io/)")
    
    with imagen_columna: 
        path = get("gift/hombreDev.json") 
        st_lottie (path) 
    #st.image("img/devimag.png")


#parte de contacto

st.subheader("Contacto")

form = st.form(key="home", clear_on_submit=True)
with form:
    input_name = st.text_input("Name:", placeholder="Escriba su nombre")
    input_email = st.text_input("Email:", placeholder="Escriba su correo electrónico")
    input_area = st.text_area("Comentario:")
    button_submit= form.form_submit_button("Enviar")

#Footer 
with st.container():
    st.write("---")
    p1, p2, p3 = st.columns((3))
    with p1:
        st.subheader("Contatos")
        st.write("***Dirección:*** Juigalpa, Chontales-Nicaragua")
        st.write("***Teléfono:*** +(505) 5784-5840")
    with p2:
        st.subheader("Servicios")
        st.write("Diseños de Aplicaciones")
        st.write("Automatización de procesos")
        st.write("visualización de datos")
    with p3:
        st.subheader("Redes sociales")
        st.markdown("[YOUTUBE](https://youtube.com/)")
        st.markdown("[FACEBOOK](https://youtube.com/)")
        st.markdown("[INSTAGRAM](https://youtube.com/)")
        

