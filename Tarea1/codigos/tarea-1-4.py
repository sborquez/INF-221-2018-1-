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