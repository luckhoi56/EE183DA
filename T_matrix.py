'''
Author: Cuong Hoang
UID:
Date: 1/23/2018
Usage: the T_matrix takes input from the D-H parameters and feed into
the matrix we derived in class.
'''
from sympy import Matrix
from sympy import sin, cos
import numpy
def T_matrix (alpha,a,d,theta):
    T = Matrix ([[cos(theta), -sin(theta), 0 ,a],
               [sin(theta)* cos (alpha), cos(theta) * cos(alpha), -sin (alpha), -sin(alpha) *d],
               [sin(theta)*sin(alpha), cos(theta) * sin (alpha), cos(alpha), cos(alpha) *d],
               [0,0,0,1]])
    return T



