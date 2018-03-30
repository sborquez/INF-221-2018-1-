#!/usr/bin/python3
# # -*- coding: utf-8 -*-

__author__ = "Sebastián Bórquez González"

import numpy as np


def interpolate(x, X, Y):
    """
    interpolate obtiene el valor interpolado 'y' para un 'x' usando
    los puntos conocidos (X,Y) de una funcion f.
    
    Se utiliza la fórmula baricéntrica de Lagrange.

    Argumentos:
        x:  valor real (float) que se desea  obtener y = f(x).
        
        X:  ndarray de las componentes x de los puntos conocidos de f.
        Y:  ndarray de las componentes y de los puntos conocidos de f, donde yi = f(xi) para cada xi en X.
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