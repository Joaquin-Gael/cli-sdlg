from components.models.user import (User, UserValidationError)
import faker as fk
import os

if __name__ == '__main__':
    os.system('clear')
    
    fake = fk.Faker()
    
    valid_user_data = {
        "id": fake.random_int(min=1, max=1000),
        "DNI": fake.random_int(min=10000000, max=99999999),
        "name": fake.first_name(),
        "lastname": fake.last_name(),
        "username": fake.user_name(),
        "email": fake.email(),
        "password": fake.password(),
        "phone": fake.phone_number()
    }
    
    invalid_user_data = valid_user_data.copy()
    invalid_user_data["DNI"] = "invalid-DNI"
    invalid_user_data["email"] = "invalid-email"
    
    try:
        valid_user = User.validate_user(valid_user_data)
        print(valid_user.tabla())
    except UserValidationError as err:
        print(f"{err}")

    # Probar con datos inválidos
    try:
        invalid_user = User.validate_user(invalid_user_data)
        print(invalid_user.tabla())
    except UserValidationError as err:
        print(f"{err}")