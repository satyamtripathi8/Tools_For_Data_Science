import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
c = pd.read_csv('C:\\Users\\HP\\Desktop\\IRIS.csv')
print(c)
print(c.info())
print(c.isnull())
print(c.describe())
print(c.fillna('A'))
