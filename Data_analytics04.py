import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


c = pd.read_csv('C:\\Users\\HP\\Desktop\\IRIS.csv')
array = np.array(c)


x_first = array[:50, 0]
y_first = array[:50, 1]

x_second = array[50:100, 0]
y_second = array[50:100, 1]

x_last = array[100:, 0]
y_last = array[100:, 1]


plt.scatter(x_first, y_first, c='red', label='First 50')
plt.scatter(x_second, y_second, c='blue', label='Second 50')
plt.scatter(x_last, y_last, c='green', label='Last 50')


plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('IRIS')


plt.legend()


plt.show()
