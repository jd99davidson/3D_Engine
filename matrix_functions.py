import math as m
import numpy as np

def translate(pos):
    tx, ty, tz = pos
    return np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [tx, ty, tz, 1]])

def rotate_x(a):
    return np.array([[1, 0, 0, 0],
                     [0, m.cos(a), m.sin(a), 0],
                     [0, -m.sin(a), m.cos(a), 0],
                     [0, 0, 0, 1]])

def rotate_y(a):
    return np.array([[m.cos(a), 0, -m.sin(a), 0],
                     [0, 1, 0, 0],
                     [m.sin(a), 0, m.cos(a), 0],
                     [0, 0, 0, 1]])

def rotate_z(a):
    return np.array([[m.cos(a), m.sin(a), 0, 0],
                     [-m.sin(a), m.cos(a), 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])

def scale(n):
    return np.array([[n, 0, 0, 0],
                     [0, n, 0, 0],
                     [0, 0, n, 0],
                     [0, 0, 0, 1]])


