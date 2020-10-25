#FCFS
process = int(input("Ingrese el número de procesos: "))
process_time = []
wait_time = []
counter = 0
wait_time_average = 0
response_time = []
response_time_average = 0
#Obtengo los valores de procesos
for i in range(process):
  process_time.append(int(input("Ingrese los tiempos de cada proceso: ")))
  wait_time.append(counter)
  counter+=process_time[i]
  wait_time_average += wait_time[i]
  response_time.append(counter)
  response_time_average += response_time[i]
print("El tiempo de atencion es:",wait_time,'\n',"El tiempo promedio de espera es:",wait_time_average/process,'\n',"El tiempo promedio de respuesta es:",response_time_average/process)

