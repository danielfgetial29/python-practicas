import requests, os


os.system("cls")

# Ejemplo simple de como puedo obtener datos de un servicio

url = "https://jsonplaceholder.typicode.com/posts/"

respuesta = requests.get(url)# obtengo la respuesta usando request.get() y dentro del parentesis llamo a servicio que estoy utilizando

data = respuesta.json() # utilizo .json() para obtener los datos en ese formato

# Manera simple de recorer todos los datos que contiene la url (servicio)
# for d in data:
#     print(d)
#     print("-------------------------------------------------------")

# print("=== Ejemplo de mostrar los datos que deseemos ===")
# for d in data[:2]:
#     print(f"Mostrar solo los titulos del arreglo: {d['title'].title()}")
#     print("-----------")

# peticcion GET
print("=== GET ==")
api_url = 'https://www.google.com/'
resp = requests.get(api_url)
print(resp.status_code)

# peticiones POST
print("=== POST ==")
auth_data = {"title": "foo","body": "bar","userId": 1}
resp = requests.post(url, json=auth_data)
print(resp.status_code)

# Peticiones POST envueltas en un try para manejar los errores
try:
    auth_data = {"title": "foo","body": "bar","userId": 1}
    resp = requests.post(url, json=auth_data)
    print(resp.status_code)
except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud {e}")
