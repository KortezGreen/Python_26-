import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd

#Zad 1 + 2

# x = np.arange(1, 21)
# y = 1/x
# plt.plot(x, y, 'g>', label='f(x)=1/x', linestyle=':')
# plt.axis(([0,20,0,1]))
# plt.title('Wykres funkcji f(x) dla x [1, 20]')
# plt.ylabel("f(x)")
# plt.xlabel("x")
# plt.legend()
# plt.show()

#Zad 2

# x = np.arange(0, 30, 0.1)
# y = np.sin(x)
# z = np.cos(x)
# plt.plot(x, y, label='sin(x)')
# plt.plot(x, z, label='cos(x)')
# plt.title('Wykres funkcji sin(x) i cos(x)')
# plt.ylabel("Funkcje trygonometryczne")
# plt.xlabel("x")
# plt.legend()
# plt.show()

#zad 4

# x = np.arange(0, 30, 0.1)
# y = np.sin(x)
# z = np.sin(x)
# plt.plot(x, y+1, label='sin(x)')
# plt.plot(x, (z+1)*-1, label='sin(x)')
#
# plt.xlabel("x")
# plt.ylabel("sin(x)")
# plt.title('Wykres sin(x), sin(x)')
#
# plt.legend()
# plt.show()

#zad 5

# df = pd.read_csv('iris.data', header=None)
# print(df.head())
#
# plt.scatter(x=df[0], y=df[1], s=abs(df[0]-df[1])*5, c=df[0], cmap='viridis')
# plt.xlabel('sepal length')
# plt.ylabel('sepal width')
# plt.show()

#zad 6

df = pd.read_excel("imiona.xlsx")

plec_suma = df.groupby('Plec')['Liczba'].sum()

kobiety = df[df['Plec'] == 'K'].groupby('Rok')['Liczba'].sum()
mezczyzni = df[df['Plec'] == 'M'].groupby('Rok')['Liczba'].sum()

rocznie_suma = df.groupby('Rok')['Liczba'].sum()

fig, ax = plt.subplots(1, 3, figsize=(18, 5))

ax[0].bar(plec_suma.index, plec_suma.values, color=['red', 'green'])
ax[0].set_ylabel('Liczba')
ax[0].set_xlabel('Rok')

ax[1].plot(kobiety.index, kobiety.values, label='Kobiety', color='red')
ax[1].plot(mezczyzni.index, mezczyzni.values, label='Mężczyźni', color='green')
ax[1].legend()

ax[2].bar(rocznie_suma.index, rocznie_suma.values, color='blue')


plt.tight_layout()
plt.show()
