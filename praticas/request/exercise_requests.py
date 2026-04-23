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

def show_data_api(id_data, api):
    """
    Traer toda la data de un id ingresado
    """
    try:
        with requests.get(api) as resp:
            data = resp.json()

            for d in data:
                if d["id"] == id_data:
                    print(f"\n Post #{d['id']}")
                    print(f"Usuario: {d['userId']}")
                    print(f"Título: {d['title']}")
                    print(f"Contenido: {d['body']}")
                    return
            print("ID no encontrad...")
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud {e}")

post_id = int(
    input("Por favor ingrese un numero de id valido, para obtener la informacion necesaria: \n")
)
show_data_api(post_id, url)

# Peticiones POST envueltas en un try para manejar los errores
try:
    auth_data = {"title": "foo","body": "bar","userId": 1}
    resp = requests.post(url, json=auth_data)
    print(resp.status_code)
except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud {e}")
