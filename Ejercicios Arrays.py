import numpy as np, random, os
os.system('cls')

arr = np.empty([3,3], dtype = int)
for f in range(3):
    for c in range(3):
        arr[f][c] = np.random.randint(0,100)

print('Matriz\n',arr)

prom =  arr.sum()/arr.size
print(f'suma {arr.sum()}\npromedio {prom}\ntamaño {arr.size}\ndimensiones {arr.ndim}\nmayor {arr.max()}')
print(f'menor {arr.min()}\ndiagonal {arr.diagonal()}')

arr2 = np.zeros((3,3), int)
np.fill_diagonal(arr2,(range(1,4)))
print(arr2)

#prueba de cosas

print('Lino')