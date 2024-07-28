import pydantic
from typing import (Tuple, List)
from pandas import DataFrame
from tabulate import tabulate
from colorama import (init, Fore, Back, Style)

init(autoreset=True)

class UserValidationError(Exception):
    def __init__(self, field:list[str], message:str, data:dict = None):
        self.field = field
        self.message = message
        self.data = data
        if data is not None:
            tabla = DataFrame(self.data, index=[0])
            for header in tabla.columns:
                if header not in self.field:
                    tabla.rename(columns={header: Fore.CYAN + header.upper() + Style.RESET_ALL}, inplace=True)
                else:
                    tabla.rename(columns={header: Fore.RED + header.upper() + Style.RESET_ALL}, inplace=True)
                
            tabla.index = [Fore.CYAN + str(i) + Style.RESET_ALL for i in tabla.index]
            data = tabulate(tabla, headers='keys', tablefmt='pretty')
            super().__init__(f"Error en el campo  {Fore.RED + str([param.upper() for param in self.field if param in self.field]) + Style.RESET_ALL}: {self.message}:\n{data}")
        else:
            super().__init__(f"Error en el campo  {Fore.RED + str([param.upper() for param in self.field if param in self.field]) + Style.RESET_ALL}: {self.message}")

# Models

class User(pydantic.BaseModel):
    id: int
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
