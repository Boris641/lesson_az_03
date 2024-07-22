import numpy as np
import matplotlib.pyplot as plt



random_array = np.random.rand(5)  # массив из 5 случайных чисел
print(random_array)

x = random_array
y = x

plt.scatter(x, y)
plt.xlabel("ось Х")
plt.ylabel("ось Y")
plt.title("Тестовая диаграмма рассеяния")

plt.show()

