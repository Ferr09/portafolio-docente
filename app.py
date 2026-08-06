import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Portafolio Docente",
    page_icon="👨‍🏫",
    layout="wide"
)

# --- ESTILOS CSS PERSONALIZADOS PARA LAS TARJETAS (CARDS) ---
st.markdown("""
<style>
    .card-title {
        font-size: 20px;
        font-weight: bold;
        margin-top: 10px;
        color: #1F2937;
    }
    .card-desc {
        font-size: 14px;
        color: #4B5563;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# --- DICCIONARIO DE CURSOS ---
# Puedes agregar más cursos fácilmente editando esta lista
cursos_data = [
    {
        "id": "curso1",
        "titulo": "Investigación Operativa",
        "descripcion": "Modelos de optimización, programación lineal, redes y teoría de decisiones.",
        "icono": "📊",
        "archivo": "cursos/curso_1.py"
    },
    {
        "id": "curso2",
        "titulo": "Econometría Aplicada",
        "descripcion": "Modelos de regresión, variables instrumentales, efectos fijos y series de tiempo.",
        "icono": "📈",
        "archivo": "cursos/curso_2.py"
    },
    {
        "id": "curso3",
        "titulo": "Ciencia de Datos & Data Mining",
        "descripcion": "Procesamiento de datos en Python/R, aprendizaje supervisado y visualización.",
        "icono": "💻",
        "archivo": "cursos/curso_3.py"
    },
    {
        "id": "curso4",
        "titulo": "Gestión de Operaciones",
        "descripcion": "Logística, cadenas de suministro, inventarios y simulación de procesos.",
        "icono": "⚙️",
        "archivo": "cursos/curso_4.py"
    }
]

# --- VISTA PRINCIPAL (LANDING PAGE) ---
def mostrar_landing_page():
    # 1. PORTADA: Imagen y Descripción Docente
    col_img, col_info = st.columns([1, 2], gap="large")
    
    with col_img:
        # Puedes reemplazar la URL por una imagen local colocada en tu proyecto
        st.image("https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=500", use_container_width=True)
    
    with col_info:
        st.title("Portafolio Docente & Académico")
        st.subheader("Profesor Adjunto / Investigador")
        st.write("""
        Bienvenido/a a mi espacio académico. En este portal encontrarás el material didáctico,
        herramientas interactivas, guías de código y recursos desarrollados para los cursos
        que imparto. Selecciona una materia a continuación para explorar sus contenidos.
        """)
        st.markdown("---")

    st.subheader("📚 Cursos y Asignaturas")
    st.write("Selecciona un curso para acceder a sus guías, evaluaciones y herramientas:")

    # 2. CUADRÍCULA EN DOS FILAS (2 columnas x 2 filas)
    for i in range(0, len(cursos_data), 2):
        col1, col2 = st.columns(2, gap="medium")
        
        # Tarjeta 1 de la fila
        with col1:
            curso = cursos_data[i]
            with st.container(border=True):
                st.markdown(f"### {curso['icono']} {curso['titulo']}")
                st.markdown(f"<p class='card-desc'>{curso['descripcion']}</p>", unsafe_allow_html=True)
                if st.button(f"Ver Materiales →", key=curso['id'], use_container_width=True):
                    st.session_state["curso_seleccionado"] = curso["id"]
                    st.rerun()

        # Tarjeta 2 de la fila (si existe)
        if i + 1 < len(cursos_data):
            with col2:
                curso = cursos_data[i+1]
                with st.container(border=True):
                    st.markdown(f"### {curso['icono']} {curso['titulo']}")
                    st.markdown(f"<p class='card-desc'>{curso['descripcion']}</p>", unsafe_allow_html=True)
                    if st.button(f"Ver Materiales →", key=curso['id'], use_container_width=True):
                        st.session_state["curso_seleccionado"] = curso["id"]
                        st.rerun()

# --- ENRUTAMIENTO / NAVEGACIÓN ---
if "curso_seleccionado" not in st.session_state:
    st.session_state["curso_seleccionado"] = "home"

if st.session_state["curso_seleccionado"] == "home":
    mostrar_landing_page()
else:
    # Botón para volver a la Landing Page desde cualquier curso
    if st.sidebar.button("← Volver a la Portada"):
        st.session_state["curso_seleccionado"] = "home"
        st.rerun()

    # Cargar el contenido del curso seleccionado
    selected_id = st.session_state["curso_seleccionado"]
    if selected_id == "curso1":
        st.title("📊 Modelamiento y Optimización - IN3171")
        st.write("Aquí anexarás tus guías de ejercicios, scripts en Python/R, pautas y simuladores.")
    elif selected_id == "curso2":
        st.title("📈 Econometría Aplicada")
        st.write("Aquí anexarás tus conjuntos de datos, scripts de R/Stata y lecturas.")
    elif selected_id == "curso3":
        st.title("💻 Ciencia de Datos & Data Mining")
        st.write("Aquí anexarás Jupyter Notebooks, datasets y proyectos prácticos.")
    elif selected_id == "curso4":
        st.title("⚙️ Gestión de Operaciones")
        st.write("Aquí anexarás casos de estudio, planillas y modelos de simulación.")