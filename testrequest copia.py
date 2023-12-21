import requests
import getpass


token_endpoint = "http://192.168.1.12:8000/auth/jwt/create/"

usuario = "tu_usuario"
contrasena = "tu_contraseña"

datos_token = {
    "username": input('username: '),
    "password": getpass.getpass('password: '),
}

response = requests.post(token_endpoint, data=datos_token)

if response.status_code == 200:
    token_jwt = response.json().get("access")
    print(f"Token JWT obtenido: {token_jwt}")

    url = "http://192.168.1.12:8000/api/nextmatches"

    headers = {
        "Authorization": f"Bearer {token_jwt}",
        "Content-Type": "application/json",
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("Solicitud exitosa!")
        print(response.json())
    else:
        print(f"Error en la solicitud protegida: {response.status_code}")
        print(response.text)
else:
    print(f"Error al obtener el token: {response.status_code}")
    print(response.text)
