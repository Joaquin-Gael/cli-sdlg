import requests, json, pydantic

BASE_URL = 'http://127.0.0.1:8000/api'

def patch_user(userID:int, update_data):
    url = f'{BASE_URL}/users/{userID}/'
    response = requests.patch(url, json=update_data)
    if response.status_code == 200:
        return response.json()
    return f'Error al actualizar el usuario: {response.status_code} - {response.text}'

def patch_doctor(medicoID:int, update_data):
    url = f'{BASE_URL}/doctors/{medicoID}/'
    response = requests.patch(url, json=update_data)
    if response.status_code == 200:
        return response.json()
    return f'Error al actualizar el usuario: {response.status_code} - {response.text}'

def patch_turno(turnoID:int, update_data):
    url = f'{BASE_URL}/shifts/{turnoID}/'
    response = requests.patch(url, json=update_data)
    if response.status_code == 200:
        return response.json()
    return f'Error al actualizar el usuario: {response.status_code} - {response.text}'

def patch_testimonio(id:int, update_data):
    url = f'{BASE_URL}/testimonials/{id}/'
    response = requests.patch(url, json=update_data)
    if response.status_code == 200:
        return response.json()
    return f'Error al actualizar el usuario: {response.status_code} - {response.text}'

def patch_ubicacion(id:int, update_data):
    url = f'{BASE_URL}/locations/{id}/'
    response = requests.patch(url, json=update_data)
    if response.status_code == 200:
        return response.json()
    return f'Error al actualizar el usuario: {response.status_code} - {response.text}'

def patch_departamento(departamentoID:int, update_data):
    url = f'{BASE_URL}/departments/{departamentoID}/'
    response = requests.patch(url, json=update_data)
    if response.status_code == 200:
        return response.json()
    return f'Error al actualizar el usuario: {response.status_code} - {response.text}'

def patch_especialidad(especialidadID:int, update_data):
    url = f'{BASE_URL}/specialties/{especialidadID}/'
    response = requests.patch(url, json=update_data)
    if response.status_code == 200:
        return response.json()
    return f'Error al actualizar el usuario: {response.status_code} - {response.text}'

def patch_horario(horarioID:int, update_data):
    url = f'{BASE_URL}/schedules/{horarioID}/'
    response = requests.patch(url, json=update_data)
    if response.status_code == 200:
        return response.json()
    return f'Error al actualizar el usuario: {response.status_code} - {response.text}'

def patch_cita(citaID:int, update_data):
    url = f'{BASE_URL}/appointments/{citaID}/'
    response = requests.patch(url, json=update_data)
    if response.status_code == 200:
        return response.json()
    return f'Error al actualizar el usuario: {response.status_code} - {response.text}'

