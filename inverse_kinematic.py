'''
Author: Khoi Luc
UID: 104570581
Date: 1/23/2018
Usage: The FK is abbreviated of forward kinematic. Here we
have 4 revolute joints. By inputting four theta angles of
the joint, we obtain the final position of the end effector



Variable:
x_d: desired position of end effector
x_0: initial position of end effector
q: an array contains all the angles to get to the x_d
'''
from jacobian import jacobian
from forward_kinematic import FK

import numpy



def IK(x_d):
    q_0 =numpy.array([0,0,0,0])
    x_0 =  FK(q_0[0],q_0[1],q_0[2],q_0[3])
    q = q_0
    x = x_0
    dx= x_d - x
    while (numpy.linalg.norm(dx) > 0.01):
        t1 = q[0]
        t2 = q [1]
        t3 = q [2]
        t4= q[3]
        J = jacobian (t1,t2,t3,t4)
        dq = numpy.linalg.pinv(J) * dx
        q= q + dq.A1
        x= FK(q[0],q[1],q[2],q[3])
        dx = x_d - x

        # debug
        print (x)

    return (q % (2* numpy.pi))

A =IK(numpy.matrix([[20],[0],[-30]]))
B =IK(numpy.matrix([[35.3553379],[0],[-7.07107359]]))
C =IK(numpy.matrix([[29.99992654],[0],[20.0001102]]))

print (A)
print (B)
print (C)


