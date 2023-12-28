from core.models import User
import requests
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Obtains information about matches in the current round'

    def handle(self, *args, **kwargs):
        def create_user(datos_user):
            create_user_endpoint = "http://192.168.1.12:8000/core/create_user/"
            response = requests.post(create_user_endpoint, data=datos_user)
            return response

        def get_token(datos_user):
            token_endpoint = "http://192.168.1.12:8000/auth/jwt/create/"
            datos_user.pop("email", None)

            response = requests.post(token_endpoint, data=datos_user)
            token_jwt = response.json().get("access")
            print(f"JWT Token obtained: {token_jwt}")

            headers = {
                "Authorization": f"JWT {token_jwt}",
                "Content-Type": "application/json",
            }
            return headers

        def test_auth_endpoints(endpoint, headers):
            print("Headers:", headers)  # Add this line to print headers
            url = f"http://192.168.1.12:8000/api/{endpoint}"
            response = requests.get(url, headers=headers)
            
            print(response.status_code)
            if response.status_code == 200:
                print(f"endpoint: {endpoint} working.")
            # print(response.text)
            # print(response.json())
            print("-------------------------")

        def delete_user(username):
            try:
                user = User.objects.get(username=username)
                user.delete()
                print(f"User '{username}' deleted successfully.")
            except User.DoesNotExist:
                print(f"User '{username}' does not exist.")
            except Exception as e:
                print(f"An error occurred: {e}")

        datos_user = {
            "username": "example",
            "password": "GTRE2F$·",
            "email": "example@example.com"
        }

        # Create User
        create_user_response = create_user(datos_user)
        if create_user_response.status_code == 201:
            print("User successfully created.")
        elif create_user_response.status_code == 400:
            print("User creation failed. User may already exist.")
        else:
            print(f"Failed to create user. Status code: {create_user_response.status_code}")
        create_user_response = create_user(datos_user)
        if create_user_response.status_code == 201:
            print("User successfully created.")
        elif create_user_response.status_code == 400:
            print("User creation failed. User may already exist.")
        else:
            print(f"Failed to create user. Status code: {create_user_response.status_code}")

       # Get Token
        headers = get_token(datos_user)

        # Test Authentication Endpoints
        auth_endpoints = ['nextmatches/', 'lastmatches/', 'goalers/']
        for endpoint in auth_endpoints:
            test_auth_endpoints(endpoint, headers)

        # Delete User
        delete_user(datos_user.get("username"))
