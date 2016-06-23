
import numpy as np
import ast


n,m = 3,3
s = raw_input("Enter space sep. matrix elements: ")
items  = map(ast.literal_eval, s.split(' '))
assert(len(items) == n*m)
A  = np.array(items).reshape((n,m))
print "User given Matrix: " 
#print A 
s=(n,m)
#L=np.zeros(s)
U=np.zeros(s)
#print L

#print U
L=np.identity(3)
for j in xrange(n):
		
	for i in xrange(j+1):
		sum1 = sum(U[k][j] * L[i][k] for k in xrange(i))
    		U[i][j] = A[i][j]- sum1
    	for j in xrange(n):
			for i in xrange(j, n):
				sum2 = sum(U[k][j] * L[i][k] for k in xrange(j))
        			L[i][j] = (A[i][j] - sum2) / U[j][j]
print "user matrix"
print A
print "L matrix"
print L
print "U matrix"
print U
c=np.dot(L,U)
print "verfied by DOT product of LU"
print c