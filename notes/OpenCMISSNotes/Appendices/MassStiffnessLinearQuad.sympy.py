from sympy import *

numberOfDimensions = 2
numberOfXi = 2
numberOfNodes = 4

dx, dy = symbols('dx,dy')
xi1, xi2  = symbols('xi1,xi2')

Phi = Matrix([[ (1-xi1)*(1-xi2) ],
                  [ xi1*(1-xi2) ],
                  [ (1-xi1)*xi2 ], 
                  [ xi1*xi1 ]])
J = dx*dy

for mIdx in range(0,numberOfNodes):
     for nIdx in range(0,numberOfNodes):
         integrand = Phi[mIdx]*Phi[nIdx]*J
         integral1 = integrate(integrand,(xi2,0,1))
         integral2 = simplify(integrate(integral1,(xi1,0,1)))
         print("m=%2d, n=%2d, K = %s" % (mIdx+1,nIdx+1,integral2))
                 

