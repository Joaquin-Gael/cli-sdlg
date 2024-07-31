import pydantic
from typing import (Any, List, Tuple)
from pandas import DataFrame
from tabulate import tabulate
from colorama import (init, Fore, Back, Style)

init(autoreset=True)

class UserValidationError(Exception):
    def __init__(self, field: list[str], message: str, data: dict = None):
        self.field = field
        self.message = message
        self.data = data
        if data is not None:
            tabla = DataFrame([self.data])
            for header in tabla.columns:
                if header not in self.field:
                    tabla.rename(columns={header: Fore.CYAN + header.upper() + Style.RESET_ALL}, inplace=True)
                else:
                    tabla.rename(columns={header: Fore.RED + header.upper() + Style.RESET_ALL}, inplace=True)
            tabla.index = [Fore.CYAN + str(i) + Style.RESET_ALL for i in tabla.index]
            data_str = tabulate(tabla, headers='keys', tablefmt='pretty')
            super().__init__(f"Error en el campo {Fore.RED + str([param.upper() for param in self.field]) + Style.RESET_ALL}: {self.message}:\n{data_str}")
        else:
            super().__init__(f"Error en el campo {Fore.RED + str([param.upper() for param in self.field]) + Style.RESET_ALL}: {self.message}")

# Models

class User(pydantic.BaseModel):
    userID: int
    DNI: int
    name: str
    lastname: str
    username: str
    email: pydantic.EmailStr
    password: str
    phone: str
    
    @classmethod
    def validate_user(cls, user:dict):
        try:
            return cls(**user)
        except pydantic.ValidationError as e:
            for error in e.errors():
                field = [error['loc'][0]]
                message = error['msg']
                raise UserValidationError(field, message, user)
            
    @pydantic.field_validator('*', mode='before')
    def check_not_none(cls, v, field):
        if v is None:
            raise ValueError(f'{field.name} must not be None')
        return v
    
    def tabla(self):
        try:
            tabla = DataFrame(self.dict(), index=[0])
            tabla.columns = [Fore.CYAN + header.upper() + Style.RESET_ALL for header in tabla.columns]
            tabla.index = [Fore.CYAN + str(i) + Style.RESET_ALL for i in tabla.index]
            return tabulate(tabla, headers='keys', tablefmt='pretty')
        except pydantic.ValidationError as e:
            for error in e.errors():
                field = [error['loc'][0]]
                message = error['msg']
                raise UserValidationError(field, message)
    
    @classmethod
    def dataFrame_users(cls, users_obj:list[Any]):
        try:
            data = {
                "userID": [],
                "DNI": [],
                "name": [],
                "lastname": [],
                "username": [],
                "email": [],
                "password": [],
                "phone": [],
            }
            for user_obj in users_obj:
                data['userID'].append(user_obj.userID)
                data['DNI'].append(user_obj.DNI)
                data['name'].append(user_obj.name)
                data['lastname'].append(user_obj.lastname)
                data['username'].append(user_obj.username)
                data['email'].append(user_obj.email)
                data['password'].append(user_obj.password)
                data['phone'].append(user_obj.phone)
            data = DataFrame(data)
            return data
        except Exception as err:
            print(f'Error en el dataframe user: {err}')

    @classmethod
    def tabla_users(cls, users_obj:list[Any]):
        data = cls.dataFrame_users(users_obj)
        data.columns = [Fore.CYAN + header.upper() + Style.RESET_ALL for header in data.columns]
        data.index = [Fore.CYAN + str(i) + Style.RESET_ALL for i in data.index]
        tabla = tabulate(data, headers='keys', tablefmt='psql')
        return tabla
