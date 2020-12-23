# =============================================================================
# -*- coding: utf-8 -*-
# Prácticas del Capítulo 3 con NumPy Library
# Created on Wed Dec 23 09:53:53 2020
# @author: LuisAlejandroF
# =============================================================================
import numpy as np # Se importa la libreria
a = np.array ([1,2,3])
print("imprime el tipo de objeto guardado en la variable a")
print(type(a))
print("imprime el tipo tipo de data")
print(a.dtype)
print("devuelve la dimensión de a")
print(a.ndim)
print("devuelve el tamaño de a")
print(a.size)
b = np.array([[1.3, 2.4], [0.3,4.1]])
print (type(b))
print (b.dtype)
print (b.ndim)
print (b.size)
print (b.shape)
print (b.itemsize)
print (b.data)
c = np.array(((1, 2, 3),(4, 5,6)))
print (c)
e = np.array ([(1, 2, 3), [4, 5, 6], (7, 8, 9)])
print (e)
g = np.array ([['a', 'b'], ['c', 'd']])
print (g)
print (g.dtype)
print (g.dtype.name)
f = np.array ([[1, 2, 3],[4, 5, 6]], dtype = complex)
print(f)
h = np.ones ((3, 3))
print (h)
i = np.arange(1,10)
print (1)
j = np.arange(0, 13, 6)
print (j)
k = np.arange(0, 120, 8.4)
print (k)
# Aqui esta las divisiones para las temperaturas del horno
l = np.linspace (0, (60*24), 73)
print (l)
m = np.random.random(3)
print (m)
n= m + 1
print (n)
data = np.genfromtxt('data.txt', delimiter =',', names = True)
print(data)
# =============================================================================
# Seria genial preparar un archivo con datos.txt de 24 h
# de data de producción con las mediciones de cada 20 min
# Entonces al cargar la data extraer la columna que uno
# Quiere graficar y estudiar
# =============================================================================
