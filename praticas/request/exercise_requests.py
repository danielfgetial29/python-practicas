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

# ejerccio con una funcion pero esta vez utilizando requests

def show_data_api(id_data):
    """
    Trae todos los datos de un id especifico
    """
    try:
        url = f"https://jsonplaceholder.typicode.com/posts/{id_data}"
        resp = requests.get(url)
        resp.raise_for_status()

        data = resp.json()

        print(f"\n📌 Post #{data['id']}")
        print(f"👤 Usuario: {data['userId']}")
        print(f"📝 Título: {data['title']}")
        print(f"📄 Contenido: {data['body']}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error: {e}")


post_id = int(
    input("Por favor ingrese un numero de id valido, para obtener la informacion necesaria: \n")
)
show_data_api(post_id)

# Peticiones POST envueltas en un try para manejar los errores
try:
    auth_data = {"title": "foo","body": "bar","userId": 1}
    resp = requests.post(url, json=auth_data)
    print(resp.status_code)
except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud {e}")
