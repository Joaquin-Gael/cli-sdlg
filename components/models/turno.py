import pydantic
from typing import (Any, Dict, List)
from pandas import DataFrame
from tabulate import tabulate
from colorama import (init, Fore, Back, Style)

init(autoreset=True)

class TurnoValidationError(Exception):
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

#Models

class Turno(pydantic.BaseModel):
    id: int
    userID: int
    citaID: int
    medicoID: int
    motive: str
    state: str
    fecha: str
    fecha_creacion: str
    
    @classmethod
    def validate_turno(cls, turno: Dict[str, Any]):
        try:
            return cls(**turno)
        except pydantic.ValidationError as e:
            for error in e.errors():
                field = error['loc'][0]
                message = error['msg']
                value = turno.get(field, None)
                raise TurnoValidationError(field, message, value)

    @pydantic.field_validator('*', mode='before')
    def check_not_none(cls, v, info):
        if v is None:
            raise ValueError(f'{info.field_name} must not be None')
        return v

    def tabla(self):
        df = DataFrame([self.dict()])
        headers = [Fore.CYAN + header + Style.RESET_ALL for header in df.columns]
        table = tabulate(df, headers=headers, tablefmt='pretty')
        print(table)
    
    @classmethod
    def tabla_turnos(cls, turnos_obj: List[Any]):
        data = {
            "id": [],
            "userID": [],
            "citaID": [],
            "medicoID": [],
            "motive": [],
            "state": [],
            "fecha": [],
            "fecha_creacion": [],
        }
        for turno_obj in turnos_obj:
            data['id'].append(turno_obj.id)
            data['userID'].append(turno_obj.userID)
            data['citaID'].append(turno_obj.citaID)
            data['medicoID'].append(turno_obj.medicoID)
            data['motive'].append(turno_obj.motive)
            data['state'].append(turno_obj.state)
            data['fecha'].append(turno_obj.fecha)
            data['fecha_creacion'].append(turno_obj.fecha_creacion)
        
        df = DataFrame(data)
        df.columns = [Fore.CYAN + header.upper() + Style.RESET_ALL for header in df.columns]
        df.index = [Fore.CYAN + str(i) + Style.RESET_ALL for i in df.index]
        tabla = tabulate(df, headers='keys', tablefmt='psql')
        return tabla