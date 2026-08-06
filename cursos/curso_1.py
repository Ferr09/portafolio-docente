import streamlit as st

st.title("📊 Modelamiento y Optimización - IN3171")
st.markdown("Bienvenido al módulo interactivo de Modelamiento y Optimización.")

tab1, tab2, tab3 = st.tabs(["📖 Programa y Lecturas", "💡 Cuestionarios y Práctica", "💻 Guías de Código"])

with tab1:
    st.subheader("Descarga de Apuntes")
    st.write("Aquí puedes consultar y descargar la pauta, el syllabus y guías teóricas del curso.")

with tab2:
    st.subheader("🧠 Entrenamiento rápido")
    st.write("""
    Esta sección permite entrenar tus habilidades para identificar patrones y formular problemas de optimización.
    """)
    
    with st.container(border=True):
        st.markdown("### 📝 Quiz Semana 1 - Programación Lineal & Modelos Clásicos")
        st.write("Aprende a reconocer rápidamente si un enunciado corresponde a problemas de la mochila, dimensionamiento de lote, facility location u otros modelos fundamentales.")
        
        st.link_button(
            label="🚀 Abrir Quiz Semana 1 (NotebookLM)", 
            url="https://notebook.google.com/notebook/88dde8d7-ad8e-4a7e-bc20-57e61e5b08b6/artifact/5ce3f142-5d02-4d9e-bc9a-8a2026bf98ef?utm_source=nlm_web_share&utm_medium=google_oo&utm_campaign=art_share_1&utm_content=&utm_smc=nlm_web_share_google_oo_art_share_1_",
            use_container_width=True,
            type="primary"
        )

    with st.container(border=True):
        st.markdown("### 📝 Cuestionario General: Detección Rápida de Modelos")
        st.write("Ejercita la identificación de estructuras entre Programación Lineal, Entera, Redes o Dinámica a partir de enunciados y expresiones matemáticas.")
        
        st.link_button(
            label="🚀 Abrir Cuestionario General (NotebookLM)", 
            url="https://notebooklm.google.com/notebook/88dde8d7-ad8e-4a7e-bc20-57e61e5b08b6/artifact/e5e5339c-4d27-40b1-8b65-53d3ba490688?utm_source=nlm_web_share&utm_medium=google_oo&utm_campaign=art_share_1&utm_content=&utm_smc=nlm_web_share_google_oo_art_share_1_",
            use_container_width=True,
            type="secondary"
        )

with tab3:
    st.subheader("💻 Sintaxis y Formulario Computacional Gurobi (`gurobipy`)")
    st.write("""
    Consulta la equivalencia entre la formulación matemática y su implementación directa en **Python con Gurobi**.
    """)

    # --- DESPLEGABLE 1: FORMULARIO SINTÁCTICO DE GUROBI ---
    with st.expander("📖 **Ver Formulario Sintáctico Completo (Variables, Objetivos, Big-M e Indicadoras)**", expanded=True):
        st.markdown("### 1. Declaración de Variables y Dominios")
        st.markdown("""
        | Tipo de Variable | Expresión Matemática | Sintaxis Computacional (`gurobipy`) |
        | :--- | :--- | :--- |
        | **Continua No Negativa** | $x \\in \\mathbb{R}_{\\ge 0}$ | `x = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="x")` |
        | **Continua Irrestricta** | $x \\in \\mathbb{R}$ | `x = model.addVar(lb=-GRB.INFINITY, vtype=GRB.CONTINUOUS)` |
        | **Binaria** | $x \\in \\{0, 1\\}$ | `x = model.addVar(vtype=GRB.BINARY, name="x")` |
        | **Entera General** | $x \\in \\mathbb{Z}_{\\ge 0}$ | `x = model.addVar(lb=0, vtype=GRB.INTEGER, name="x")` |
        | **Entera Acotada** | $x \\in \\{L, \\dots, U\\}$ | `x = model.addVar(lb=L, ub=U, vtype=GRB.INTEGER)` |
        | **Indexada por Conjuntos** | $x_{i,j} \\in \\mathbb{R}_{\\ge 0}, \\quad \\forall i \\in I, j \\in J$ | `x = model.addVars(I, J, lb=0, vtype=GRB.CONTINUOUS, name="x")` |
        """)

        st.markdown("---")
        st.markdown("### 2. Función Objetivo (Exclusivamente Lineal)")
        st.markdown("""
        | Tipo de Objetivo | Expresión Matemática | Sintaxis Computacional (`gurobipy`) |
        | :--- | :--- | :--- |
        | **Lineal (Minimización)** | $\\min \\sum_{i \\in I} c_i x_i$ | `model.setObjective(gp.quicksum(c[i] * x[i] for i in I), GRB.MINIMIZE)` |
        | **Lineal (Maximización)** | $\\max \\sum_{i \\in I} c_i x_i$ | `model.setObjective(gp.quicksum(c[i] * x[i] for i in I), GRB.MAXIMIZE)` |
        | **Lineal Vectorial/Matricial** | $\\min c^T x$ | `model.setObjective(c @ x, GRB.MINIMIZE)` |
        """)

        st.markdown("---")
        st.markdown("### 3. Lógica Booleana y Condicionales (Big-M)")
        st.markdown("""
        | Concepto Lógico | Expresión Matemática | Sintaxis Computacional (`gurobipy`) |
        | :--- | :--- | :--- |
        | **Activación / Capacidad (Big-M)** | $x \\le M \\cdot y, \\quad y \\in \\{0, 1\\}$ | `model.addConstr(x <= M * y)` |
        | **Costo Fijo con Producción** | $x_i \\le M_i \\cdot y_i \\quad \\forall i \\in I$ | `model.addConstrs(x[i] <= M[i] * y[i] for i in I)` |
        | **O Exclusivo (Either-Or)** | $\\begin{cases} f(x) \\le b_1 + M y \\\\ g(x) \\le b_2 + M(1-y) \\end{cases}$ | `model.addConstr(f_x <= b1 + M * y)`<br>`model.addConstr(g_x <= b2 + M * (1 - y))` |
        | **Seleccionar $k$ de $N$** | $\\sum_{i \\in I} y_i = k$ | `model.addConstr(gp.quicksum(y[i] for i in I) == k)` |
        """)

        st.markdown("---")
        st.markdown("### 4. Restricciones Indicadoras Generalizadas")
        st.markdown("""
        | Relación Lógica | Expresión Matemática | Sintaxis Computacional (`gurobipy`) |
        | :--- | :--- | :--- |
        | **Si $y=1 \\implies a^T x \\le b$** | $y = 1 \\implies \\sum_{j} a_j x_j \\le b$ | `model.addGenConstrIndicator(y, True, gp.quicksum(a[j]*x[j] for j in J) <= b)` |
        | **Si $y=0 \\implies a^T x \\le b$** | $y = 0 \\implies \\sum_{j} a_j x_j \\le b$ | `model.addGenConstrIndicator(y, False, gp.quicksum(a[j]*x[j] for j in J) <= b)` |
        | **Implicación con Igualdad** | $y = 1 \\implies \\sum_{j} a_j x_j = b$ | `model.addGenConstrIndicator(y, True, gp.quicksum(a[j]*x[j] for j in J) == b)` |
        """)

    # --- DESPLEGABLE 2: ERRORES TÍPICOS DE MODELAMIENTO Y DIAGNÓSTICO EN GUROBI ---
    with st.expander("⚠️ **Errores Típicos de Modelamiento y Diagnóstico en Gurobi**", expanded=False):
        st.markdown("""
        Al formular un modelo en Gurobi, los errores más comunes no siempre lanzan un fallo en Python, sino que resultan en un **modelo mal planteado** (soluciones absurdas o infactibles). A continuación se resumen los diagnósticos clave:

        ---

        #### 1. Diagnóstico por Estado del Solver (`model.Status`)

        | Estado / Mensaje en Consola | Significado Matemático | Causa Habitual en el Código |
        | :--- | :--- | :--- |
        | **`UNBOUNDED` (Estado 4)** | La función objetivo puede crecer/decrecer hacia el infinito. | **Falta de restricciones:** Olvidaste acotar variables de producción/flujo o la función objetivo maximiza sin limite. |
        | **`INFEASIBLE` (Estado 3)** | No existe ninguna solución que cumpla todas las restricciones a la vez. | **Contradicción lógica:** Restricciones con el signo equivocado (`>=` en vez de `<=`), capacidades menores a la demanda mínima, o constante $M$ muy pequeña. |
        | **`INF_OR_UNBD` (Estado 5)** | El modelo es Infactible o No Acotado. | Ocurre frecuentemente cuando faltan dominios de variables ($lb=0$) y las restricciones se contradicen. |

        > 💡 **Tip de Diagnóstico para Infactibilidad:** Si tu modelo es `INFEASIBLE`, puedes agregar esta línea para que Gurobi te indique qué restricciones se están contradiciendo (Irreducible Inconsistent Subsystem):
        """)
        
        st.code("""
# Si el modelo resulta infactible, genera el reporte de conflicto
if model.status == GRB.INFEASIBLE:
    model.computeIIS()
    model.write("modelo_conflicto.ilp")  # Guarda las restricciones contradictorias
        """, language="python")

        st.markdown("""
        ---

        #### 2. Errores de Declaración de Variables y Dominios

        * **Variables Continuas Negativas por Defecto:**
          * **Sintaxis:** `x = model.addVar()` (por defecto `lb=0.0`).
          * **Error Típico:** Si necesitas una variable irrestricta (que pueda tomar valores negativos como utilidades o desviaciones), debes declarar explícitamente `lb=-GRB.INFINITY`. De lo contrario, Gurobi asumirá $x \\ge 0$.
        * **Confusión de Dominios en Variables Indexadas:**
          * **Error Típico:** Olvidar especificar `vtype=GRB.BINARY` o `vtype=GRB.INTEGER` al usar `addVars()`. Si no se especifica, Gurobi declara las variables como **continuas**, lo que provocará que tus decisiones "sí/no" adopten valores fraccionarios como `0.45` o `0.82`.

        ---

        #### 3. Errores en la Función Objetivo

        * **Olvidar el Sentido de Optimización (`GRB.MINIMIZE` vs `GRB.MAXIMIZE`):**
          * **Error Típico:** Por defecto, si usas `model.setObjective(expresion)` sin segundo argumento, Gurobi asume **Minimización**. Si estás maximizando beneficios y lo olvidas, el modelo intentará hacer la producción cero o no acotarse.
        * **Costos Fijos Desconectados:**
          * **Sintaxis Incorrecta:** Sumar la variable binaria $y_i$ en la función objetivo sin agregar la restricción de activación Big-M ($x_i \\le M \\cdot y_i$).
          * **Consecuencia:** Como $y_i$ suma costo en la función objetivo y no restringe a $x_i$, el solver fijará $y_i = 0$ y $x_i > 0$, generando una solución matemáticamente libre de costo fijo.

        ---

        #### 4. Errores Frecuentes en Big-M y Lógica Booleana

        * **Valor de $M$ Demasiado Pequeño:**
          * **Consecuencia:** Si la producción real $x_i$ necesita ser $1500$, pero fijaste $M = 1000$ en la restricción $x_i \\le M \\cdot y_i$, estás recortando artificialmente la región factible del problema.
        * **Valor de $M$ Demasiado Grande ($10^9$ o más):**
          * **Consecuencia:** Genera **problemas de mala condición numérica** (*ill-conditioning*). Gurobi puede considerar que un número muy pequeño (como $0.0000001$) es equivalente a $0$, permitiendo que $x_i > 0$ sin activar la binaria $y_i$.
        * **Solución:** Utilizar el mínimo $M$ válido (e.g., la capacidad máxima física de la planta) o sustituir por **Restricciones Indicadoras** (`model.addGenConstrIndicator`).
        """)

    st.markdown("---")
    st.subheader("🚀 Ejemplos Código Ejecutable")

    tab_ej1, tab_ej2, tab_ej3 = st.tabs([
        "1. Estructura General", 
        "2. Aplicación Big-M", 
        "3. Restricciones Indicadoras"
    ])

    with tab_ej1:
        st.code("""
import gurobipy as gp
from gurobipy import GRB

# Crear Modelo
model = gp.Model("Ejemplo_Base")

# Conjuntos y Datos
I = ["A", "B", "C"]
c = {"A": 25, "B": 30, "C": 20}
a = {"A": 2, "B": 3.5, "C": 1.5}

# 1. Variables Indexadas
x = model.addVars(I, lb=0, vtype=GRB.CONTINUOUS, name="x")

# 2. Función Objetivo
model.setObjective(gp.quicksum(c[i] * x[i] for i in I), GRB.MAXIMIZE)

# 3. Restricción Lineal
model.addConstr(gp.quicksum(a[i] * x[i] for i in I) <= 100, name="Capacidad")

# 4. Optimizar
model.optimize()
        """, language="python")

    with tab_ej2:
        st.code("""
import gurobipy as gp
from gurobipy import GRB

model = gp.Model("Ejemplo_BigM")
M = 1000
I = [1, 2, 3]
c, f = {1: 10, 2: 15, 3: 20}, {1: 100, 2: 150, 3: 120}

x = model.addVars(I, lb=0, vtype=GRB.CONTINUOUS, name="x")
y = model.addVars(I, vtype=GRB.BINARY, name="y")

# Objetivo: Minimizar Costo Variable + Costo Fijo
model.setObjective(gp.quicksum(c[i] * x[i] + f[i] * y[i] for i in I), GRB.MINIMIZE)

# Relación Big-M: x_i <= M * y_i
model.addConstrs((x[i] <= M * y[i] for i in I), name="BigM_CostoFijo")

model.optimize()
        """, language="python")

    with tab_ej3:
        st.code("""
import gurobipy as gp
from gurobipy import GRB

model = gp.Model("Ejemplo_Indicadoras")
J = [1, 2, 3]
a = {1: 2.5, 2: 1.0, 3: 4.0}
b = 25.0

x = model.addVars(J, lb=0, vtype=GRB.CONTINUOUS, name="x")
y = model.addVar(vtype=GRB.BINARY, name="y")

# Restricción Indicadora: Si y = 1 => sum(a_j * x_j) <= b
model.addGenConstrIndicator(y, True, gp.quicksum(a[j] * x[j] for j in J) <= b, name="Si_Y_Es_1")

model.setObjective(gp.quicksum(x[j] for j in J), GRB.MAXIMIZE)
model.optimize()
        """, language="python")