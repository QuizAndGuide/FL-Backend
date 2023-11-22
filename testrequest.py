import requests

token_endpoint = "http://127.0.0.1:8000/auth/jwt/create/"

usuario = "tu_usuario"
contrasena = "tu_contraseña"

datos_token = {
    "username": usuario,
    "password": contrasena,
}

response = requests.post(token_endpoint, data=datos_token)

if response.status_code == 200:
    token_jwt = response.json().get("access")
    print(f"Token JWT obtenido: {token_jwt}")

    url = "http://127.0.0.1:8000/api/"

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
