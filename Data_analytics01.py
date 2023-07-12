import pandas as pd
import numpy as np
import matplotlib as mt
d = pd.read_excel('C:\\Users\\HP\Desktop\\da - Copy.xlsx')
c = pd.read_csv('C:\\Users\HP\\Desktop\\da - Copy.csv')
print(c)
print(type(c))
print(c.iloc[0])
print(c['Name'])
print(c.tail(2))
e = np.array(c)
print(e)
print(type(e))
print(e[2,0])
print(e[:,1])
print(e[1,:])
print(e[0:2,1:3])
f = np.mean(e[:,-1])
print(f)