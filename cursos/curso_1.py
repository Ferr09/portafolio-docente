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
    st.write("Consulta el formulario de equivalencias matemáticas, diagnósticos de errores y estructuras de código por tipo de modelo.")

    # =========================================================================
    # 1. FORMULARIO SINTÁCTICO DE GUROBI
    # =========================================================================
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

    st.markdown("---")

    # =========================================================================
    # 2. SECCIÓN DE ERRORES TÍPICOS CON FUENTE AMPLIADA
    # =========================================================================
    st.markdown("""
    <style>
        .error-title {
            font-size: 26px !important;
            font-weight: bold !important;
            color: #DC2626 !important;
            margin-bottom: 12px;
        }
        .error-sub {
            font-size: 20px !important;
            font-weight: bold !important;
            color: #B91C1C !important;
            margin-top: 18px;
        }
        .error-body {
            font-size: 17px !important;
            line-height: 1.6 !important;
            color: #1F2937 !important;
        }
        .error-box {
            background-color: #FEF2F2;
            border-left: 6px solid #DC2626;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 25px;
        }
    </style>

    <div class="error-box">
        <div class="error-title">⚠️ Errores Típicos de Modelamiento y Diagnóstico en Gurobi</div>
        <div class="error-body">
            A continuación se resumen los fallos más frecuentes al formular o programar un modelo en Gurobi:
        </div>
        
        <div class="error-sub">1. Diagnóstico por Estado del Solver (model.Status)</div>
        <div class="error-body">
            <ul>
                <li><b>UNBOUNDED (Estado 4):</b> La función objetivo crece o decrece al infinito. Ocurre por <b>falta de restricciones de capacidad</b> o cotas en las variables.</li>
                <li><b>INFEASIBLE (Estado 3):</b> No existe ninguna solución factible. Ocurre por <b>contradicciones lógicas</b> (signos equivocados <code>>=</code> por <code><=</code>) o demandas mayores a la capacidad disponible.</li>
                <li><b>INF_OR_UNBD (Estado 5):</b> Modelo infactible o no acotado. Ocurre habitualmente al omitir dominios base como <code>lb=0</code>.</li>
            </ul>
        </div>

        <div class="error-sub">2. Errores de Declaración de Variables</div>
        <div class="error-body">
            <ul>
                <li><b>Variables continuas no negativas por defecto:</b> <code>model.addVar()</code> asume <code>lb=0.0</code>. Si requieres variables irrestrictas (ej. utilidades negativas), debes indicar explícitamente <code>lb=-GRB.INFINITY</code>.</li>
                <li><b>Omisión de vtype en variables indexadas:</b> Si no especificas <code>vtype=GRB.BINARY</code> en <code>addVars()</code>, Gurobi asumirá que son continuas y entregará valores fraccionarios (ej. 0.34).</li>
            </ul>
        </div>

        <div class="error-sub">3. Errores en la Función Objetivo</div>
        <div class="error-body">
            <ul>
                <li><b>Sentido por defecto:</b> Gurobi asume <code>GRB.MINIMIZE</code> si omites el segundo argumento en <code>setObjective()</code>. Si estás maximizando beneficios, debes especificar <code>GRB.MAXIMIZE</code>.</li>
                <li><b>Costos fijos desconectados:</b> Sumar la binaria de costo fijo $y_i$ en el objetivo pero olvidar la restricción de activación Big-M ($x_i \le M \cdot y_i$).</li>
            </ul>
        </div>

        <div class="error-sub">4. Errores en el Parámetro Big-M</div>
        <div class="error-body">
            <ul>
                <li><b>M demasiado pequeño:</b> Recorta y elimina soluciones válidas de la región factible.</li>
                <li><b>M demasiado grande ($> 10^8$):</b> Produce problemas de mala condición numérica. Gurobi tratará valores muy pequeños como cero, permitiendo producir $x_i > 0$ sin pagar el costo fijo.</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # =========================================================================
    # 3. SECCIÓN DE EJEMPLOS DE CÓDIGO POR TIPO DE PPL
    # =========================================================================
    st.subheader("🚀 Ejemplos de Código por Tipo de PPL")
    st.write("Estructuras estándar de formulación e implementación en Python con Gurobi (`gurobipy`).")

    tab_p1, tab_p2, tab_p3, tab_p4 = st.tabs([
        "🎒 1. Mochila (Knapsack)", 
        "🏭 2. Costo Fijo / Capacidad", 
        "🏢 3. Localización (Facility Location)",
        "📦 4. Dimensionamiento de Lote (Lot Sizing)"
    ])

    with tab_p1:
        st.markdown("### Formato General: Problema de la Mochila (Knapsack)")
        st.write("Selección de un conjunto de ítems para maximizar valor sujeto a un límite de capacidad física o presupuestaria.")
        st.code("""
import gurobipy as gp
from gurobipy import GRB

model = gp.Model("Knapsack")

I = ["Item1", "Item2", "Item3"]
v = {"Item1": 10, "Item2": 15, "Item3": 25}  # Valor / Utilidad
w = {"Item1": 2,  "Item2": 4,  "Item3": 5}   # Peso / Recurso
W_max = 8                                    # Capacidad máxima

y = model.addVars(I, vtype=GRB.BINARY, name="y")

model.setObjective(gp.quicksum(v[i] * y[i] for i in I), GRB.MAXIMIZE)
model.addConstr(gp.quicksum(w[i] * y[i] for i in I) <= W_max, name="Capacidad")

model.optimize()
        """, language="python")

    with tab_p2:
        st.markdown("### Formato General: Activación y Costo Fijo (Big-M)")
        st.write("Modelación de decisiones donde la producción o activación de una línea incurre en un costo fijo único.")
        st.code("""
import gurobipy as gp
from gurobipy import GRB

model = gp.Model("Costo_Fijo")

I = ["Planta1", "Planta2"]
c = {"Planta1": 5, "Planta2": 8}     # Costo variable por unidad
f = {"Planta1": 100, "Planta2": 150} # Costo fijo de activación
M = {"Planta1": 500, "Planta2": 600} # Capacidad máxima por planta

x = model.addVars(I, lb=0, vtype=GRB.CONTINUOUS, name="x")
y = model.addVars(I, vtype=GRB.BINARY, name="y")

model.setObjective(gp.quicksum(c[i]*x[i] + f[i]*y[i] for i in I), GRB.MINIMIZE)
model.addConstrs((x[i] <= M[i] * y[i] for i in I), name="Activacion_BigM")

model.optimize()
        """, language="python")

    with tab_p3:
        st.markdown("### Formato General: Localización de Instalaciones (Facility Location)")
        st.write("Decidir qué instalaciones abrir y cómo asignar la demanda de los clientes hacia ellas.")
        st.code("""
import gurobipy as gp
from gurobipy import GRB

model = gp.Model("Facility_Location")

I = ["Bodega1", "Bodega2"]  # Candidatos a instalación
J = ["Cliente1", "Cliente2", "Cliente3"]  # Clientes

f = {"Bodega1": 1000, "Bodega2": 1500} # Costo de apertura
c = {("Bodega1", "Cliente1"): 4, ("Bodega1", "Cliente2"): 6, ("Bodega1", "Cliente3"): 9,
     ("Bodega2", "Cliente1"): 5, ("Bodega2", "Cliente2"): 3, ("Bodega2", "Cliente3"): 4}

y = model.addVars(I, vtype=GRB.BINARY, name="y")
x = model.addVars(I, J, lb=0, vtype=GRB.CONTINUOUS, name="x")

model.setObjective(
    gp.quicksum(f[i] * y[i] for i in I) + 
    gp.quicksum(c[i, j] * x[i, j] for i in I for j in J), 
    GRB.MINIMIZE
)

model.addConstrs((gp.quicksum(x[i, j] for i in I) == 1 for j in J), name="Demanda")
model.addConstrs((x[i, j] <= y[i] for i in I for j in J), name="Apertura")

model.optimize()
        """, language="python")

    with tab_p4:
        st.markdown("### Formato General: Dimensionamiento de Lote (Lot Sizing)")
        st.write("Planificación multi-período equilibrando costos de producción, inventario y costos fijos de preparación (*setup*).")
        st.code("""
import gurobipy as gp
from gurobipy import GRB

model = gp.Model("Lot_Sizing")

T = [1, 2, 3, 4]
d = {1: 100, 2: 150, 3: 200, 4: 120}
c, f, h = 10, 500, 2
M = 1000

x = model.addVars(T, lb=0, vtype=GRB.CONTINUOUS, name="x")
s = model.addVars(T, lb=0, vtype=GRB.CONTINUOUS, name="s")
y = model.addVars(T, vtype=GRB.BINARY, name="y")

model.setObjective(
    gp.quicksum(c*x[t] + f*y[t] + h*s[t] for t in T), 
    GRB.MINIMIZE
)

for t in T:
    s_prev = s[t-1] if t > 1 else 0
    model.addConstr(s_prev + x[t] == d[t] + s[t], name=f"Balance_t{t}")
    model.addConstr(x[t] <= M * y[t], name=f"Setup_t{t}")

model.optimize()
        """, language="python")