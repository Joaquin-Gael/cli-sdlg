from components.API import (GET, POST,PUT,PATCH,DELETE)
from components.models.user import (User, UserValidationError)
from components.models.turno import (Turno, TurnoValidationError)
from components.models.cita import (Cita, CitaValidationError)
from components.models.especialidad import (Especialidad,EspecialidadValidationError)
from components.models.departamento import (Departamento,DepartamentoValidationError)
from components.models.ubicacion import (Ubicacion,UbicacionValidationError)
from components.models.medico import (Medico,MedicoValidationError)
from components.models.horario import (HorarioMedico,HorarioMedicoValidationError)
from components.models.testimonio import (Testimonio,TestimonioValidationError)
import pandas as pd
import requests
from tabulate import tabulate
from colorama import (init, Fore, Back, Style)

BASE_URL = 'http://127.0.0.1:8000/api'
init(autoreset=True)

def get_user_by_id(userID:int):
    try:
        url = f"{BASE_URL}/users/{userID}"
        response = GET.user(url)
        if response is not None:
            user_obj = User.validate_user(response)
            return user_obj
    
    except UserValidationError as e:
        print(e)

def get_users_data(query:dict):
    try:
        url = f"{BASE_URL}/users"
        response = GET.users(url, query)
        if response is not None:
            users_obj = [User.validate_user(user_data) for user_data in response]
            return User.tabla_users(users_obj)
    
    except UserValidationError as e:
        print(e)
        
def patch_user(userID:int, update_data):
    return PATCH.patch_user(userID, update_data)

    
def delete_user(userID):
    return DELETE.delete_user(userID)


def put_user(userID, update_data):
    return PUT.put_user(userID, update_data)

def post_user(userID):
    return POST.post_user(userID)

#---------------------------------------

def get_testimonio_by_id(id: int):
    try:
        url = f"{BASE_URL}/testimonials/{id}"
        response = GET.testimonio(url)
        if response is not None:
            testimonio_obj = Testimonio.validate_testimonio(response)
            return testimonio_obj
    except TestimonioValidationError as e:
        print(e)

def get_testimonios_data(query: dict):
    try:
        url = f"{BASE_URL}/testimonials"
        response = GET.testimonios(url, query)
        if response is not None:
            testimonios_obj = [Testimonio.validate_testimonio(testimonio_data) for testimonio_data in response]
            return Testimonio.tabla_testimonios(testimonios_obj)
    except TestimonioValidationError as e:
        print(e)

def patch_testimony(id:int, update_data):
    return PATCH.patch_testimonio(id, update_data)

    
def delete_testimony(id):
    return DELETE.delete_testimony(id)


def put_testimony(id, update_data):
    return PUT.put_testimony(id, update_data)

def post_testimony(id):
    return POST.post_testimony(id)


#---------------------------------------

def get_medico_by_id(medicoID: int):
    try:
        url = f"{BASE_URL}/doctors/{medicoID}"
        response = GET.medico(url)
        if response is not None:
            medico_obj = Medico.validate_medico(response)
            return medico_obj
    except MedicoValidationError as e:
        print(e)

def get_medicos_data(query: dict):
    try:
        url = f"{BASE_URL}/doctors"
        response = GET.medicos(url, query)
        if response is not None:
            medicos_obj = [Medico.validate_medico(medico_data) for medico_data in response]
            return Medico.tabla_medicos(medicos_obj)
    except MedicoValidationError as e:
        print(e)
        
def patch_doctor(medicoID:int, update_data):
    return PATCH.patch_doctor(medicoID, update_data)

    
def delete_doctor(medicoID):
    return DELETE.delete_doctor(medicoID)


def put_doctor(medicoID, update_data):
    return PUT.put_doctor(medicoID, update_data)

def post_doctor(medicoID):
    return POST.post_doctor(medicoID)

#---------------------------------------

def get_horario_medico_by_id(horarioID: int):
    try:
        url = f"{BASE_URL}/schedules/{horarioID}"
        response = GET.horario_medico(url)
        if response is not None:
            horario_medico_obj = HorarioMedico.validate_horario_medico(response)
            return horario_medico_obj
    except HorarioMedicoValidationError as e:
        print(e)

def get_horarios_medicos_data(query: dict):
    try:
        url = f"{BASE_URL}/schedules"
        response = GET.horarios_medicos(url, query)
        if response is not None:
            horarios_medicos_obj = [HorarioMedico.validate_horario_medico(horario_medico_data) for horario_medico_data in response]
            return HorarioMedico.tabla_horarios_medicos(horarios_medicos_obj)
    except HorarioMedicoValidationError as e:
        print(e)
        
def patch_schedule(horarioID:int, update_data):
    return PATCH.patch_horario(horarioID, update_data)

    
def delete_schedule(horarioID):
    return DELETE.delete_schedule(horarioID)


def put_schedule(horarioID, update_data):
    return PUT.put_schedule(horarioID, update_data)

def post_schedule(horarioID):
    return POST.post_schedule(horarioID)

#---------------------------------------

def get_turno_by_id(turnoID:int):
    try:
        url = f"{BASE_URL}/shifts/{turnoID}"
        response = GET.turno(url)
        if response is not None:
            turno_obj = Turno.validate_turno(response)
            return turno_obj
    
    except TurnoValidationError as e:
        print(e)

def get_turnos_data(query:dict):
    try:
        url = f"{BASE_URL}/shifts"
        response = GET.turnos(url, query)
        if response is not None:
            turnos_obj = [Turno.validate_turno(turno_data) for turno_data in response]
            return Turno.tabla_turnos(turnos_obj)
    
    except TurnoValidationError as e:
        print(e)

def patch_shift(turnoID:int, update_data):
    return PATCH.patch_turno(turnoID, update_data)

    
def delete_shift(turnoID):
    return DELETE.delete_turno(turnoID)


def put_shift(turnoID, update_data):
    return PUT.put_turno(turnoID, update_data)

def post_shift(turnoID):
    return POST.post_turno(turnoID)

#---------------------------------------

def get_cita_by_id(citaID: int):
    try:
        url = f"{BASE_URL}/appointments/{citaID}"
        response = GET.cita(url)
        if response is not None:
            cita_obj = Cita.validate_cita(response)
            return cita_obj
    except CitaValidationError as e:
        print(e)

def get_citas_data(query: dict):
    try:
        url = f"{BASE_URL}/appointments"
        response = GET.citas(url, query)
        if response is not None:
            citas_obj = [Cita.validate_cita(cita_data) for cita_data in response]
            return Cita.tabla_citas(citas_obj)
    except CitaValidationError as e:
        print(e)

def patch_appointment(citaID:int, update_data):
    return PATCH.patch_cita(citaID, update_data)

    
def delete_appointment(citaID):
    return DELETE.delete_appointment(citaID)


def put_appointment(citaID, update_data):
    return PUT.put_appointment(citaID, update_data)

def post_appointment(citaID):
    return POST.post_appointment(citaID)


#---------------------------------------

def get_ubicacion_by_id(ubicacionID: int):
    try:
        url = f"{BASE_URL}/locations/{ubicacionID}"
        response = GET.ubicacion(url)
        if response is not None:
            ubicacion_obj = Ubicacion.validate_ubicacion(response)
            return ubicacion_obj
    except UbicacionValidationError as e:
        print(e)
        
def get_ubicaciones_data(query: dict):
    try:
        url = f"{BASE_URL}/locations"
        response = GET.ubicaciones(url, query)
        if response is not None:
            ubicaciones_obj = [Ubicacion.validate_ubicacion(ubicacion_data) for ubicacion_data in response]
            return Ubicacion.tabla_ubicaciones(ubicaciones_obj)
    except UbicacionValidationError as e:
        print(e)

def patch_location(ubicacionID:int, update_data):
    return PATCH.patch_ubicacion(ubicacionID, update_data)

    
def delete_location(ubicacionID):
    return DELETE.delete_location(ubicacionID)


def put_location(ubicacionID, update_data):
    return PUT.put_location(ubicacionID, update_data)

def post_location(ubicacionID):
    return POST.post_location(ubicacionID)

#---------------------------------------

def get_departamento_by_id(departamentoID: int):
    try:
        url = f"{BASE_URL}/departments/{departamentoID}"
        response = GET.departamento(url)
        if response is not None:
            departamento_obj = Departamento.validate_departamento(response)
            return departamento_obj
    except DepartamentoValidationError as e:
        print(e)
        
def get_departamentos_data(query: dict):
    try:
        url = f"{BASE_URL}/departments"
        response = GET.departamentos(url, query)
        if response is not None:
            departamentos_obj = [Departamento.validate_departamento(departamento_data) for departamento_data in response]
            return Departamento.tabla_departamentos(departamentos_obj)
    except DepartamentoValidationError as e:
        print(e)

def patch_department(departamentoID:int, update_data):
    return PATCH.patch_departamento(departamentoID, update_data)

    
def delete_department(departamentoID):
    return DELETE.delete_department(departamentoID)


def put_department(departamentoID, update_data):
    return PUT.put_department(departamentoID, update_data)

def post_department(departamentoID):
    return POST.post_department(departamentoID)

#---------------------------------------

def get_especialidad_by_id(especialidadID: int):
    try:
        url = f"{BASE_URL}/specialties/{especialidadID}"
        response = GET.especialidad(url)
        if response is not None:
            especialidad_obj = Especialidad.validate_especialidad(response)
            return especialidad_obj
    except EspecialidadValidationError as e:
        print(e)

def get_especialidades_data(query: dict):
    try:
        url = f"{BASE_URL}/specialties"
        response = GET.especialidades(url, query)
        if response is not None:
            especialidades_obj = [Especialidad.validate_especialidad(especialidad_data) for especialidad_data in response]
            return Especialidad.tabla_especialidades(especialidades_obj)
    except EspecialidadValidationError as e:
        print(e)        

def patch_specialty(especialidadID:int, update_data):
    return PATCH.patch_especialidad(especialidadID, update_data)

    
def delete_specialty(especialidadID):
    return DELETE.delete_department(especialidadID)


def put_specialty(especialidadID, update_data):
    return PUT.put_department(especialidadID, update_data)

def post_specialty(especialidadID):
    return POST.post_specialty(especialidadID)

#---------------------------------------
if __name__ == '__main__':
    user_data = get_user_by_id(1)
    usesr_data = get_users_data({})
    print(user_data.tabla())