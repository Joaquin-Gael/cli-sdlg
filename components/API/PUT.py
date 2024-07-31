import requests, json, pydantic

BASE_URL = 'http://127.0.0.1:8000/api'


def put_user(userID:int, update_data):
    url = f'{BASE_URL}/users/{userID}/'
    response = requests.put(url, json=update_data)
    if response.status_code == 200:
        return response.json()
    return f'Error al actualizar el usuario: {response.status_code} - {response.text}'

def put_doctor(medicoID:int, update_data):
    url = f'{BASE_URL}/doctors/{medicoID}/'
    response = requests.put(url, json=update_data)
    if response.status_code == 200:
        return response.json()
    return f'Error al actualizar el usuario: {response.status_code} - {response.text}'

def put_turno(turnoID:int, update_data):
    url = f'{BASE_URL}/shifts/{turnoID}/'
    response = requests.put(url, json=update_data)
    if response.status_code == 200:
        return response.json()
    return f'Error al actualizar el usuario: {response.status_code} - {response.text}'

def put_testimony(id:int, update_data):
    url = f'{BASE_URL}/testimonials/{id}/'
    response = requests.put(url, json=update_data)
    if response.status_code == 200:
        return response.json()
    return f'Error al actualizar el usuario: {response.status_code} - {response.text}'

def put_location(ubicacionID:int, update_data):
    url = f'{BASE_URL}/locations/{ubicacionID}/'
    response = requests.put(url, json=update_data)
    if response.status_code == 200:
        return response.json()
    return f'Error al actualizar el usuario: {response.status_code} - {response.text}'

def put_specialty(especialidadID:int, update_data):
    url = f'{BASE_URL}/specialties/{especialidadID}/'
    response = requests.put(url, json=update_data)
    if response.status_code == 200:
        return response.json()
    return f'Error al actualizar el usuario: {response.status_code} - {response.text}'

def put_schedule(horarioID:int, update_data):
    url = f'{BASE_URL}/schedules/{horarioID}/'
    response = requests.put(url, json=update_data)
    if response.status_code == 200:
        return response.json()
    return f'Error al actualizar el usuario: {response.status_code} - {response.text}'

def put_appointment(citaID:int, update_data):
    url = f'{BASE_URL}/appointments/{citaID}/'
    response = requests.put(url, json=update_data)
    if response.status_code == 200:
        return response.json()
    return f'Error al actualizar el usuario: {response.status_code} - {response.text}'

def put_department(departamentoID:int, update_data):
    url = f'{BASE_URL}/departments/{departamentoID}/'
    response = requests.put(url, json=update_data)
    if response.status_code == 200:
        return response.json()
    return f'Error al actualizar el usuario: {response.status_code} - {response.text}'