import pydantic
from typing import (Any, List, Dict)
from pandas import DataFrame
from tabulate import tabulate
from colorama import (init, Fore, Style)
import pydantic

init(autoreset=True)

class MedicoValidationError(Exception):
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


class Medico(pydantic.BaseModel):
    medicoID: int
    nombre: str
    apellido: str
    dni: str
    especialidadID: int
    telefono: str
    email: str
    
    @classmethod
    def validate_medico(cls, medico: Dict[str, Any]):
        try:
            return cls(**medico)
        except pydantic.ValidationError as e:
            for error in e.errors():
                field = error['loc'][0]
                message = error['msg']
                value = medico.get(field, None)
                raise MedicoValidationError(field, message, value)

    def tabla(self):
        df = DataFrame([self.dict()])
        headers = [Fore.CYAN + header.upper() + Style.RESET_ALL for header in df.columns]
        table = tabulate(df, headers=headers, tablefmt='pretty')
        print(table)
    
    @classmethod
    def tabla_medicos(cls, medicos_obj: List[Any]):
        data = {
            "medicoID": [],
            "nombre": [],
            "apellido": [],
            "dni": [],
            "especialidadID": [],
            "telefono": [],
            "email": []
        }
        for medico_obj in medicos_obj:
            data['medicoID'].append(medico_obj.medicoID)
            data['nombre'].append(medico_obj.nombre)
            data['apellido'].append(medico_obj.apellido)
            data['dni'].append(medico_obj.dni)
            data['especialidadID'].append(medico_obj.especialidadID)
            data['telefono'].append(medico_obj.telefono)
            data['email'].append(medico_obj.email)
        
        df = DataFrame(data)
        df.columns = [Fore.CYAN + header.upper() + Style.RESET_ALL for header in df.columns]
        df.index = [Fore.CYAN + str(i) + Style.RESET_ALL for i in df.index]
        tabla = tabulate(df, headers='keys', tablefmt='psql')
        return tabla