import pydantic
from typing import (Any, List, Dict)
from pandas import DataFrame
from tabulate import tabulate
from colorama import (init, Fore, Style)
import pydantic

init(autoreset=True)

class EspecialidadValidationError(Exception):
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

class Especialidad(pydantic.BaseModel):
    especialidadID: int
    nombre: str
    descripcion: str
    departamentoID: int
    
    @classmethod
    def validate_especialidad(cls, especialidad: Dict[str, Any]):
        try:
            return cls(**especialidad)
        except pydantic.ValidationError as e:
            for error in e.errors():
                field = error['loc'][0]
                message = error['msg']
                value = especialidad.get(field, None)
                raise EspecialidadValidationError(field, message, value)

    def tabla(self):
        df = DataFrame([self.dict()])
        headers = [Fore.CYAN + header.upper() + Style.RESET_ALL for header in df.columns]
        table = tabulate(df, headers=headers, tablefmt='pretty')
        print(table)
    
    @classmethod
    def tabla_especialidades(cls, especialidades_obj: List[Any]):
        data = {
            "especialidadID": [],
            "nombre": [],
            "descripcion": [],
            "departamentoID": []
        }
        for especialidad_obj in especialidades_obj:
            data['especialidadID'].append(especialidad_obj.especialidadID)
            data['nombre'].append(especialidad_obj.nombre)
            data['descripcion'].append(especialidad_obj.descripcion)
            data['departamentoID'].append(especialidad_obj.departamentoID)
        
        df = DataFrame(data)
        df.columns = [Fore.CYAN + header.upper() + Style.RESET_ALL for header in df.columns]
        df.index = [Fore.CYAN + str(i) + Style.RESET_ALL for i in df.index]
        tabla = tabulate(df, headers='keys', tablefmt='psql')
        return tabla