from sympy import *

numberOfDimensions = 2
numberOfXi = 2
numberOfNodes = 4

dx, dy = symbols('dx,dy')
xi1, xi2  = symbols('xi1,xi2')

dPhidxi = Matrix([[ -(1-xi2), -(1-xi1) ],
                  [   1-xi2 ,    -xi1  ],
                  [    -xi2 ,   1-xi1  ], 
                  [     xi2 ,     xi1  ]])
dPhimdx = Matrix([ 0, 0 ])
dPhindx = Matrix([ 0, 0 ])
gu = Matrix([[ 0, 0 ],
             [ 0, 0 ]])
J = dx*dy

dxidx = Matrix([[  1/dx,     0 ],
                [     0,  1/dy ]])

for xiIdx1 in range(0,numberOfXi):
    for xiIdx2 in range(0,numberOfXi):
        gu[xiIdx1,xiIdx2]=0
        for coordIdx in range(0,numberOfDimensions):
            gu[xiIdx1,xiIdx2] = gu[xiIdx1,xiIdx2] + dxidx[xiIdx1,coordIdx]*dxidx[xiIdx2,coordIdx]
for mIdx in range(0,numberOfNodes):
     for nIdx in range(0,numberOfNodes):
         integrand = 0
         for xiIdx1 in range(0,numberOfXi):
             for xiIdx2 in range(0,numberOfXi):
                 integrand = integrand + dPhidxi[mIdx,xiIdx1]*dPhidxi[nIdx,xiIdx2]*gu[xiIdx1,xiIdx2]
         integrand = integrand*J
         integral1 = integrate(integrand,(xi2,0,1))
         integral2 = simplify(integrate(integral1,(xi1,0,1)))
         print("m=%2d, n=%2d, K = %s" % (mIdx+1,nIdx+1,integral2))
                 

