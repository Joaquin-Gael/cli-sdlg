from components.models.user import (User, UserValidationError)
from components.models.turno import (Turno, TurnoValidationError)
from typing import (Any, Dict, List)
from colorama import (init, Fore, Style)
import faker as fk
import os

init(autoreset=True)

if __name__ == '__main__':
    os.system('clear')

    fake = fk.Faker()

    def generar_usuario_valido() -> Dict[str, Any]:
        return {
            "id": fake.random_int(min=1, max=1000),
            "DNI": fake.random_int(min=10000000, max=99999999),
            "name": fake.first_name(),
            "lastname": fake.last_name(),
            "username": fake.user_name(),
            "email": fake.email(),
            "password": fake.password(),
            "phone": fake.phone_number()
        }

    def generar_usuario_invalido() -> Dict[str, Any]:
        user_data = generar_usuario_valido()
        user_data["DNI"] = "invalid-DNI"
        user_data["email"] = "invalid-email"
        return user_data

    def generar_usuarios(cantidad: int) -> (List[Dict[str, Any]], List[Dict[str, Any]]):
        valid_users = [generar_usuario_valido() for _ in range(cantidad)]
        invalid_users = [generar_usuario_invalido() for _ in range(cantidad)]
        return valid_users, invalid_users

    cantidad_usuarios = 5
    valid_users_data, invalid_users_data = generar_usuarios(cantidad_usuarios)

    valid_users = []
    invalid_users = []

    for user_data in valid_users_data:
        try:
            user = User.validate_user(user_data)
            valid_users.append(user)
        except UserValidationError as e:
            print(e)

    for user_data in invalid_users_data:
        try:
            user = User.validate_user(user_data)
            invalid_users.append(user)
        except UserValidationError as e:
            print(e)

    if valid_users:
        print(User.tabla_users(valid_users))

    if invalid_users:
        print(Fore.RED + "Usuarios inválidos no pueden ser mostrados en la tabla.")

    def generar_turno_fake(id: int) -> Dict[str, Any]:
        return {
            "id": id,
            "userID": fake.random_int(min=1, max=1000),
            "citaID": fake.random_int(min=1, max=1000),
            "medicoID": fake.random_int(min=1, max=1000),
            "motive": fake.sentence(nb_words=3),
            "state": fake.random_element(elements=("Pendiente", "Confirmado", "Cancelado")),
            "fecha": fake.date(pattern="%Y-%m-%d"),
            "fecha_creacion": fake.date(pattern="%Y-%m-%d")
        }

    turnos_data = [generar_turno_fake(i) for i in range(1, 30)]
    turnos = []

    for turno_data in turnos_data:
        try:
            turno = Turno.validate_turno(turno_data)
            turnos.append(turno)
        except TurnoValidationError as e:
            print(e)

    if turnos:
        print(Turno.tabla_turnos(turnos))