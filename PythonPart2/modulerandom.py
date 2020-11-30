#Insert module random
#Import module random para numeros pseudoaleatorios
import random
random.seed(0)
for i in range(5):
    print(round(random.random(),2))

#import randrange y randint para obtener valores pseudoaleatorios entre un rango especìfico
from random import randrange, randint

print(randrange(1))
print(randrange(0,20,1))
print(randint(0,2))
#Sample y choice me pemite escoger valores aleatorios de una lista para que estos no se repitan
from random import choice,sample
lst1=[]
for i in range(10):
    lst1.append(random.randint(0,10))
print(lst1)
lst = [1,2,3,4,5,6,7,8,9,10]
print(choice(lst1))
print(sample(lst1,5))
print(sample(lst1,10))


