from sympy import *

numberOfDimensions = 3
numberOfXi = 3
numberOfNodes = 8

dx, dy, dz = symbols('dx,dy,dz')
xi1, xi2, xi3  = symbols('xi1,xi2,xi3')

dPhidxi = Matrix([[ -(1-xi2)*(1-xi3), -(1-xi1)*(1-xi3), -(1-xi1)*(1-xi2) ],
                  [  (1-xi2)*(1-xi3),     -xi1*(1-xi3),     -xi1*(1-xi2) ],
                  [     -xi2*(1-xi3),  (1-xi1)*(1-xi3),     -(1-xi1)*xi2 ],
                  [      xi2*(1-xi3),       xi1*(1-xi3),        -xi1*xi2 ],
                  [     -(1-xi2)*xi3,     -(1-xi1)*xi3,  (1-xi1)*(1-xi2) ],
                  [      (1-xi2)*xi3,         -xi1*xi3,      xi1*(1-xi2) ],
                  [         -xi2*xi3,      (1-xi1)*xi3,      (1-xi1)*xi2 ],
                  [          xi2*xi3,          xi1*xi3,          xi1*xi2 ]])
gu = Matrix([[ 0, 0, 0 ],
             [ 0, 0, 0 ],
             [ 0, 0, 0 ]])

J = dx*dy*dz

dxidx = Matrix([[ 1/dx,    0,    0 ],
                [    0, 1/dy,    0 ],
                [    0,    0, 1/dz ]])       
 
for xiIdx1 in range(0,numberOfXi):
    for xiIdx2 in range(0,numberOfXi):
        gu[xiIdx1,xiIdx2]=0
        for coordIdx in range(0,numberOfDimensions):
            gu[xiIdx1,xiIdx2] = gu[xiIdx1,xiIdx2] + dxidx[xiIdx1,coordIdx]*dxidx[xiIdx2,coordIdx]
print("gu = ",gu)
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
        integral1 = integrate(integrand,(xi3,0,1))
        integral2 = integrate(integral1,(xi2,0,1))
        integral3 = simplify(integrate(integral2,(xi1,0,1)))
        print("m=%2d, n=%2d, K = %s" % (mIdx+1,nIdx+1,integral3))
                 

