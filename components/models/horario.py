import pydantic
from typing import (Any, List, Dict)
from pandas import DataFrame
from tabulate import tabulate
from colorama import (init, Fore, Style)
import pydantic

init(autoreset=True)

class HorarioMedicoValidationError(Exception):
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



class HorarioMedico(pydantic.BaseModel):
    horarioID: int
    medicoID: int
    dia: str
    hora_inicio: str
    hora_fin: str
    especialidadID: int
    departamentoID: int
    
    @classmethod
    def validate_horario_medico(cls, horario_medico: Dict[str, Any]):
        try:
            return cls(**horario_medico)
        except pydantic.ValidationError as e:
            for error in e.errors():
                field = error['loc'][0]
                message = error['msg']
                value = horario_medico.get(field, None)
                raise HorarioMedicoValidationError(field, message, value)

    def tabla(self):
        df = DataFrame([self.dict()])
        headers = [Fore.CYAN + header.upper() + Style.RESET_ALL for header in df.columns]
        table = tabulate(df, headers=headers, tablefmt='pretty')
        print(table)
    
    @classmethod
    def tabla_horarios_medicos(cls, horarios_medicos_obj: List[Any]):
        data = {
            "horarioID": [],
            "medicoID": [],
            "dia": [],
            "hora_inicio": [],
            "hora_fin": [],
            "especialidadID": [],
            "departamentoID": []
        }
        for horario_medico_obj in horarios_medicos_obj:
            data['horarioID'].append(horario_medico_obj.horarioID)
            data['medicoID'].append(horario_medico_obj.medicoID)
            data['dia'].append(horario_medico_obj.dia)
            data['hora_inicio'].append(horario_medico_obj.hora_inicio)
            data['hora_fin'].append(horario_medico_obj.hora_fin)
            data['especialidadID'].append(horario_medico_obj.especialidadID)
            data['departamentoID'].append(horario_medico_obj.departamentoID)
        
        df = DataFrame(data)
        df.columns = [Fore.CYAN + header.upper() + Style.RESET_ALL for header in df.columns]
        df.index = [Fore.CYAN + str(i) + Style.RESET_ALL for i in df.index]
        tabla = tabulate(df, headers='keys', tablefmt='psql')
        return tabla