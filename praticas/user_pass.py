import re, os
os.system("cls")

# Ejercicio que verificara si un correo y una contraseña ingresada por el usuario son validas

def check_user (email):
    """
    Valida el correo ingresado por el usuario
    """
    pattern = r"[\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,}"

    match = re.fullmatch (pattern, email)
    if match:
        print("El correo ingresado es valido")
    else:
        print("El correo NO es valido, ingreselo nuevamente")

    return match
    
def check_password (password):
    """
    Valida la contrasena ingresada por el usuario
    """
    pattern = r"^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%&*])[\w.!@#$%&*-]{8,}$"
    match = re.fullmatch(pattern, password)
    if match:
        print("La contraseña es valida")
    else:
        print("La contraseña NO es valida, intentalo nuevamente")

    return match

while True:
    print("=== VALIDADOR DE CORREO Y CONTRASEÑA ===")

    # Validar correo
    while True:
        correo = input("Por favor ingrese su correo electrónico:\n ")
        user = check_user(correo)
        # si es correcto pasa al otro loop interno
        if user:
            break

    # Validar contraseña
    while True:
        contrasena = input(
            "Por favor ingrese una contraseña válida.\n"
            "Debe tener una mayúscula,\n"
            "un número, un carácter especial,\n"
            "sin espacios y mínimo 8 caracteres:\n "
        )

        password = check_password(contrasena)
        # sale del loop interno ya que valido que es correcto
        if password:
            break
    # Cuando ambos ya son correctos sale del ciclo que controla el programa y termina la ejecucion
    print("El correo y la contraseña son válidos, hasta pronto... 👋")
    break
