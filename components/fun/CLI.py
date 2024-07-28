from components.API import (GET, POST)
from components.models import user
import pandas as pd
from tabulate import tabulate
from colorama import (init, Fore, Back, Style)

def get_user_by_id(id:int):
    try:
        url = f"http://127.0.0.1:8000/users/{id}"
        response = GET.user(url)
        if response is not None:
            user_obj = user.User.validate_user(response)
            return user_obj
    
    except Exception as err:
        print(err)

def get_users_data(data:dict):
    try:
        url = f"http://127.0.0.1:8000/users"
        response = GET.users(url, data)
        if response is not None:
            users_obj = [user.User.validate_user(user_data) for user_data in response]
            data = {
                "id": [],
                "DNI": [],
                "name": [],
                "lastname": [],
                "username": [],
                "email": [],
                "password": [],
                "phone": [],
            }
            for user_obj in users_obj:
                data['id'].append(user_obj.id)
                data['DNI'].append(user_obj.DNI)
                data['name'].append(user_obj.name)
                data['lastname'].append(user_obj.lastname)
                data['username'].append(user_obj.username)
                data['email'].append(user_obj.email)
                data['password'].append(user_obj.password)
                data['phone'].append(user_obj.phone)
            data = pd.DataFrame(data)
            data.columns = [Fore.CYAN + header.upper() + Style.RESET_ALL for header in data.columns]
            data.index = [Fore.CYAN + str(i) + Style.RESET_ALL for i in data.index]
            tabla = tabulate(data, headers='keys', tablefmt='psql')
            return tabla
    
    except Exception as err:
        print(err)

if __name__ == '__main__':
    user_data = get_user_by_id(1)
    usesr_data = get_users_data({})
    print(user_data.tabla())