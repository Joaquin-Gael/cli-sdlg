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
from components.API import GET

# Cargar datos
turnos_list = []
especialidades = []
medicos = []

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

# Crear un diccionario de especialidades para acceso rápido
especialidad_dict = {esp.especialidadID: esp.nombre for esp in especialidades}

# Crear un diccionario de médicos para acceso rápido
medico_dict = {medico.medicoID: medico.especialidadID for medico in medicos}

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

# Crear el gráfico
fig, ax = plt.subplots()
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
    st.write("Gráfico de Especialidades más Utilizadas")
    st.pyplot(fig)
