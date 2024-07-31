import pydantic
from typing import Any, List, Dict
from pandas import DataFrame
from tabulate import tabulate
from colorama import init, Fore, Style

class CitaValidationError(Exception):
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

class Cita(pydantic.BaseModel):
    citaID: int
    medicoID: int
    horarioID: int
    departamentoID: int
    motivo: str
    estado: str
    
    @classmethod
    def validate_cita(cls, cita: Dict[str, Any]):
        try:
            return cls(**cita)
        except pydantic.ValidationError as e:
            for error in e.errors():
                field = error['loc'][0]
                message = error['msg']
                value = cita.get(field, None)
                raise CitaValidationError(field, message, value)

    def tabla(self):
        df = DataFrame([self.dict()])
        headers = [Fore.CYAN + header.upper() + Style.RESET_ALL for header in df.columns]
        table = tabulate(df, headers=headers, tablefmt='pretty')
        print(table)
    
    @classmethod
    def tabla_citas(cls, citas_obj: List[Any]):
        data = {
            "citaID": [],
            "medicoID": [],
            "horarioID": [],
            "departamentoID": [],
            "motivo": [],
            "estado": []
        }
        for cita_obj in citas_obj:
            data['citaID'].append(cita_obj.citaID)
            data['medicoID'].append(cita_obj.medicoID)
            data['horarioID'].append(cita_obj.horarioID)
            data['departamentoID'].append(cita_obj.departamentoID)
            data['motivo'].append(cita_obj.motivo)
            data['estado'].append(cita_obj.estado)
        
        df = DataFrame(data)
        df.columns = [Fore.CYAN + header.upper() + Style.RESET_ALL for header in df.columns]
        df.index = [Fore.CYAN + str(i) + Style.RESET_ALL for i in df.index]
        tabla = tabulate(df, headers='keys', tablefmt='psql')
        return tabla