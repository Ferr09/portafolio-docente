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
    st.subheader("💻 Formatos Generales por Tipo de Modelo de PPL")
    st.write("Estructuras estándar de formulación e implementación en Python con Gurobi (`gurobipy`).")

    # --- SECCIÓN 1: FORMATOS GENERALES POR TIPO DE MODELO ---
    tab_p1, tab_p2, tab_p3, tab_p4 = st.tabs([
        "🎒 1. Problema de la Mochila", 
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

# Conjuntos y Parámetros
I = ["Item1", "Item2", "Item3"]
v = {"Item1": 10, "Item2": 15, "Item3": 25}  # Valor / Utilidad
w = {"Item1": 2,  "Item2": 4,  "Item3": 5}   # Peso / Recurso
W_max = 8                                    # Capacidad máxima

# Variable: y_i = 1 si se selecciona el ítem i, 0 e.o.c.
y = model.addVars(I, vtype=GRB.BINARY, name="y")

# Función Objetivo: Maximizar valor total
model.setObjective(gp.quicksum(v[i] * y[i] for i in I), GRB.MAXIMIZE)

# Restricción: No superar la capacidad
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

# Conjuntos y Parámetros
I = ["Planta1", "Planta2"]
c = {"Planta1": 5, "Planta2": 8}     # Costo variable por unidad
f = {"Planta1": 100, "Planta2": 150} # Costo fijo de activación
M = {"Planta1": 500, "Planta2": 600} # Capacidad máxima por planta

# Variables: x_i continua (nivel), y_i binaria (activación)
x = model.addVars(I, lb=0, vtype=GRB.CONTINUOUS, name="x")
y = model.addVars(I, vtype=GRB.BINARY, name="y")

# Función Objetivo: Minimizar Costo Variable + Costo Fijo
model.setObjective(gp.quicksum(c[i]*x[i] + f[i]*y[i] for i in I), GRB.MINIMIZE)

# Restricción Big-M: x_i <= M_i * y_i
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

# Conjuntos
I = ["Bodega1", "Bodega2"]  # Candidatos a instalación
J = ["Cliente1", "Cliente2", "Cliente3"]  # Clientes

f = {"Bodega1": 1000, "Bodega2": 1500} # Costo de apertura
c = {("Bodega1", "Cliente1"): 4, ("Bodega1", "Cliente2"): 6, ("Bodega1", "Cliente3"): 9,
     ("Bodega2", "Cliente1"): 5, ("Bodega2", "Cliente2"): 3, ("Bodega2", "Cliente3"): 4}

# Variables
y = model.addVars(I, vtype=GRB.BINARY, name="y")                   # 1 si abre instalación i
x = model.addVars(I, J, lb=0, vtype=GRB.CONTINUOUS, name="x")       # Flujo asignado de i a j

# Objetivo: Minimizar Costos de Apertura + Costos de Transporte
model.setObjective(
    gp.quicksum(f[i] * y[i] for i in I) + 
    gp.quicksum(c[i, j] * x[i, j] for i in I for j in J), 
    GRB.MINIMIZE
)

# Restricción 1: Satisfacer demanda de cada cliente j (asumiendo demanda normalizada = 1)
model.addConstrs((gp.quicksum(x[i, j] for i in I) == 1 for j in J), name="Demanda")

# Restricción 2: Solo enviar desde instalaciones abiertas (x_ij <= y_i)
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

T = [1, 2, 3, 4] # Períodos de tiempo
d = {1: 100, 2: 150, 3: 200, 4: 120} # Demanda por período
c, f, h = 10, 500, 2                 # Costo prod, costo fijo, costo inventario
M = 1000                             # Big-M (suma de demandas futuras)

# Variables
x = model.addVars(T, lb=0, vtype=GRB.CONTINUOUS, name="x") # Producción
s = model.addVars(T, lb=0, vtype=GRB.CONTINUOUS, name="s") # Inventario al final del período
y = model.addVars(T, vtype=GRB.BINARY, name="y")           # Setup de producción

# Objetivo
model.setObjective(
    gp.quicksum(c*x[t] + f*y[t] + h*s[t] for t in T), 
    GRB.MINIMIZE
)

# Balance de Inventarios: s_{t-1} + x_t = d_t + s_t
for t in T:
    s_prev = s[t-1] if t > 1 else 0  # Inventario inicial s_0 = 0
    model.addConstr(s_prev + x[t] == d[t] + s[t], name=f"Balance_t{t}")
    model.addConstr(x[t] <= M * y[t], name=f"Setup_t{t}")

model.optimize()
        """, language="python")

    st.markdown("---")

    # --- SECCIÓN 2: ERRORES TÍPICOS CON FUENTE AUMENTADA (HTML/CSS) ---
    st.markdown("""
    <style>
        .error-title {
            font-size: 26px !important;
            font-weight: bold !important;
            color: #DC2626 !important;
            margin-bottom: 10px;
        }
        .error-sub {
            font-size: 20px !important;
            font-weight: bold !important;
            color: #B91C1C !important;
            margin-top: 15px;
        }
        .error-body {
            font-size: 17px !important;
            line-height: 1.6 !important;
            color: #1F2937 !important;
        }
        .error-box {
            background-color: #FEF2F2;
            border-left: 6px solid #DC2626;
            padding: 18px;
            border-radius: 6px;
            margin-bottom: 20px;
        }
    </style>

    <div class="error-box">
        <div class="error-title">⚠️ Errores Típicos de Modelamiento en Gurobi</div>
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