import pydantic
from typing import (Any, List, Tuple, Optional)
from pandas import DataFrame
from tabulate import tabulate
from colorama import (init, Fore, Back, Style)
import pydantic


init(autoreset=True)

class UserValidationError(Exception):
    def __init__(self, field: List[str], message: str, data: dict = None):
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

class User(pydantic.BaseModel):
    userID: int
    dni: str
    nombre: str
    apellido: str
    fecha_nacimiento: Optional[str]
    email: Optional[str]
    telefono: Optional[str]
    contraseña: str
    is_active: bool
    date_joined: str
    last_login: Optional[str]
    last_logout: Optional[str]
    imagen: Optional[str]

    @classmethod
    def validate_user(cls, user: dict):
        try:
            return cls(**user)
        except pydantic.ValidationError as e:
            for error in e.errors():
                field = [error['loc'][0]]
                message = error['msg']
                raise UserValidationError(field, message, user)
    
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
    def data_frame_users(cls, users_obj: List[Any]):
        data = {
            "userID": [],
            "dni": [],
            "nombre": [],
            "apellido": [],
            "fecha_nacimiento": [],
            "email": [],
            "telefono": [],
            "contraseña": [],
            "is_active": [],
            "date_joined": [],
            "last_login": [],
            "last_logout": [],
            "imagen": []
        }
        for user_obj in users_obj:
            data['userID'].append(user_obj.userID)
            data['dni'].append(user_obj.dni)
            data['nombre'].append(user_obj.nombre)
            data['apellido'].append(user_obj.apellido)
            data['fecha_nacimiento'].append(user_obj.fecha_nacimiento)
            data['email'].append(user_obj.email)
            data['telefono'].append(user_obj.telefono)
            data['contraseña'].append(user_obj.contraseña)
            data['is_active'].append(user_obj.is_active)
            data['date_joined'].append(user_obj.date_joined)
            data['last_login'].append(user_obj.last_login)
            data['last_logout'].append(user_obj.last_logout)
            data['imagen'].append(user_obj.imagen)
        data = DataFrame(data)
        return data


    @classmethod
    def tabla_users(cls, users_obj: List[Any]):
        data = cls.data_frame_users(users_obj=users_obj)
        data.columns = [Fore.CYAN + header.upper() + Style.RESET_ALL for header in data.columns]
        data.index = [Fore.CYAN + str(i) + Style.RESET_ALL for i in data.index]
        tabla = tabulate(data, headers='keys', tablefmt='psql')
        return tabla