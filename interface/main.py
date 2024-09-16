import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from components.models.user import User
from components.models.especialidad import Especialidad
from components.models.medico import Medico
from components.models.turno import Turno
from components.models.departamento import Departamento
from components.API import GET

def graficar(titulo,xtexto,ytexto,rotacion):
    plt.title(titulo)
    plt.xlabel(xtexto)
    plt.ylabel(ytexto)
    plt.xticks(rotation=rotacion)
    plt.show()

# Cargar datos
turnos_list = []
especialidades = []
medicos = []
departamentos = []

#Obtener departamentos
for h in GET.departamentos():
    departamentos.append(
        Departamento(
            departamentoID=h['departamentoID'],
            nombre=h['nombre'],
            descripcion=h['descripcion'],
            ubicacionID=h['ubicacionID']
        )
    )

# Obtener médicos
for i in GET.medicos():
    medicos.append(
        Medico(
            medicoID=i['medicoID'], 
            nombre=i['nombre'], 
            apellido=i['apellido'], 
            dni=i['dni'], 
            especialidadID=i['especialidadID'], 
            telefono=i['telefono'], 
            email=i['email']
        )
    )

# Obtener especialidades
for j in GET.especialidades():
    especialidades.append(
        Especialidad(
            especialidadID=j['departamentoID'], 
            nombre=j['nombre'], 
            descripcion=j['descripcion'], 
            departamentoID=j['departamentoID']
        )
    )

# Obtener turnos
for ii in GET.turnos():
    turnos_list.append(
        Turno(
            TurnoID=ii['TurnoID'],
            userID=ii['userID'],
            citaID=ii['citaID'],
            medicoID=ii['medicoID'],
            motivo=ii['motivo'],
            estado=ii['estado'],
            fecha=ii['fecha'],
            fecha_created=ii['fecha_created']
        )
    )

# Diccionarios de acceso rápido
especialidad_dict = {esp.especialidadID: esp.nombre for esp in especialidades}
medico_dict = {medico.medicoID: medico.especialidadID for medico in medicos}
turnos_dict = {turno.turnoID: turno.medicoID for turno in turnos_list}
departamentos_dict = {departamento.departamentoID: departamento.nombre for departamento in departamentos}

# Contar turnos por especialidad
especialidad_count = Counter()
for turno in turnos_list:
    especialidad_id = medico_dict.get(turno.medicoID)
    if especialidad_id:
        especialidad_name = especialidad_dict.get(especialidad_id, 'Desconocida')
        especialidad_count[especialidad_name] += 1
# Convertir a DataFrame para graficar
data = {
    "Especialidad": list(especialidad_count.keys()),
    "Cantidad": list(especialidad_count.values())
}
df = pd.DataFrame(data)

# --Especialidades más comunes en los Médicos-- #
# DataFrames con Médicos y Especialidades asignadas
especialidades_df = pd.DataFrame(list(especialidad_dict.items()), columns=['especialidadID', 'nombre']) 
medicos_df = pd.DataFrame(list(medico_dict.items()), columns=['medicoID', 'especialidadID'])
medicos_especialidades = pd.merge(medicos_df, especialidades_df, on='especialidadID',how="inner")
count_nombres = medicos_especialidades.value_counts('nombre').head(5)
count_nombres_df = count_nombres.reset_index()
count_nombres_df.columns = ["nombre","cantidad"]

# --Cantidad de turnos atendidos por los médicos-- #
# DataFrames con Turnos + Médicos asignados
turnos_df = pd.DataFrame(list(turnos_dict.items()), columns=['turnoID','medicoID'])
medicos_df2 = pd.DataFrame(list(medico_dict.items()), columns=['medicoID','nombre','apellido'])
medicos_turnos = pd.merge(turnos_df,medicos_df,on="medicoID",how="inner")

medicos_turnos["Medico"] = medicos_turnos["nombre"] + " " + medicos_turnos["apellido"] 
df_nuevo_medicos_turnos = medicos_turnos[["Medico","turnoID"]]
df_final_medicos_turnos = df_nuevo_medicos_turnos.set_index("Medico")
count_turnos = df_final_medicos_turnos.value_counts('Medico')
df_count_turnos = count_turnos.reset_index()
df_count_turnos.columns = ["Medico","Cantidad de Turnos"]

# --Departamentos más recurridos-- #
departamentos_df = pd.DataFrame(list(departamentos_dict.items()), columns=['departamentoID','nombre','especialidadID'])
turnos_df_2 = pd.DataFrame(list(turnos_dict.items()), columns=['turnoID','departamentoID'])
turnos_departamentos = pd.merge(departamentos_df,turnos_df_2,on="departamentoID",how="inner")
df_nuevo_turnos_departamentos = turnos_departamentos[["turnoID","nombre"]]
df_final_turnos_departamentos = df_nuevo_turnos_departamentos.set_index("nombre")
count_dept = df_nuevo_turnos_departamentos.value_counts("nombre")
df_count_dept = count_dept.reset_index()
df_count_dept.columns = ["nombre","visitas"]

# Crear los gráficos
count_nombres_df.plot(x='nombre',y='cantidad',figsize=(10,5),kind="bar",legend=False)
fig1 = graficar("Las 10 especialidades más comunes en nuestros Médicos","Nombre","Cantidad",0)

df_count_turnos.plot(x='Medico',y='Cantidad de Turnos',figsize=(10,5),kind="bar",legend=False)
fig3 = graficar("Cantidad de turnos asignados a los médicos", "Médico", "Cantidad de turnos", 0)

df_count_dept.plot(x='nombre',y='visitas',figsize=(10,5),kind="bar",legend=False)
fig4 = graficar("Departamentos más recurridos","Nombre","Visitas",45)



# --Especialidades más recurridas en los turnos-- #
fig2, ax = plt.subplots()
ax.pie(df['Cantidad'], labels=df['Especialidad'], autopct='%1.1f%%', startangle=90)
ax.axis('equal')

# Mostrar en Streamlit
if __name__ == '__main__':
    responce = GET.users(url='http://127.0.0.1:8000/API/users/')
    with st.sidebar:
        st.title('Hospital SDLG :blue[CLI]')
        if responce is not None:
            st.success('This is a success data!', icon="✅")
        else:
            st.error('This is an error', icon="🚨")
    st.header('Users Table')
    st.table(
        User.data_frame_users(
            users_obj=[User.validate_user(user_data) for user_data in responce]
        )
    )
    st.pyplot(fig1)
    st.write("Gráfico de Especialidades más recurridas por los pacientes")
    st.pyplot(fig2)
    st.pyplot(fig3)
    st.pyplot(fig4)
