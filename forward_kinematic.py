'''
Author: Cuong Hoang
UID:
Date: 1/23/2018
Usage: The FK is abbreviated of forward kinematic. Here we
have 4 revolute joints. By inputting four theta angles of
the joint, we obtain the final position of the end effector
'''


from sympy import pi
import numpy
from sympy import Matrix
from T_matrix import T_matrix
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#import matplotlib as plt

def FK (t1, t2, t3, t4):
    m_a1 = 0
    m_a2 = pi/2
    m_a3 = pi/2
    m_a4 = pi/2
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

    #the T_matrix is sympy.Matrix
    #cast from object -> float
    ee = numpy.matrix(T_05 * Matrix([[0],[0],[0],[1]])).astype(float)

    #truncate the excessive 1 at the end
    ee = ee[0:-1]

    return  ee
A = (FK (0, 0, 0, 0))
B = (FK (0, 0.785398, 0, 0))
C = (FK (0, 1.5708, 0, 0))

print (A)
print (B)
print (C)

fig = plt.figure()
ax = Axes3D(fig)
plt.xlabel('x')
plt.ylabel('y')
ax.set_xlabel('X label')
ax.set_ylabel('Y label')
ax.set_zlabel('Z label')
ax.scatter(A[0],A[1],A[2], color ='blue' )
ax.scatter(B[0],B[1],B[2], color ='orange' )
ax.scatter(C[0],C[1],C[2], color ='red')

plt.show()