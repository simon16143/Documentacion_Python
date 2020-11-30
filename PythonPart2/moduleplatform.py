#module platform me permite obtener informacion del sistema operativo
import platform
print(platform.platform())
print(platform.machine())
#El metodo processor() me permite obtener informaciòn sobre mi procesador
print(platform.processor())
print(platform.system())
print(platform.version())
#Tambien podemos utilizar el mòdulo platform para ver la version de python  y su implementaciòn
print(platform.python_implementation())
print(platform.python_version_tuple())
