#!/usr/bin/python3
# # -*- coding: utf-8 -*-

__author__ = "Sebastián Bórquez González"

import numpy as np


def interpolate_lagrange(x, X, Y):
    """
    interpolate obtiene el valor interpolado 'y' para un 'x' usando
    los puntos conocidos (X,Y) de una funcion f.
    
    Se utiliza la fórmula baricéntrica de Lagrange.
    """
    
    # Para cada j en [0,n]
    # D = X[j] - X[X != X[j]] son las diferencias (xj - xk) para toda k != j
    # w = np.prod(D) es la multiplicatoria de las diferencias
    # luego tomamos su inversa W = w^-1
    w = [np.prod(X[j] - X[X != X[j]]) for j in range(len(X))]
    W = np.power(np.array(w), -1)
    
    # diff = x - X es la diferencia x - xj para cada j en [0, n]
    diff = x - X
    
    # numerador
    # W*Y/diff es calcular (wj * f(xj))/(x - xj) para cada j en [0, n]
    # Luego realizamos la sumatoria entre estos valores
    num = np.sum(W*Y / diff)
    
    # denominador
    # De la misma forma calculamos para el denominador W/diff 
    # equivalente a wj/(x - xj) para cada j en [0, n]
    # y sumamos los valores
    den = np.sum(W / diff)
    
    # finalmente retornamos la division
    return num/den

def interpolate_newton(x, X, Y):
    """
    interpolate obtiene el valor interpolado 'y' para un 'x' usando
    los puntos conocidos (X,Y) de una funcion f.
    
    Se utiliza la fórmula diferencias dividas de Newton.
    """
    

    # A es el arreglo de coeficientes, comienza con los valores de f(x)
    A = list(Y)
    
    # Por cada "nivel" de diferencias
    # Nos saltamos al primer nivel, ya que son los mismos valores de Y
    for i in range(1, len(A)):
        # Por cada Coeficiente
        # Los menores a i ya están en su valor definitivo
        
        # Vamos de atrás hacia adelanta para que al actualizar
        # los valores de A[j], los valores modicados no son usados
        # en la misma iteración sobre 'i'.
        for j in range(len(A)-1, i-1, -1):
            # A[j] - A[j - 1] es la diferencia de f[xj xj-1 ...x_k+1] - f[x_j x_j-1 ...x_k]
            # X[j] - X[j-i] es la diferencia de x_j - x_k 
            A[j] = (A[j] - A[j - 1]) / (X[j] - X[j-i])
    
    # Valor que multiplica a los coeficientes A_i. (x-x0)*(x-x1)...
    x_diff = 1
    y = A[0] * x_diff
    
    # Por cada coeficiente (desde A_1) 
    for i in range(0, len(X)-1):
        # Cada iteracion multiplica la diferencia de x con un nuevo 
        # x de la tabla, luego lo multiplica por el coeficiente
        x_diff *= (x - X[i])
        y += A[i+1] * x_diff
    return y

def interpolate(x, X, Y):
    return interpolate_newton(x, X, Y)