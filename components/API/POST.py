import requests, json, pydantic

BASE_URL = 'http://127.0.0.1:8000/api'

def post_user(user_data):
    url = f'{BASE_URL}/users/'
    response = requests.post(url, json=user_data)
    if response.status_code == 201:
        return response.json()
    return f'Error al crear el usuario: {response.status_code} - {response.text}'

def post_doctor(doctor_data):
    url = f'{BASE_URL}/doctors/'
    response = requests.post(url, json=doctor_data)
    if response.status_code == 201:
        return response.json()
    return f'Error al crear el usuario: {response.status_code} - {response.text}'

def post_turno(turno_data):
    url = f'{BASE_URL}/shifts/'
    response = requests.post(url, json=turno_data)
    if response.status_code == 201:
        return response.json()
    return f'Error al crear el usuario: {response.status_code} - {response.text}'

def post_testimony(testimonials_data):
    url = f'{BASE_URL}/testimonials/'
    response = requests.post(url, json=testimonials_data)
    if response.status_code == 201:
        return response.json()
    return f'Error al crear el usuario: {response.status_code} - {response.text}'

def post_location(locations_data):
    url = f'{BASE_URL}/locations/'
    response = requests.post(url, json=locations_data)
    if response.status_code == 201:
        return response.json()
    return f'Error al crear el usuario: {response.status_code} - {response.text}'

def post_department(departments_data):
    url = f'{BASE_URL}/departments/'
    response = requests.post(url, json=departments_data)
    if response.status_code == 201:
        return response.json()
    return f'Error al crear el usuario: {response.status_code} - {response.text}'

def post_specialty(specialties_data):
    url = f'{BASE_URL}/specialties/'
    response = requests.post(url, json=specialties_data)
    if response.status_code == 201:
        return response.json()
    return f'Error al crear el usuario: {response.status_code} - {response.text}'

def post_schedule(schedules_data):
    url = f'{BASE_URL}/schedules/'
    response = requests.post(url, json=schedules_data)
    if response.status_code == 201:
        return response.json()
    return f'Error al crear el usuario: {response.status_code} - {response.text}'

def post_appointment(appointments_data):
    url = f'{BASE_URL}/appointments/'
    response = requests.post(url, json=appointments_data)
    if response.status_code == 201:
        return response.json()
    return f'Error al crear el usuario: {response.status_code} - {response.text}'