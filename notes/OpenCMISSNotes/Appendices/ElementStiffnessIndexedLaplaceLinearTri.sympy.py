from sympy import *

dx, dy = symbols('dx,dy')
xi1, xi2  = symbols('xi1,xi2')

dNdxi = Matrix([[ -1, -1 ],
                [  1,  0 ],
                [  0,  1 ]])

J = dx*dy

for subElementIdx in range(0,2):
    print("\n\n Sub-element : %1d\n\n" % (subElementIdx))
    if(subElementIdx == 0):
        dxidx = Matrix([[  1/dx, -1/dy ],
                        [     0,  1/dy ]])       
    elif(subElementIdx == 1):
        dxidx = Matrix([[  1/dx,     0 ],
                        [ -1/dx,  1/dy ]])
    for iIdx in range(0,2):
        for mIdx in range(0,3):
            dNmdxi = 0.0
            for xiIdx in range(0,2):
                dNmdxi = dNmdxi + dNdxi[mIdx,xiIdx]*dxidx[xiIdx,iIdx]
            for jIdx in range(0,2):
                for nIdx in range(0,3):
                    dNndxi = 0.0
                    for xiIdx in range(0,2):
                        dNndxi = dNndxi + dNdxi[nIdx,xiIdx]*dxidx[xiIdx,jIdx]
                    integrand = dNmdxi*dNndxi*J
                    integral1 = integrate(integrand,(xi2,0,1-xi1))
                    integral2 = simplify(integrate(integral1,(xi1,0,1)))
                    print("i=%1d, m=%2d, j=%1d, n=%2d, K = %s" % (iIdx+1,mIdx+1,jIdx+1,nIdx+1,integral2))
                 

