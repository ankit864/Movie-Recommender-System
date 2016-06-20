import numpy as np
import ast
import numpy.linalg as linalg

def gram_schmidt_columns(X):
    Q, R = np.linalg.qr(X)
    return Q

def eigenValuesVectors(Y):
	eigenValues,eigenVectors = linalg.eig(Y)
	idx = eigenValues.argsort()[::-1]   
	eigenValues = eigenValues[idx]
	eigenVectors = eigenVectors[:,idx]
	return eigenValues,  eigenVectors

n,m = 2,3
s = raw_input("Enter space sep. matrix elements: ")
items  = map(ast.literal_eval, s.split(' '))
assert(len(items) == n*m)
A  = np.array(items).reshape((n,m))
print "User given Matrix: " 
print A 
A_T = A.transpose()
A_dot_A_T = np.dot(A,A_T)
e_value , e_vector = eigenValuesVectors(A_dot_A_T)
U = gram_schmidt_columns(e_vector)
A_T_dot_A = np.dot(A_T,A)
e_value , e_vector = eigenValuesVectors(A_T_dot_A)
v=gram_schmidt_columns(e_vector)
V = v.transpose()
k = np.sqrt(e_value)
r = np.diag(k)
d = r[~np.all(r == 0, axis=1)]
print "U = " 
print  U
print "S = " 
print d
print "V = " 
print  V
final  = np.dot(U,d)
final1 = np.dot(final,V)
print final1
