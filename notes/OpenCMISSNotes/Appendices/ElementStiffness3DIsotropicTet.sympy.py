from sympy import *

LINEAR = 1
QUADRATIC = 2
CUBIC = 3

#interpolation = LINEAR
interpolation = QUADRATIC
#interpolation = CUBIC

numberOfDimensions = 3
numberOfXi = 3

dx, dy, dz, a = symbols('dx,dy,dz,a')
xi1, xi2, xi3 = symbols('xi1,xi2,xi3')
E, v = symbols('E,v')

xi = Matrix([ xi1, xi2, xi3 ])

if(interpolation == LINEAR):
    numberOfNodes = 4
    N = Matrix([ 1-xi1-xi2-xi3,
                 xi1,
                 xi2,
                 xi3 ])
elif(interpolation == QUADRATIC):
    numberOfNodes = 10
    N = Matrix([ 2*xi1**2 + 4*xi1*xi2 + 4*xi1*xi3 - 3*xi1 + 2*xi2**2 + 4*xi2*xi3 - 3*xi2 + 2*xi3**2 - 3*xi3 + 1,
                 2*xi1**2 - xi1,
                 2*xi2**2 - xi2,
                 2*xi3**2 - xi3,
                 -4*xi1**2 - 4*xi1*xi2 - 4*xi1*xi3 + 4*xi1,
                 -4*xi1*xi2 - 4*xi2**2 - 4*xi2*xi3 + 4*xi2,
                 -4*xi1*xi3 - 4*xi2*xi3 - 4*xi3**2 + 4*xi3,
                 4*xi1*xi2,
                 4*xi2*xi3,
                 4*xi1*xi3 ])
elif(interpolation == CUBIC):
    numberOfNodes = 20 
    N = Matrix([ -9*xi1**3 - 27*xi1**2*xi2 - 27*xi1**2*xi3 + 18*xi1**2 - 27*xi1*xi2**2 - 54*xi1*xi2*xi3 + 36*xi1*xi2 - 27*xi1*xi3**2 + 36*xi1*xi3 - 11*xi1 - 9*xi2**3 - 27*xi2**2*xi3 + 18*xi2**2 - 27*xi2*xi3**2 + 36*xi2*xi3 - 11*xi2 - 9*xi3**3 + 18*xi3**2 - 11*xi3 + 2,
                 9*xi1**3 - 6*xi1**2 + xi1,
                  9*xi2**3 - 6*xi2**2 + xi2,
                  9*xi3**3 - 6*xi3**2 + xi3,
                 13.5*xi1**3 + 27.0*xi1**2*xi2 + 27.0*xi1**2*xi3 - 22.5*xi1**2 + 13.5*xi1*xi2**2 + 27.0*xi1*xi2*xi3 - 22.5*xi1*xi2 + 13.5*xi1*xi3**2 - 22.5*xi1*xi3 + 9.0*xi1,
                 -13.5*xi1**3 - 13.5*xi1**2*xi2 - 13.5*xi1**2*xi3 + 18.0*xi1**2 + 4.5*xi1*xi2 + 4.5*xi1*xi3 - 4.5*xi1,
                 13.5*xi1**2*xi2 + 27.0*xi1*xi2**2 + 27.0*xi1*xi2*xi3 - 22.5*xi1*xi2 + 13.5*xi2**3 + 27.0*xi2**2*xi3 - 22.5*xi2**2 + 13.5*xi2*xi3**2 - 22.5*xi2*xi3 + 9.0*xi2,
                 -13.5*xi1*xi2**2 + 4.5*xi1*xi2 - 13.5*xi2**3 - 13.5*xi2**2*xi3 + 18.0*xi2**2 + 4.5*xi2*xi3 - 4.5*xi2,
                 13.5*xi1**2*xi3 + 27.0*xi1*xi2*xi3 + 27.0*xi1*xi3**2 - 22.5*xi1*xi3 + 13.5*xi2**2*xi3 + 27.0*xi2*xi3**2 - 22.5*xi2*xi3 + 13.5*xi3**3 - 22.5*xi3**2 + 9.0*xi3,
                 -13.5*xi1*xi3**2 + 4.5*xi1*xi3 - 13.5*xi2*xi3**2 + 4.5*xi2*xi3 - 13.5*xi3**3 + 18.0*xi3**2 - 4.5*xi3,
                 13.5*xi1**2*xi2 - 4.5*xi1*xi2,
                 13.5*xi1*xi2**2 - 4.5*xi1*xi2,
                 13.5*xi2**2*xi3 - 4.5*xi2*xi3,
                 13.5*xi2*xi3**2 - 4.5*xi2*xi3,
                  13.5*xi1**2*xi3 - 4.5*xi1*xi3,
                 13.5*xi1*xi3**2 - 4.5*xi1*xi3,
                 -27*xi1**2*xi2 - 27*xi1*xi2**2 - 27*xi1*xi2*xi3 + 27*xi1*xi2,
                 -27*xi1**2*xi3 - 27*xi1*xi2*xi3 - 27*xi1*xi3**2 + 27*xi1*xi3,
                 -27*xi1*xi2*xi3 - 27*xi2**2*xi3 - 27*xi2*xi3**2 + 27*xi2*xi3,
                  27*xi1*xi2*xi3 ])

K = zeros(numberOfDimensions*numberOfNodes,numberOfDimensions*numberOfNodes)


dNdxi = zeros(numberOfNodes,numberOfXi)
for nodeIdx in range(0,numberOfNodes):
    for xiIdx in range(0,numberOfXi):
        dNdxi[nodeIdx,xiIdx] = N[nodeIdx].diff(xi[xiIdx])

print("dNdxi = ",dNdxi)

c = E/((1+v)*(1-2*v))*Matrix([[  1-v,   v,   v,         0,         0,         0 ],
                              [    v, 1-v,   v,         0,         0,         0 ],
                              [    v,   v, 1-v,         0,         0,         0 ],
                              [    0,   0,   0, (1-2*v)/2,         0,         0 ],
                              [    0,   0,   0,         0, (1-2*v)/2,         0 ],
                              [    0,   0,   0,         0,         0, (1-2*v)/2 ]])

J = dx*dy*dz

for subElementIdx in range(0,2):
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

    dNdx = dNdxi*dxidx

    print("dNdx = ",dNdx)

    B = zeros(6,numberOfNodes*numberOfDimensions)
    for nodeIdx in range(0,numberOfNodes):
        B[0,nodeIdx]                 = B[4,nodeIdx+2*numberOfNodes] = B[5,nodeIdx+numberOfNodes] = dNdx[nodeIdx,0]
        B[1,nodeIdx+numberOfNodes]   = B[3,nodeIdx+2*numberOfNodes] = B[5,nodeIdx]               = dNdx[nodeIdx,1]
        B[2,nodeIdx+2*numberOfNodes] = B[3,nodeIdx+numberOfNodes]   = B[4,nodeIdx]               = dNdx[nodeIdx,2]

    print("\nB: ", simplify(B))

    integrandMatrix = B.transpose()*c*B*J

    print("\nintegrandMatrix : ",integrandMatrix)

    for rowElementDOFIdx in range(0,numberOfDimensions*numberOfNodes):
        for columnElementDOFIdx in range(0,numberOfDimensions*numberOfNodes):
            integrand = integrandMatrix[rowElementDOFIdx,columnElementDOFIdx]
            integral1 = integrate(integrand,(xi3,0,1-xi1-xi2))
            integral2 = integrate(integral1,(xi2,0,1-xi1))
            integral3 = integrate(integral2,(xi1,0,1))
            K[rowElementDOFIdx,columnElementDOFIdx] = simplify(integral3)

    print("\nK : ",K)
    
    K1 = K.subs(E,30000000)
    K2 = K1.subs(v,0.3)
    
    print("\nK2: ", simplify(K2))
    
    K3=K2.subs(dx,a)
    K4=K3.subs(dy,a)
    K5=K4.subs(dz,a)
    
    print("\nK5: ", simplify(K5))
