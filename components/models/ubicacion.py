import pydantic
from typing import (Any, List, Dict)
from pandas import DataFrame
from tabulate import tabulate
from colorama import (init, Fore, Back, Style)
import pydantic

init(autoreset=True)

class UbicacionValidationError(Exception):
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

class Ubicacion(pydantic.BaseModel):
    ubicacionID: int
    nombre: str
    descripcion: str
    
    @classmethod
    def validate_ubicacion(cls, ubicacion: Dict[str, Any]):
        try:
            return cls(**ubicacion)
        except pydantic.ValidationError as e:
            for error in e.errors():
                field = error['loc'][0]
                message = error['msg']
                value = ubicacion.get(field, None)
                raise UbicacionValidationError(field, message, value)

    def tabla(self):
        df = DataFrame([self.dict()])
        headers = [Fore.CYAN + header.upper() + Style.RESET_ALL for header in df.columns]
        table = tabulate(df, headers=headers, tablefmt='pretty')
        print(table)
    
    @classmethod
    def tabla_ubicaciones(cls, ubicaciones_obj: List[Any]):
        data = {
            "ubicacionID": [],
            "nombre": [],
            "descripcion": []
        }
        for ubicacion_obj in ubicaciones_obj:
            data['ubicacionID'].append(ubicacion_obj.ubicacionID)
            data['nombre'].append(ubicacion_obj.nombre)
            data['descripcion'].append(ubicacion_obj.descripcion)
        
        df = DataFrame(data)
        df.columns = [Fore.CYAN + header.upper() + Style.RESET_ALL for header in df.columns]
        df.index = [Fore.CYAN + str(i) + Style.RESET_ALL for i in df.index]
        tabla = tabulate(df, headers='keys', tablefmt='psql')
        return tabla