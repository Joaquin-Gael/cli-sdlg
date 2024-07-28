import requests, json, pydantic
import faker as fk

fake = fk.Faker()

def user(url:str, data:dict = None):
    """_summary_

    Args:
        url (str): Url to send request
        data (dict, optional): Parameters to send. Defaults to None.

    Returns:
        dict: responce data
    """
    try:
        if data is not None:
            query = []
            for key, value in data.items():
                query.append(f"{key}={value}")
            query = "&".join(query)
            url = f"{url}/?{query}"
            print(url)
            #responce = requests.get(url)
        else:
            pass
            #responce = requests.get(url)
        #serialized_data = json.decoder(responce.json())
        fake_responce = {
            "status_code":200,
            "body":{
                "id": fake.random_int(min=1, max=1000),
                "DNI": fake.random_int(min=10000000, max=99999999),
                "name": fake.first_name(),
                "lastname": fake.last_name(),
                "username": fake.user_name(),
                "email": fake.email(),
                "password": fake.password(),
                "phone": fake.phone_number()
            }
        }
        if fake_responce['status_code'] == 200:
            user_data = fake_responce['body']
            return user_data
        else:
            return None
    except Exception as err:
        print(err)

def users(url:str, data:dict = None):
    """_summary_

    Args:
        url (str): Url to send request
        data (dict, optional): Parametes to send. Defaults to None.

    Returns:
        dict: responce data
    """
    try:
        if data is not None:
            query = []
            for key, value in data.items():
                query.append(f"{key}={value}")
            query = "&".join(query)
            url = f"{url}/?{query}"
            print(url)
            #responce = requests.get(url)
        else:
            pass
            #responce = requests.get(url)
        #serialized_data = json.decoder(responce.json())
        fake_responce = {
            "status_code":200,
            "body":[
                {
                    "id": fake.random_int(min=1, max=1000),
                    "DNI": fake.random_int(min=10000000, max=99999999),
                    "name": fake.first_name(),
                    "lastname": fake.last_name(),
                    "username": fake.user_name(),
                    "email": fake.email(),
                    "password": fake.password(),
                    "phone": fake.phone_number()
                },
                {
                    "id": fake.random_int(min=1, max=1000),
                    "DNI": fake.random_int(min=10000000, max=99999999),
                    "name": fake.first_name(),
                    "lastname": fake.last_name(),
                    "username": fake.user_name(),
                    "email": fake.email(),
                    "password": fake.password(),
                    "phone": fake.phone_number()
                },
                {
                    "id": fake.random_int(min=1, max=1000),
                    "DNI": fake.random_int(min=10000000, max=99999999),
                    "name": fake.first_name(),
                    "lastname": fake.last_name(),
                    "username": fake.user_name(),
                    "email": fake.email(),
                    "password": fake.password(),
                    "phone": fake.phone_number()
                }
            ]
        }
        if fake_responce['status_code'] == 200:
            user_data = fake_responce['body']
            return user_data
        else:
            return None
    except Exception as err:
        print(err)