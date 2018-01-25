'''
Author: Khoi Luc
UID: 104570581
Date: 1/23/2018
Usage: Implementation of jacobian
'''
from sympy import *
from T_matrix import T_matrix
import numpy
from sympy import Matrix

def jacobian(a1,a2,a3,a4):
    t1, t2, t3 ,t4 = symbols ('t1 t2 t3 t4')

    m_a1 = 0
    m_a2 = pi / 2
    m_a3 = pi / 2
    m_a4 = pi / 2
    m_a5 = 0

    m_r1 = 0
    m_r2 = 0
    m_r3 = 0
    m_r4 = 0
    m_r5 = 20

    m_d1 = 0
    m_d2 = 0
    m_d3 = 30
    m_d4 = 0
    m_d5 = 0

    m_t1 = t1
    m_t2 = t2
    m_t3 = t3
    m_t4 = t4
    m_t5 = 0

    T_01 = T_matrix(m_a1, m_r1, m_d1, m_t1)
    T_12 = T_matrix(m_a2, m_r2, m_d2, m_t2)
    T_23 = T_matrix(m_a3, m_r3, m_d3, m_t3)
    T_34 = T_matrix(m_a4, m_r4, m_d4, m_t4)
    T_45 = T_matrix(m_a5, m_r5, m_d5, m_t5)
    # forward kinematic to get the end effector
    T_05 = T_01 * T_12 * T_23 * T_34 * T_45

    ee = T_05 * Matrix([[0],[0],[0],[1]])

    x = ee[0]
    y = ee[1]
    z = ee[2]



    J = Matrix([[diff(x,t1), diff (x,t2), diff(x,t3), diff(x,t4)],
               [diff(y,t1), diff(y,t2), diff (y, t3), diff (y, t4)],
                [diff(z, t1), diff(z, t2), diff(z, t3), diff(z, t4)]
               ])
    result = J.evalf(subs={t1: a1, t2: a2, t3: a3, t4: a4})
    return numpy.matrix(result).astype(float)


