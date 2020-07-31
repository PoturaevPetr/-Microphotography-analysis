#Загрузка фоторграфий поверхности материала, выполненных с помощью оптического микроскопа Олимпус
import matplotlib.pyplot as plt
import numpy as np
imag = plt.imread('F2_x20_1_tsentr_verkhniy_ryadom_s_Cu.tif')
print(imag)
plt.imshow(imag)

#Перевод трехмерного массива в двумерный, где срезаны данные отвечающие цвету
imag = np.dot(imag[...,:3],[1,1,1])
print(imag)
plt.imshow(imag)
plt.colorbar()

# Очевидно, что границы между зернами сплава отображены как темные пигменеты (исходя из оригиналного цвета)
# тогда для более высокой контрастности изображения имеет смысл избавится от цвета границ зерен
for i in imag:
    for j in range(len(i)):
        if i[j] < 350:  # все что ниже 350 (RGB), в единицу (примерно)
            i[j] = 1

print(imag)
plt.imshow(imag)
plt.colorbar()


#Трехмерное избражение поверхности, выполненное с учетом данных цвета (RGB)
#Здесь оси Х и У это шейпы массива, а Z - значечения для цвета
# Как итог, имеется трехмерное изображение поверхности (разуммется условное, т.к. все опираеется на данные отвечающие цвету), лишенные некоторого физического фундумента
#Отмечу, что такое изображение странным образом напоминает изображения которые обычно получаются на профилометре
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

import matplotlib.pyplot as plt
import numpy as np
imag = plt.imread('F2_x20_1_tsentr_verkhniy_ryadom_s_Cu.tif')
imag = np.dot(imag[...,:3],[1,1,1])

fig = plt.figure(figsize = (20, 5))
ax = fig.gca(projection='3d')

x = np.arange(0, imag.shape[1], 1)
y = np.arange(0, imag.shape[0], 1)

X, Y = np.meshgrid(x, y)

imag = np.array(imag)

ax.plot_surface(X, Y, imag, cmap='viridis')



#Выполнен поворот на определенное значение угла (в данном случае на 10 градусов по часовой стрелке, и наклонено на 60 градусов)
fig = plt.figure(figsize = (20, 5))
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, imag, cmap='viridis')
ax.view_init(50, -10)  # поворот




#Гистрграмма по цветам для оригинальных изображений (использовался сторонний модуль skimage)
#с помощью данной функции предполагалось некоторым образом, получить количество зерен.
#Однако, по всей видимости такой подход приводит в тупик
from skimage import data
from skimage.exposure import histogram
imag = plt.imread('F2_x20_1_tsentr_verkhniy_ryadom_s_Cu.tif')
hist, hist_centers = histogram(imag)
fig, ax = plt.subplots(1,2, figsize = (8, 3))
ax[0].plot(hist_centers, hist)
ax[1].imshow(imag)


#Гистрграмма по цветам для изображений избавлеенных от цвета
from skimage import data
from skimage.exposure import histogram
imag = plt.imread('F2_x20_1_tsentr_verkhniy_ryadom_s_Cu.tif')
imag = np.dot(imag[...,:3],[1,1,1])
hist, hist_centers = histogram(imag)
fig, ax = plt.subplots(1,2, figsize = (8, 3))
ax[0].plot(hist_centers, hist)
ax[1].imshow(imag)