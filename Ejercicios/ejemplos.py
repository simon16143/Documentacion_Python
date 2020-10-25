
"""
#FCFS
process = int(input("Ingrese el número de procesos: "))
process_time = []
wait_time = []
counter = 0
wait_time_average = 0
response_time = []
response_time_average = 0
for i in range(process):
  process_time.append(int(input("Ingrese los tiempos de cada proceso: ")))
  wait_time.append(counter)
  counter+=process_time[i]
  wait_time_average += wait_time[i]
  response_time.append(counter)
  response_time_average += response_time[i]
print(wait_time,wait_time_average/process,response_time_average/process)
"""
"""    
#nested dictionary
car = {
        'ferrari':{
              'nombre' : 'ferrari',
              'modelo' : 'AX3000',
              'año' : '2005'
              'cilindraje' : 380}

         'ford':{
              'nombre' : 'Ford',
              'modelo' : 'Power2000',
              'año' : '2016',
              'cilindraje': 400} 
                             
                   }
print(car)
"""
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

while swapped:
 swapped = False
 for i in range(len(process_time)-1):
    if process_time[i]>process_time[i+1]:
       process_time[i],process_time[i+1] = process_time[i+1],process_time[i]
       swapped = True
for i in process_time:
    wait_time_average += counter
    wait_time.append(counter)
    counter+=i
    

    
print(wait_time,wait_time_average/process,response_time_average/process)  


















