#!/usr/bin/python3
# # -*- coding: utf-8 -*-

__author__ = "Sebastián Bórquez González"

import numpy as np


def interpolate(x, X, Y):
    """
    interpolate obtiene el valor interpolado 'y' para un 'x' usando
    los puntos conocidos (X,Y) de una funcion f.
    
    Se utiliza la fórmula baricéntrica de Lagrange.
    """
    w = [np.prod(X[j] - X[X != X[j]]) for j in range(len(X))]
    W = np.power(np.array(w), -1)
    diff = x - X    
    num = np.sum(W*Y / diff)
    den = np.sum(W / diff)
    return num/den


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
    xs = secMethod(g, -0.39, -0.19, 1E-10)

    print(xs, interpolate(xs, X, Y))



if __name__ == '__main__':
    main()