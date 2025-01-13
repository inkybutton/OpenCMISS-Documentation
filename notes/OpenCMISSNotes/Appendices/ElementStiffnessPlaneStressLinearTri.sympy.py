from sympy import *

dx, dy = symbols('dx,dy')
xi1, xi2  = symbols('xi1,xi2')
E, v = symbols('E,v')

dNdxi = Matrix([[ -1, -1 ],
                [  1,  0 ],
                [  0,  1 ]])

tensorToVoigt = Matrix([[ 0, 2 ],
                        [ 2, 1 ]])

c = Matrix([[   E/(1-v**2), E*v/(1-v**2),           0 ],
            [ E*v/(1-v**2),   E/(1-v**2),           0 ],
            [            0,            0, E/(2*(1+v)) ]])    

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
            for kIdx in range(0,2):
                for nIdx in range(0,3):
                    K = 0
                    for jIdx in range(0,2):
                        cIdx1 = tensorToVoigt[iIdx,jIdx]
                        dNmdxi = 0.0
                        for xiIdx in range(0,2):
                            dNmdxi = dNmdxi + dNdxi[mIdx,xiIdx]*dxidx[xiIdx,jIdx]
                        for lIdx in range(0,2):
                            cIdx2 = tensorToVoigt[kIdx,lIdx]
                            dNndxi = 0.0
                            for xiIdx in range(0,2):
                                dNndxi = dNndxi + dNdxi[nIdx,xiIdx]*dxidx[xiIdx,lIdx]
                            integrand = c[cIdx1,cIdx2]*dNmdxi*dNndxi*J
                            integral1 = integrate(integrand,(xi2,0,1-xi1))
                            integral2 = simplify(integrate(integral1,(xi1,0,1)))
                            K = K + integral2
                    print("i=%1d, m=%2d, k=%1d, n=%2d, K = %s" % (iIdx+1,mIdx+1,kIdx+1,nIdx+1,K))
                            

