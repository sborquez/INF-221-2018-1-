#!/usr/bin/python3
# # -*- coding: utf-8 -*-

__author__ = "Sebastián Bórquez González"

import numpy as np


def interpolate(x, X, Y):
    """
    interpolate obtiene el valor interpolado 'y' para un 'x' usando
    los puntos conocidos (X,Y) de una funcion f.
    
    Se utiliza la fórmula diferencias dividas de Newton.
    """
    A = list(Y)
    for i in range(1, len(A)):
        for j in range(len(A)-1, i-1, -1):
            A[j] = (A[j] - A[j - 1]) / (X[j] - X[j-i])
    
    x_diff = 1
    y = A[0] * x_diff
    
    for i in range(0, len(X)-1):
        x_diff *= (x - X[i])
        y += A[i+1] * x_diff
    return y


def secMethod(f, x0, x1, epsilon):
    """
    Implementación del método de la secante para hallar ceros de la función f, 
    dado los puntos iniciales x0 y x1.
    """

    x2 = x1
    iterations = 0
    while abs(f(x2)) > epsilon and iterations < 100000:
        f0 = f(x0)
        f1 = f(x1)
        x2 = x1 - (f1*(x1 - x0))/(f1 - f0)
        iterations += 1        
        x0, x1 = x1, x2
    return x2

def main():
    # Puntos
    X = np.array([-1.000, -.600, -.467, -.200, -.067])
    Y = np.array([  .038,  .100,  .155,  .500,  .900])

    # Obtenemos la interseccion entre f y 0.3
    # g(x) = f(x) - 0.3 
    g = lambda x:  interpolate(x, X, Y) - 0.3
    
    # Buscamos su raíz, la que se debe encontrar entre -0.4 y -0.2
    xs = secMethod(g, -0.468, -0.19, 1E-10)

    print(xs)



if __name__ == '__main__':
    main()