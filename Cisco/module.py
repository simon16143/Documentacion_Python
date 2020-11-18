#Generación de números pseudoaleatorios, la funcion seed es la semilla que permite que siempre se repitan los numeros 0.0 a 1.0
from random import random,seed, randrange,randint
seed(0)

for i in range(5):
    print(random())

print(randrange(0,10,2),end='\t')
print(randrange(0,2))

