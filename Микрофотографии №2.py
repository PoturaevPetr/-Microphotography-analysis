#для анализа микрофотографий изначально планировалось использовать структуру однослойного переспетрона
#Планировалось что данный пересептрон мог бы делать некоторые выводы о шероховатости поверхности материала
#В перспективе могли бы произовдится рассчеты числа зерен сплава, на единицу площади поверхности
import numpy as np
import os
import matplotlib.pyplot as plt
name = os.listdir(r'C:\Users\User\Микрофотографии')
name_tif = filter(lambda x: x.endswith('.tif'), name)
D = []
Y = []#проблема заключается в том, что не ясно каким образом следует задавать обучающий вектор (истинные значения)
for i in name_tif:
    imag = plt.imread(i)
    imag = np.dot(imag[...,:3],[1,1,1])
    for i in imag:
        for j in range(len(i)):
            if i[j] < 350:
                i[j] = 1
    D.append(imag.flatten())
#w = np.zeros((np.array(D).shape[0], np.array(D).shape[1]))
w =
α = 0.2
β = -0.4
σ = lambda x: 1 if x > 0 else 0


def f(x):
    s = β + np.sum(x * w)
    return σ(s)


def train():
    global w
    _w = w.copy()
    for x, y in zip(D, Y):
        i = np.where(x > 0)
        print(i)
        w[i] += α * (y - f(x)) * x

    return (w != _w).any()


while train():
    print(w)