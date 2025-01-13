from sympy import *

dx, dy, dz = symbols('dx,dy,dz')
xi1, xi2, xi3 = symbols('xi1,xi2,xi3')

dNdxi = Matrix([[ -1, -1, -1 ],
                [  1,  0,  0 ],
                [  0,  1,  0 ],
                [  0,  0,  1 ]])

J = dx*dy*dz

for subElementIdx in range(0,6):
    print("\n\n Sub-element : %1d\n\n" % (subElementIdx))
    if(subElementIdx == 0):
        dxidx = Matrix([[  1/dx, -1/dy,     0 ],
                        [     0,  1/dy, -1/dz ],
                        [     0,     0,  1/dx ]])       
    elif(subElementIdx == 1):
        dxidx = Matrix([[  1/dx,     0, -1/dy ],
                        [ -1/dx,  1/dy,     0 ],
                        [     0,     0,  1/dz ]])
    elif(subElementIdx == 2):
        dxidx = Matrix([[  1/dx,     0, -1/dz ],
                        [     0,  1/dy,     0 ],
                        [     0, -1/dy,  1/dz ]])
    elif(subElementIdx == 3):
        dxidx = Matrix([[  1/dx, -1/dy,     0 ],
                        [     0,  1/dy,     0 ],
                        [ -1/dx,     0,  1/dz ]])
    elif(subElementIdx == 4):
        dxidx = Matrix([[  1/dx,     0, -1/dz ],
                        [     0,  1/dy, -1/dz ],
                        [ -1/dx,     0,  1/dz ]])
    elif(subElementIdx == 5):
        dxidx = Matrix([[  1/dx,     0,     0 ],
                        [ -1/dx,  1/dy,     0 ],
                        [     0, -1/dy,  1/dz ]])        
    for iIdx in range(0,3):
        for mIdx in range(0,4):
            dNmdxi = 0.0
            for xiIdx in range(0,3):
                dNmdxi = dNmdxi + dNdxi[mIdx,xiIdx]*dxidx[xiIdx,iIdx]
            for jIdx in range(0,3):
                for nIdx in range(0,4):
                    dNndxi = 0.0
                    for xiIdx in range(0,3):
                        dNndxi = dNndxi + dNdxi[nIdx,xiIdx]*dxidx[xiIdx,jIdx]
                    integrand = dNmdxi*dNndxi*J
                    integral1 = integrate(integrand,(xi3,0,1-xi1-xi2))
                    integral2 = integrate(integral1,xi2)
                    integral2 = integrate(integral1,(xi2,0,1-xi1))
                    integral3 = simplify(integrate(integral2,(xi1,0,1)))
                    print("i=%1d, m=%2d, j=%1d, n=%2d, K = %s" % (iIdx+1,mIdx+1,jIdx+1,nIdx+1,integral3))
                 

