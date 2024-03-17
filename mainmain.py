# Солдатова Анастасия ИСУ: 409605 Вариант: 5
# Файл: data1.csv Столбцы: 1 от 4 и 16 Формула: x∈(-п;п); y=sin(x)cos(x); z=sin(x)

import time as time
import numpy as np
import math
import matplotlib.pyplot as plt

#Задание №1

# Замер времени перемножения стандартных списков
start_time = time.perf_counter()
a = [np.random.rand() for _ in range(1000000)]
b = [np.random.rand() for _ in range(1000000)]
result_list = [a[i] * b[i] for i in range(1000000)]
end_time = time.perf_counter()
list_time = end_time - start_time

# Замер времени перемножения массивов NumPy
start_time = time.perf_counter()
arr_a = np.random.rand(1000000)
arr_b = np.random.rand(1000000)
result_np = np.multiply(arr_a, arr_b)
end_time = time.perf_counter()
numpy_time = end_time - start_time

#Результат:
print("Время выполнения операции для стандартных списков:", list_time)
print("Время выполнения операции для массивов NumPy:", numpy_time)

#Задание №2

#Создаем три массива: 1. время 2. положение заслонки 3. расход воздуха
time_arr = []
position_arr = []
csmpt_arr = []

#Загрузка данных из файла, разделяет строки файла по разделителю: ";" и добавляет данные в три массива
with open('data1.csv', 'r') as f:
    for line in f:
        res = line.split(';')
        time_arr.append(res[0])
        position_arr.append(res[3])
        csmpt_arr.append(res[15])
    f.close()

#Удаляем первый элемент из каждого массива (Так как первый элемент - название)
for arr in (time_arr, position_arr, csmpt_arr):
    arr.pop(0)

#Преобразуем строки в числа
time = np.array(time_arr, float)
csmpt = np.array(csmpt_arr, float)
position = np.array(position_arr, float)

#Строим графики
plt.title('Положение дроссельной заслонки и массовый расход воздуха в течении времени')
plt.xlabel('Время')
plt.ylabel(f'Положение дроссельной заслонки и массовый расход воздуха (кг/ч)')
plt.plot(np.array(time), np.array(position))
plt.plot(np.array(time), np.array(csmpt))
plt.show()

plt.title('График корреляции')
plt.xlabel('Положение дроссельной заслонки')
plt.ylabel('Массовый расход воздуха (кг/ч)')
plt.plot(position, csmpt, 'o')
plt.show()

#Задание 3

#Создаем массив, который содержит значения от -pi до pi
x = np.linspace(np.pi*(-1), np.pi, 100)

#Вычисляем y и z по формуле, которую нам дали в задании
y = np.zeros(len(x), float)
for i in range(len(x)):
    y[i] = math.sin(x[i]) * math.cos(x[i])

z = np.zeros(len(x), float)
for i in range(len(x)):
    z[i] = math.sin(x[i])

#Строим трехмерный график функции
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(x, y, z)
plt.show()
