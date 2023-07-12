import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
c = pd.read_csv('C:\\Users\\HP\\Desktop\\IRIS.csv')
e = np.array(c)

print(e)
a=e[:,1]
b=e[:,0]
plt.plot(a,b,'r')
plt.title("IRIS")
plt.xlabel('x')
plt.ylabel('y')