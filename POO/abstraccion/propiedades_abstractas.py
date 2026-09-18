import subprocess
subprocess.run("cls", shell=True)
from abc import ABC, abstractmethod

class Programador(ABC):
        
        @property
        @abstractmethod
        def habilidades(self):
            pass # esta propiedad abstrascta debe ser implementada en las subclases

class JavaDev(Programador):

      @property
      def habilidades(self):
        return "Java"

desarrollador_java = JavaDev()
print(f"Mi habilidad como desarrolador es: {desarrollador_java.habilidades}")