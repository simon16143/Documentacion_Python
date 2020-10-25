 #SJF Shortest Job First

process = int(input("Ingrese el numero de Procesos: "))
process_time = []
counter = 0
counter_two = 0
wait_time = []
wait_time_average = 0
swapped = True
response_time = []
response_time_average = 0
for i in range(process):
    process_time.append(int(input("Ingrese el tiempo de cada proceso: ")))
    counter_two+=process_time[i]
    response_time.append(counter_two)
    response_time_average+=response_time[i]
#Organizo mi lista de procesos de forma ascendente...nota:El método Sort() tambien permite esto..en este caso utilice buble sort
while swapped:
 swapped = False
 for i in range(len(process_time)-1):
    if process_time[i]>process_time[i+1]:
       process_time[i],process_time[i+1] = process_time[i+1],process_time[i]
       swapped = True
#Realizo sumatoria del tiempo de cada proceso para obtener el promedio       
for i in process_time:
    wait_time_average += counter
    wait_time.append(counter)
    counter+=i
    

    
print("El orden de los procesos a atender son:",process_time,"\n","El tiempo de espera es:",wait_time,'\n',"El promedio de tiempo de espera es:",wait_time_average/process,'\n',"El tiempo promedio de respuesta es:",response_time_average/process,sep="")  





