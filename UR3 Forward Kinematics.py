#!/usr/bin/env python
import numpy as np
from scipy.linalg import expm
from lab4_header import *

"""
Use 'expm' for matrix exponential.
Angles are in radian, distance are in meters.
"""

# We created the function to calculate [S]
def skew(s):

	# skewW = np.zeros((3,3))
	#print(s)
	skewW = np.array([[0, -s[2], s[1]], [s[2], 0, s[0]], [-s[1], s[0], 0]])
	#print(s)
	skewW= np.column_stack((skewW,s[3:]))
	skews = np.vstack((skewW,[0, 0, 0, 0]))
	# print(skews)
	# print(skews)
	return skews

def Get_MS():
	# =================== Your code starts here ====================#
	# Fill in the correct values for S1~6, as well as the M matrix
	M = np.array([[0, -1, 0, 0.420], [0, 0, -1, 0.349], [1, 0, 0, 0.152], [0, 0, 0, 1]])
	
	w1 = np.array([0, 0, 1])
	w2 = np.array([0, -1, 0])
	w3 = np.array([0, -1, 0])
	w4 = np.array([0, -1, 0])
	w5 = np.array([1, 0, 0])
	w6 = np.array([0, -1, 0])

	q1 = np.array([-0.120, 0.147, 0])
	q2 = np.array([-0.120, 0, 0.152])
	q3 = np.array([0.124, 0, 0.152])
	q4 = np.array([0.337, 0, 0.152])
	q5 = np.array([0, 0.267, 0.152])
	q6 = np.array([0.420, 0, 0.152])

	v1 = np.cross(-w1,q1)
	v2 = np.cross(-w2,q2)
	v3 = np.cross(-w3,q3)
	v4 = np.cross(-w4,q4)
	v5 = np.cross(-w5,q5)
	v6 = np.cross(-w6,q6)

	S1 = np.transpose(np.concatenate((w1, v1)))
	S2 = np.transpose(np.concatenate((w2, v2)))
	S3 = np.transpose(np.concatenate((w3, v3)))
	S4 = np.transpose(np.concatenate((w4, v4)))
	S5 = np.transpose(np.concatenate((w5, v5)))
	S6 = np.transpose(np.concatenate((w6, v6)))

	# print(v1)
	# print(S1.shape)
	# print(v1.shape)
	#print(S1)
	#print(S1)
	S = np.column_stack((S1, S2, S3, S4, S5, S6))
	# print(S)



	
	# ==============================================================#
	return M, S


"""
Function that calculates encoder numbers for each motor
"""
def lab_fk(theta1, theta2, theta3, theta4, theta5, theta6):

	# Initialize the return_value 
	return_value = [None, None, None, None, None, None]

	# =========== Implement joint angle to encoder expressions here ===========
	print("Foward kinematics calculated Hello:\n")

	# =================== Your code starts here ====================#
	theta = np.array([theta1,theta2,theta3,theta4,theta5,theta6])
	T = np.eye(4)

	M, S = Get_MS()

	S1_skew = skew(S[:,0])
	S2_skew = skew(S[:,1])
	S3_skew = skew(S[:,2])
	S4_skew = skew(S[:,3])
	S5_skew = skew(S[:,4])
	S6_skew = skew(S[:,5])

	# print(S)

	for x in range(len(theta)):
		T = np.matmul(T, expm(skew(S[:,x])*theta[x]))


	T = np.matmul(T, M)









	# ==============================================================#
	
	print(str(T) + "\n")

	return_value[0] = theta1 + PI
	return_value[1] = theta2
	return_value[2] = theta3
	return_value[3] = theta4 - (0.5*PI)
	return_value[4] = theta5
	return_value[5] = theta6

	return return_value


