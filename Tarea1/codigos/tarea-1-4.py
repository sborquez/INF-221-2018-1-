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


def main():
    # Puntos
    X = np.array([-1.000, -.600, -.467, -.200, -.067])
    Y = np.array([  .038,  .100,  .155,  .500,  .900])

    # y* 
    ys = 0.3

    # Interpolacion de la inversa
    xs = interpolate(ys, Y, X)

    print(xs)



if __name__ == '__main__':
    main()