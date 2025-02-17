from sympy import *

numberOfDimensions = 2
numberOfXi = 2
numberOfNodes = 9

dx, dy = symbols('dx,dy')
xi1, xi2  = symbols('xi1,xi2')

dPhidxi = Matrix([[ -(1-xi2), -(1-xi1) ],
                  [   1-xi2 ,    -xi1  ],
                  [    -xi2 ,   1-xi1  ], 
                  [     xi2 ,     xi1  ]])
dPhimdx = Matrix([ 0, 0 ])
dPhindx = Matrix([ 0, 0 ])

J = dx*dy

dxidx = Matrix([[  1/dx,     0 ],
                [     0,  1/dy ]])       
 
for mIdx in range(0,numberOfNodes):
    for coordIdx in range(0,numberOfDimensions):
        dPhimdx[coordIdx] = 0
        for xiIdx in range(0,numberOfXi):
             dPhimdx[coordIdx] = dPhimdx[coordIdx] + dPhidxi[mIdx,xiIdx]*dxidx[xiIdx,coordIdx]
    for nIdx in range(0,numberOfNodes):
        for coordIdx in range(0,numberOfDimensions):
            dPhindx[coordIdx] = 0
            for xiIdx in range(0,numberOfXi):
                dPhindx[coordIdx] = dPhindx[coordIdx] + dPhidxi[nIdx,xiIdx]*dxidx[xiIdx,coordIdx]
        integrand = 0
        for coordIdx in range(0,numberOfDimensions):
            integrand = integrand + dPhimdx[coordIdx]*dPhindx[coordIdx]
        integrand = integrand*J
        integral1 = integrate(integrand,(xi2,0,1))
        integral2 = simplify(integrate(integral1,(xi1,0,1)))
        print("m=%2d, n=%2d, K = %s" % (mIdx+1,nIdx+1,integral2))
                 

