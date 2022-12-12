import math 
import os 
import random 
import re 
import sys


def compareTriplets(a, b):
    puntuacion_a = 0
    puntuacion_b = 0
    for i in range(3):
        if a[i]>b[i]:
            puntuacion_a=puntuacion_a + 1
        elif a[i]<b[i]:
            puntuacion_b=puntuacion_b+1
    return puntuacion_a, puntuacion_b


