import requests, json, pydantic
BASE_URL = 'http://127.0.0.1:8000/API'

def user(url: str, data: dict = None):
    """Realiza una solicitud GET al endpoint de usuarios.

    Args:
        url (str): URL base de la API.
        data (dict, optional): Parámetros de consulta. Defaults to None.

    Returns:
        dict: Datos de respuesta de la API.
    """
    try:
        if data is not None:
            query = '&'.join([f"{key}={value}" for key, value in data.items() if value is not None])
            url = f"{url}?{query}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as err:
        print(f"Error: {err}")
        return None

def users(url: str, data: dict = None):
    """Realiza una solicitud GET al endpoint de usuarios.

    Args:
        url (str): URL base de la API.
        data (dict, optional): Parámetros de consulta. Defaults to None.

    Returns:
        dict: Datos de respuesta de la API.
    """
    return user(url, data)


def turno(url: str = BASE_URL, data: dict = None):
    """Realiza una solicitud GET al endpoint de turnos.

    Args:
        url (str): URL base de la API.
        data (dict, optional): Parámetros de consulta. Defaults to None.

    Returns:
        dict: Datos de respuesta de la API.
    """
    try:
        if data is not None:
            query = '&'.join([f"{key}={value}" for key, value in data.items() if value is not None])
            url = f"{url}/shifts/?{query}"
        else:
            url = f"{url}/shifts/"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as err:
        print(f"Error: {err}")
        return None

def turnos(url: str = BASE_URL, data: dict = None):
    """Realiza una solicitud GET al endpoint de turnos.

    Args:
        url (str): URL base de la API.
        data (dict, optional): Parámetros de consulta. Defaults to None.

    Returns:
        dict: Datos de respuesta de la API.
    """
    return turno(url)

def cita(url: str, data: dict = None):
    """Realiza una solicitud GET al endpoint de turnos.

    Args:
        url (str): URL base de la API.
        data (dict, optional): Parámetros de consulta. Defaults to None.

    Returns:
        dict: Datos de respuesta de la API.
    """
    try:
        if data is not None:
            query = '&'.join([f"{key}={value}" for key, value in data.items() if value is not None])
            url = f"{url}/appointments/?{query}"
        else:
            url = f"{url}/appointments/"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as err:
        print(f"Error: {err}")
        return None
    
def citas(url: str, data: dict = None):
    """Realiza una solicitud GET al endpoint de turnos.

    Args:
        url (str): URL base de la API.
        data (dict, optional): Parámetros de consulta. Defaults to None.

    Returns:
        dict: Datos de respuesta de la API.
    """
    return cita(url, data)

def testimonio(url: str, data: dict = None):
    """Realiza una solicitud GET al endpoint de turnos.

    Args:
        url (str): URL base de la API.
        data (dict, optional): Parámetros de consulta. Defaults to None.

    Returns:
        dict: Datos de respuesta de la API.
    """
    try:
        if data is not None:
            query = '&'.join([f"{key}={value}" for key, value in data.items() if value is not None])
            url = f"{url}/testimonials/?{query}"
        else:
            url = f"{url}/testimonials/"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as err:
        print(f"Error: {err}")
        return None
    
def testimonios(url: str, data: dict = None):
    """Realiza una solicitud GET al endpoint de turnos.

    Args:
        url (str): URL base de la API.
        data (dict, optional): Parámetros de consulta. Defaults to None.

    Returns:
        dict: Datos de respuesta de la API.
    """
    return testimonio(url, data)

def medico(url: str = BASE_URL, data: dict = None):
    """Realiza una solicitud GET al endpoint de turnos.

    Args:
        url (str): URL base de la API.
        data (dict, optional): Parámetros de consulta. Defaults to None.

    Returns:
        dict: Datos de respuesta de la API.
    """
    try:
        if data is not None:
            query = '&'.join([f"{key}={value}" for key, value in data.items() if value is not None])
            url = f"{url}/doctors/?{query}"
        else:
            url = f"{url}/doctors/"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as err:
        print(f"Error: {err}")
        return None
    
def medicos(url: str = BASE_URL, data: dict = None):
    """Realiza una solicitud GET al endpoint de turnos.

    Args:
        url (str): URL base de la API.
        data (dict, optional): Parámetros de consulta. Defaults to None.

    Returns:
        dict: Datos de respuesta de la API.
    """
    return medico(url)

def horario_medico(url: str, data: dict = None):
    """Realiza una solicitud GET al endpoint de turnos.

    Args:
        url (str): URL base de la API.
        data (dict, optional): Parámetros de consulta. Defaults to None.

    Returns:
        dict: Datos de respuesta de la API.
    """
    try:
        if data is not None:
            query = '&'.join([f"{key}={value}" for key, value in data.items() if value is not None])
            url = f"{url}/schedules/?{query}"
        else:
            url = f"{url}/schedules/"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as err:
        print(f"Error: {err}")
        return None
    
def horarios_medicos(url: str, data: dict = None):
    """Realiza una solicitud GET al endpoint de turnos.

    Args:
        url (str): URL base de la API.
        data (dict, optional): Parámetros de consulta. Defaults to None.

    Returns:
        dict: Datos de respuesta de la API.
    """
    return horario_medico(url, data)

def ubicacion(url: str, data: dict = None):
    """Realiza una solicitud GET al endpoint de turnos.

    Args:
        url (str): URL base de la API.
        data (dict, optional): Parámetros de consulta. Defaults to None.

    Returns:
        dict: Datos de respuesta de la API.
    """
    try:
        if data is not None:
            query = '&'.join([f"{key}={value}" for key, value in data.items() if value is not None])
            url = f"{url}/locations/?{query}"
        else:
            url = f"{url}/locations/"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as err:
        print(f"Error: {err}")
        return None
    
def ubicaciones(url: str, data: dict = None):
    """Realiza una solicitud GET al endpoint de turnos.

    Args:
        url (str): URL base de la API.
        data (dict, optional): Parámetros de consulta. Defaults to None.

    Returns:
        dict: Datos de respuesta de la API.
    """
    return ubicacion(url, data)

def departamento(url: str, data: dict = None):
    """Realiza una solicitud GET al endpoint de turnos.

    Args:
        url (str): URL base de la API.
        data (dict, optional): Parámetros de consulta. Defaults to None.

    Returns:
        dict: Datos de respuesta de la API.
    """
    try:
        if data is not None:
            query = '&'.join([f"{key}={value}" for key, value in data.items() if value is not None])
            url = f"{url}/departments/?{query}"
        else:
            url = f"{url}/departments/"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as err:
        print(f"Error: {err}")
        return None
    
def departamentos(url: str, data: dict = None):
    """Realiza una solicitud GET al endpoint de turnos.

    Args:
        url (str): URL base de la API.
        data (dict, optional): Parámetros de consulta. Defaults to None.

    Returns:
        dict: Datos de respuesta de la API.
    """
    return departamento(url, data)

def especialidad(url: str = BASE_URL, data: dict = None):
    """Realiza una solicitud GET al endpoint de turnos.

    Args:
        url (str): URL base de la API.
        data (dict, optional): Parámetros de consulta. Defaults to None.

    Returns:
        dict: Datos de respuesta de la API.
    """
    try:
        if data is not None:
            query = '&'.join([f"{key}={value}" for key, value in data.items() if value is not None])
            url = f"{url}/specialties/?{query}"
        else:
            url = f"{url}/specialties/"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as err:
        print(f"Error: {err}")
        return None
    
def especialidades(url: str = BASE_URL, data: dict = None):
    """Realiza una solicitud GET al endpoint de turnos.

    Args:
        url (str): URL base de la API.
        data (dict, optional): Parámetros de consulta. Defaults to None.

    Returns:
        dict: Datos de respuesta de la API.
    """
    return especialidad(url, data)






