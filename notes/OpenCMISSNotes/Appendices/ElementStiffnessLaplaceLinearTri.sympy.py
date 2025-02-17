from sympy import *

numberOfDimensions = 2
numberOfXi = 2
numberOfNodes = 3
numberOfSubelements = 2

dx, dy = symbols('dx,dy')
xi1, xi2  = symbols('xi1,xi2')

dNdxi = Matrix([[ -1, -1 ],
                [  1,  0 ],
                [  0,  1 ]])
gu = Matrix([[ 0, 0 ],
             [ 0, 0 ]])

J = dx*dy

for subElementIdx in range(0,numberOfSubelements):
    print("\n\n Sub-element : %1d\n\n" % (subElementIdx))
    if(subElementIdx == 0):
        dxidx = Matrix([[  1/dx, -1/dy ],
                        [     0,  1/dy ]])       
    elif(subElementIdx == 1):
        dxidx = Matrix([[  1/dx,     0 ],
                        [ -1/dx,  1/dy ]])
    for xiIdx1 in range(0,numberOfXi):
        for xiIdx2 in range(0,numberOfXi):
            gu[xiIdx1,xiIdx2]=0
            for coordIdx in range(0,numberOfDimensions):
                gu[xiIdx1,xiIdx2] = gu[xiIdx1,xiIdx2] + dxidx[xiIdx1,coordIdx]*dxidx[xiIdx2,coordIdx]
    print("gu = ",gu)
    for mIdx in range(0,numberOfNodes):
        for nIdx in range(0,numberOfNodes):
            integrand = 0
            for xiIdx1 in range(0,numberOfXi):
                for xiIdx2 in range(0,numberOfXi):
                    integrand = integrand + dNdxi[mIdx,xiIdx1]*dNdxi[nIdx,xiIdx2]*gu[xiIdx1,xiIdx2]
            integrand = integrand*J
            integral1 = integrate(integrand,(xi3,0,1-xi1-xi2))
            integral2 = integrate(integral1,(xi2,0,1-xi1))
            integral3 = simplify(integrate(integral2,(xi1,0,1)))
            print("m=%2d, n=%2d, K = %s" % (mIdx+1,nIdx+1,integral3))
                

