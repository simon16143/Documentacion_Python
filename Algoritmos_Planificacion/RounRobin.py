#Round Robin (Algoritmo de planificacion Apropiativo "Premptive")
process = int(input("Ingrese el número de procesos: "))
lst = []
cpu = []
watch = 30
swapped = True
counter = 0
#Funcion para obtener los tiempos de los procesos ingresados
def process_time(process,lst):
    for i in range(process):
        lst.append(int(input("Ingrese los tiempos de proceso: ")))

#Funcion planificador de procesos,pasa los procesos a segundos y le otorga un tiempo de reloj de 30 Seg
def planner(lst,watch,swapped,counter):
    #For para obtener el value del elemento ingresado a la lista de procesos, paso valores a seg
    for key,value in enumerate(lst):
        value = value * 60
        cpu.append(value)
    #Accedo a proceso y resto 30seg de tiempo de reloj / quito el procesador y se lo doy a otro proceso
    while swapped:
       swapped = False 
       for i in range(len(cpu)):
         if cpu[i]>0:
            cpu[i] = cpu[i] - watch
            swapped = True
            counter+=1

#Llamado de Funcione#Llamado de Funciones
print("Estado de los procesos", cpu,"ráfaga número:",counter,sep="")
process_time(process,lst)
planner(lst,watch,swapped,counter)            
             
