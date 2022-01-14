import numpy as np
import random
import matplotlib.pyplot as plt



T = 0.8
x = int(input(' Введите размер матрицы x = '))
k = [1, -1]
C_N = range(x)
matrix = np.zeros((x, x))
for i in range(x):
    for j in range(x):
        matrix[i, j] = random.choice(k)
print(matrix)  # создание матрицы заполненной 1 и -1



mas = []
mas = matrix.copy()
for m in range(int(input(' Введите кол-во итераций m = '))):
    Sum = Sum1 = 0
    for q in range(x):
        for n in range(x):
            Sum += matrix[q][n] * matrix[q][n - 1] + matrix[q - 1][n] * matrix[q][n]  # сумма попарных произведений 1 
            
    mas1 = []
    mas1 = matrix.copy()
    mas1[random.choice(C_N)][random.choice(C_N)] *= -1
    for g in range(x):
        for h in range(x):
            Sum1 += mas1[g][h] * mas1[g][h - 1] + mas1[g - 1][h] * mas1[g][h]  # сумма попарных произведений 2
            
    
      


    delE = (Sum - Sum1) * -1 # Дельта Е   
    if delE <= 0:
        matrix = mas1.copy()
        mas = matrix.copy()
    else:        
        P = random.uniform(0, 1)
        W = np.exp(-delE/T)
        if P <= W:
            mas = matrix.copy()
        else:
            matrix = mas.copy()
            
            
            
    #print(matrix) # вывод матрицы
    
    
    
    plt.clf()
    plt.imshow(matrix)
    plt.draw()
    plt.show()
    plt.gcf().canvas.flush_events()
plt.ioff() 
# вывод картинки
    
    

    