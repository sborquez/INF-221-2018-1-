#!/usr/bin/python3
# # -*- coding: utf-8 -*-

__author__ = "Sebastián Bórquez González"


def secMethod(f, x0, x1, epsilon):
    """
    Implementación del método de la secante para hallar ceros de la función f, 
    dado los puntos iniciales x0 y x1.
    """
    x2 = x1
    iterations = 0
    while abs(f(x2)) > epsilon and iterations < 100000:
        # Metodo de la secante
        f0 = f(x0)
        f1 = f(x1)
        x2 = x1 - (f1*(x1 - x0))/(f1 - f0)
        
        # Contamos las iteraciones para no entrar en un bucle infinito
        iterations += 1
        
        # Actualizamos los valores
        x0, x1 = x1, x2
    return x2