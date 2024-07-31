import requests, json, pydantic

BASE_URL = 'http://127.0.0.1:8000/api'

def delete_user(userID:int):
    url = f'{BASE_URL}/users/{userID}/'
    response = requests.delete(url)
    if response.status_code == 204:
        return 'Usuario eliminado con éxito.'
    return f'Error al eliminar el usuario: {response.status_code} - {response.text}'

def delete_doctor(medicoID:int):
    url = f'{BASE_URL}/doctors/{medicoID}/'
    response = requests.delete(url)
    if response.status_code == 204:
        return 'Usuario eliminado con éxito.'
    return f'Error al eliminar el usuario: {response.status_code} - {response.text}'

def delete_turno(turnoID:int):
    url = f'{BASE_URL}/shifts/{turnoID}/'
    response = requests.delete(url)
    if response.status_code == 204:
        return 'Usuario eliminado con éxito.'
    return f'Error al eliminar el usuario: {response.status_code} - {response.text}'

def delete_testimony(id:int):
    url = f'{BASE_URL}/testimonials/{id}/'
    response = requests.delete(url)
    if response.status_code == 204:
        return 'Usuario eliminado con éxito.'
    return f'Error al eliminar el usuario: {response.status_code} - {response.text}'

def delete_location(ubicacionID:int):
    url = f'{BASE_URL}/locations/{ubicacionID}/'
    response = requests.delete(url)
    if response.status_code == 204:
        return 'Usuario eliminado con éxito.'
    return f'Error al eliminar el usuario: {response.status_code} - {response.text}'

def delete_department(departamentoID:int):
    url = f'{BASE_URL}/departments/{departamentoID}/'
    response = requests.delete(url)
    if response.status_code == 204:
        return 'Usuario eliminado con éxito.'
    return f'Error al eliminar el usuario: {response.status_code} - {response.text}'

def delete_specialty(especialidadID:int):
    url = f'{BASE_URL}/specialties/{especialidadID}/'
    response = requests.delete(url)
    if response.status_code == 204:
        return 'Usuario eliminado con éxito.'
    return f'Error al eliminar el usuario: {response.status_code} - {response.text}'

def delete_schedule(horarioID:int):
    url = f'{BASE_URL}/schedules/{horarioID}/'
    response = requests.delete(url)
    if response.status_code == 204:
        return 'Usuario eliminado con éxito.'
    return f'Error al eliminar el usuario: {response.status_code} - {response.text}'

def delete_appointment(citaID:int):
    url = f'{BASE_URL}/appointments/{citaID}/'
    response = requests.delete(url)
    if response.status_code == 204:
        return 'Usuario eliminado con éxito.'
    return f'Error al eliminar el usuario: {response.status_code} - {response.text}'