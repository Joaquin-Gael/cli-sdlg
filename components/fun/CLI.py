from components.API import (GET, POST)
from components.models.user import (User, UserValidationError)
from components.models.turno import (Turno, TurnoValidationError)
import pandas as pd
from tabulate import tabulate
from colorama import (init, Fore, Back, Style)

def get_user_by_id(id:int):
    try:
        url = f"http://127.0.0.1:8000/users/{id}"
        response = GET.user(url)
        if response is not None:
            user_obj = User.validate_user(response)
            return user_obj
    
    except UserValidationError as e:
        print(e)

def get_users_data(query:dict):
    try:
        url = f"http://127.0.0.1:8000/users"
        response = GET.users(url, query)
        if response is not None:
            users_obj = [User.validate_user(user_data) for user_data in response]
            return User.tabla_users(users_obj)
    
    except UserValidationError as e:
        print(e)

def get_turno_by_id(id:int):
    try:
        url = f"http://127.0.0.1:8000/turnos/{id}"
        response = GET.turno(url)
        if response is not None:
            turno_obj = Turno.validate_turno(response)
            return turno_obj
    
    except TurnoValidationError as e:
        print(e)

def get_turnos_data(query:dict):
    try:
        url = f"http://127.0.0.1:8000/turnos"
        response = GET.turnos(url, query)
        if response is not None:
            turnos_obj = [Turno.validate_turno(turno_data) for turno_data in response]
            return Turno.tabla_turnos(turnos_obj)
    
    except TurnoValidationError as e:
        print(e)

if __name__ == '__main__':
    user_data = get_user_by_id(1)
    usesr_data = get_users_data({})
    print(user_data.tabla())