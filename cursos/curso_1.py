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
        st.markdown("### 📝 Cuestionario Semana 1 - Programación Lineal")
        st.write("Aprende a reconocer rápidamente si un enunciado corresponde a modelos de problema de la mochila, dimensionamiento de lote o facility location.")
        
        st.link_button(
            label="🚀 Abrir Quiz (NotebookLM)", 
            url="https://notebooklm.google.com/notebook/88dde8d7-ad8e-4a7e-bc20-57e61e5b08b6/artifact/e5e5339c-4d27-40b1-8b65-53d3ba490688?utm_source=nlm_web_share&utm_medium=google_oo&utm_campaign=art_share_1&utm_content=&utm_smc=nlm_web_share_google_oo_art_share_1_",
            use_container_width=True,
            type="primary"
        )

with tab3:
    st.subheader("💻 Implementación en Python con Gurobi (`gurobipy`)")
    st.write("""
    A continuación encuentras ejemplos prácticos para implementar modelos de optimización lineal y entera 
    utilizando la librería **Gurobi Python API**. Revisa las sintaxis para variables, funciones objetivo, 
    modelación Big-M y restricciones indicadoras.
    """)

    # Sub-pestañas dentro de la sección de código para organizar el formulario
    tab_ej1, tab_ej2, tab_ej3 = st.tabs([
        "🚀 1. Ejemplo Completo", 
        "🔀 2. Modelación Big-M", 
        "🎯 3. Restricciones Indicadoras"
    ])

    with tab_ej1:
        st.markdown("#### Ejemplo Completo: Problema de Mezcla y Capacidad con Variables Indexadas")
        st.write("Este script muestra la estructura completa para declarar un modelo, agregar variables indexadas, definir la función objetivo con `gp.quicksum` y resolver.")
        
        st.code("""
import gurobipy as gp
from gurobipy import GRB

# 1. Crear el modelo
model = gp.Model("Ejemplo_Mezcla")

# Conjuntos e Índices
I = ["Producto_A", "Producto_B", "Producto_C"]
c = {"Producto_A": 25, "Producto_B": 30, "Producto_C": 20}  # Beneficios
a = {"Producto_A": 2,  "Producto_B": 3.5, "Producto_C": 1.5} # Uso de recurso por unidad
L, U = 5, 50 # Límites para variables enteras

# 2. Declaración de Variables (Continua, Entera Acotada y Binaria)
x = model.addVars(I, lb=0, vtype=GRB.CONTINUOUS, name="x")          # Continua No Negativa x_i >= 0
z = model.addVars(I, lb=L, ub=U, vtype=GRB.INTEGER, name="z")       # Entera Acotada z_i in {L,...,U}
y = model.addVars(I, vtype=GRB.BINARY, name="y")                   # Binaria y_i in {0,1}

# 3. Función Objetivo (Maximizar Beneficio Total)
# \max \sum_{i \in I} c_i x_i
model.setObjective(gp.quicksum(c[i] * x[i] for i in I), GRB.MAXIMIZE)

# 4. Restricciones Lineales
# Restricción de disponibilidad de recurso
Capacidad_Max = 100
model.addConstr(gp.quicksum(a[i] * x[i] for i in I) <= Capacidad_Max, name="Capacidad_Recurso")

# 5. Resolver el modelo
model.optimize()

# 6. Imprimir Resultados
if model.status == GRB.OPTIMAL:
    print(f"Valor Óptimo de la Función Objetivo: {model.ObjVal}")
    for i in I:
        print(f"Producción {i} (x[{i}]): {x[i].X}")
        """, language="python")

    with tab_ej2:
        st.markdown("#### Lógica Booleana y Condicionales (Big-M)")
        st.write("Ejemplos de implementación de activación de capacidad, costos fijos y la lógica *Either-Or* (O Exclusivo) utilizando constantes $M$.")
        
        st.code("""
import gurobipy as gp
from gurobipy import GRB

model = gp.Model("Modelacion_BigM")

# Parámetros y Constantes
M = 1000  # Parámetro Big-M suficientemente grande
I = [1, 2, 3]
c = {1: 10, 2: 15, 3: 20}   # Costo variable
f = {1: 100, 2: 150, 3: 120} # Costo fijo
k = 2                       # Seleccionar exactamente k productos

# Variables
x = model.addVars(I, lb=0, vtype=GRB.CONTINUOUS, name="x") # Nivel de producción
y = model.addVars(I, vtype=GRB.BINARY, name="y")           # Decisión de activar producción

# Función Objetivo: Minimizar Costos Variables + Costos Fijos
# \min \sum_{i \in I} (c_i x_i + f_i y_i)
model.setObjective(
    gp.quicksum(c[i] * x[i] + f[i] * y[i] for i in I), 
    GRB.MINIMIZE
)

# Costo Fijo y Capacidad (Activación con Big-M): x_i <= M_i * y_i
model.addConstrs((x[i] <= M * y[i] for i in I), name="CostoFijo_Capacidad")

# Seleccionar k de N elementos: \sum_{i \in I} y_i = k
model.addConstr(gp.quicksum(y[i] for i in I) == k, name="Seleccionar_K")

# O Exclusivo (Either-Or): f(x) <= b1 + M*y OR g(x) <= b2 + M*(1-y)
# Ejemplo: (2x1 + 3x2 <= 50) O (x1 + 4x2 <= 40)
y_or = model.addVar(vtype=GRB.BINARY, name="y_or")
model.addConstr(2 * x[1] + 3 * x[2] <= 50 + M * y_or, name="O_Exclusivo_1")
model.addConstr(x[1] + 4 * x[2] <= 40 + M * (1 - y_or), name="O_Exclusivo_2")

model.optimize()
        """, language="python")

    with tab_ej3:
        st.markdown("#### Restricciones Indicadoras (General Constraints)")
        st.write("Permiten modelar condicionales lógicos del tipo $y = 1 \\implies a^T x \\le b$ sin necesidad de utilizar el parámetro $M$, previniendo problemas de mala condición numérica.")
        
        st.code("""
import gurobipy as gp
from gurobipy import GRB

model = gp.Model("Restricciones_Indicadoras")

J = [1, 2, 3, 4]
a = {1: 2.5, 2: 1.0, 3: 4.0, 4: 1.5}
b = 25.0

# Variables
x = model.addVars(J, lb=0, vtype=GRB.CONTINUOUS, name="x")
y = model.addVar(vtype=GRB.BINARY, name="y")
w = model.addVar(vtype=GRB.BINARY, name="w")

# 1. Si y = 1 => sum(a_j * x_j) <= b
model.addGenConstrIndicator(
    y, True, 
    gp.quicksum(a[j] * x[j] for j in J) <= b, 
    name="Indicadora_Si_Y_Es_1"
)

# 2. Si y = 0 => sum(a_j * x_j) <= b
model.addGenConstrIndicator(
    y, False, 
    gp.quicksum(a[j] * x[j] for j in J) <= b, 
    name="Indicadora_Si_Y_Es_0"
)

# 3. Implicación con Igualdad: Si w = 1 => sum(a_j * x_j) = b
model.addGenConstrIndicator(
    w, True, 
    gp.quicksum(a[j] * x[j] for j in J) == b, 
    name="Indicadora_Igualdad"
)

# Definir objetivo y optimizar
model.setObjective(gp.quicksum(x[j] for j in J), GRB.MAXIMIZE)
model.optimize()
        """, language="python")