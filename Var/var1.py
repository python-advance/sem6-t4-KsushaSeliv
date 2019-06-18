import numpy as np
import math
import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv('ex1data1.csv', header=None)
x, y = df[0], df[1]

x1 = list(x)
y1 = list(y)

for i in range(len(y1)):
    if math.isnan(y1[i]):
        y1[i] = 0
    else:
        y1[i] = y1[i]

plt.scatter(x1, y1, c ='green', label = u'Данные из файла')

numpy_x = np.array(x1)
numpy_y = np.array(y1)

x2 = list(range(743))


func1 = np.poly1d(np.polyfit(numpy_x, numpy_y, 2))  #Poly1d.Удобный класс, используемый для инкапсуляции «естественных» операций над полиномами,
                                                     #чтобы указанные операции могли принять свою обычную форму в коде.
plt.plot(x2, func1(x2), label = u'Полином 2-ей степени')
func2 = np.poly1d(np.polyfit(numpy_x, numpy_y, 5))
plt.plot(x2, func2(x2), label = u'Полином 5-ой степени')
func3 = np.poly1d(np.polyfit(numpy_x, numpy_y, 7))
plt.plot(x2, func3(x2), label = u'Полином 7-ой степени')
