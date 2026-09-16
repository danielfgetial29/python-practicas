import subprocess
subprocess.run("cls", shell=True)

# ABSTRACCION

class Computadora():
    def __init__(self):
        self._estado = "apagado"

    def encender(self):
        self._estado = "encendido"
        print("El computador esta encendido...")

    def programar(self):
        if self._estado == "apagado":
            self.encender()
        print("El computador esta listo para programar")

mi_pc = Computadora()
mi_pc.programar()

# print(mi_pc._estado)