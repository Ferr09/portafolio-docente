import streamlit as st

st.title("📊 Modelamiento y Optimización - IN3171")
st.markdown("Bienvenido al módulo interactivo de Modelamiento y Optimización.")

tab1, tab2, tab3 = st.tabs(["📖 Programa y Lecturas", "💡 Cuestionarios y Práctica", "💻 Guías de Código"])

with tab1:
    st.subheader("Descarga de Apuntes")
    st.write("Aquí puedes consultar y descargar la pauta, el syllabus y guías teóricas del curso.")

with tab2:
    st.subheader("🧠 Autoevaluación y Diagnóstico Rápido")
    st.write("""
    Pon a prueba tus habilidades para identificar patrones y formular problemas de optimización. 
    Accede al siguiente cuestionario interactivo para ejercitar la detección rápida de modelos 
    a partir de enunciados y estructuras matemáticas.
    """)
    
    with st.container(border=True):
        st.markdown("### 📝 Cuestionario Interactivo: Identificación de Modelos")
        st.write("Aprende a reconocer rápidamente si un enunciado corresponde a Programación Lineal, Entera, Redes o Dinámica.")
        
        st.link_button(
            label="🚀 Abrir Cuestionario Interactivo (NotebookLM)", 
            url="https://notebooklm.google.com/notebook/88dde8d7-ad8e-4a7e-bc20-57e61e5b08b6/artifact/e5e5339c-4d27-40b1-8b65-53d3ba490688?utm_source=nlm_web_share&utm_medium=google_oo&utm_campaign=art_share_1&utm_content=&utm_smc=nlm_web_share_google_oo_art_share_1_",
            use_container_width=True,
            type="primary"
        )

with tab3:
    st.subheader("Ejemplos en Python (SciPy / PuLP)")
    st.code("""
    import scipy.optimize as opt
    # Resolver un problema de optimización lineal
    res = opt.linprog(c=[-3, -5], A_ub=[[1, 0], [0, 2], [3, 2]], b_ub=[4, 12, 18])
    print("Solución óptima:", res.x)
    """, language="python")