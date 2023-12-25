import requests

create_user_endpoint = "http://192.168.1.12:8000/core/create_user/"
token_endpoint = "http://192.168.1.12:8000/auth/jwt/create/"



datos_user = {
    "username": "example",
    "password": "GTRE2F$·",
    "email": "example@example.com",
}

response = requests.post(create_user_endpoint, data=datos_user)
print(response.status_code)
response = requests.post(create_user_endpoint, data=datos_user)
print(response.status_code)
datos_token = datos_user.pop("email")
response = requests.post(token_endpoint, data=datos_token)

if response.status_code == 200:
    token_jwt = response.json().get("access")
    print(f"Token JWT obtenido: {token_jwt}")


    headers = {
        "Authorization": f"Bearer {token_jwt}",
        "Content-Type": "application/json",
    }
    auth_endpoints = ['nextmatches/', 'lastmatches/', 'goalers/']
    for endpoint in auth_endpoints:
        url = f"http://192.168.1.12:8000/api/{endpoint}"
        response = requests.get(url, headers=headers)
        print(response.status_code)
        print(response.text)
        print(response.json())
        print("-------------------------")
    response = requests.get(url, headers=headers)

from django.contrib.auth.models import User

def delete_user(username):
    try:
        user = User.objects.get(username=username)
        user.delete()
        print(f"User '{username}' deleted successfully.")
    except User.DoesNotExist:
        print(f"User '{username}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage example
if __name__ == "__main__":
    username_to_delete = 'example'  # Replace with the actual username
    delete_user(username_to_delete)
