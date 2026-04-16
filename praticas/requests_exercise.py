import urllib.request
import json, os
os.system("cls")

api = "https://jsonplaceholder.typicode.com/posts/"

def show_data_api (id_data, api):
    """
    Nos permite seleccionar los datos de la api que deseemos ver, para una mayor clarida
    al momento de mostrar en la consola

    """
    # id_data = 0

    try:
        with urllib.request.urlopen(api) as respuesta:
            data = respuesta.read()
            data_json = json.loads(data.decode('utf-8'))

        for dato in data_json:
            if dato["id"] == id_data:
                print(f"\n Post #{dato['id']}")
                print(f"Usuario: {dato['userId']}")
                print(f"Título: {dato['title']}")
                print(f"Contenido: {dato['body']}")
                return
            
        print("ID no encontrado..")
        
    except urllib.error.URLError as e:
        print(f"Error en la solicitud en: {e}")

print("=== Ejemplo de como consumir un API ===")

post_id = int(
    input("Por favor ingrese un numero de id valido, para obtener la informacion necesaria: \n")
)
show_data_api(post_id, api)

# if dato_obtenido:
#     print(dato_obtenido)

