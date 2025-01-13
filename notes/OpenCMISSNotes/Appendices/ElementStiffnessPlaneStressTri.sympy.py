from sympy import *

LINEAR = 1
QUADRATIC = 2
CUBIC = 3

interpolation = LINEAR
#interpolation = QUADRATIC
#interpolation = CUBIC

numberOfDimensions = 2
numberOfXi = 2

dx, dy = symbols('dx,dy')
xi1, xi2  = symbols('xi1,xi2')
E, v = symbols('E,v')

xi = Matrix([ xi1, xi2 ])

if(interpolation == LINEAR):
    numberOfNodes = 3
    N = Matrix([ 1-xi1-xi2,
                 xi1,
                 xi2 ])
elif(interpolation == QUADRATIC):
    numberOfNodes = 6
    N = Matrix([ 2*xi1**2 + 4*xi1*xi2 - 3*xi1 + 2*xi2**2 - 3*xi2 + 1,
                 2*xi1**2 - xi1,
                 2*xi2**2 - xi2,
                 -4*xi1**2 - 4*xi1*xi2 + 4*xi1,
                 4*xi1*xi2,
                 -4*xi1*xi2 - 4*xi2**2 + 4*xi2 ])
elif(interpolation == CUBIC):
    numberOfNodes = 10 
    N = Matrix([ -4.5*xi1**3 - 13.5*xi1**2*xi2 + 9.0*xi1**2 - 13.5*xi1*xi2**2 + 18.0*xi1*xi2 - 5.5*xi1 - 4.5*xi2**3 + 9.0*xi2**2 - 5.5*xi2 + 1.0,
                 4.5*xi1**3 - 4.5*xi1**2 + 1.0*xi1,
                 4.5*xi2**3 - 4.5*xi2**2 + 1.0*xi2,
                 13.5*xi1**3 + 27.0*xi1**2*xi2 - 22.5*xi1**2 + 13.5*xi1*xi2**2 - 22.5*xi1*xi2 + 9.0*xi1,
                  -13.5*xi1**3 - 13.5*xi1**2*xi2 + 18.0*xi1**2 + 4.5*xi1*xi2 - 4.5*xi1,
                 13.5*xi1**2*xi2 - 4.5*xi1*xi2,
                 13.5*xi1*xi2**2 - 4.5*xi1*xi2,
                 -13.5*xi1*xi2**2 + 4.5*xi1*xi2 - 13.5*xi2**3 + 18.0*xi2**2 - 4.5*xi2,
                 13.5*xi1**2*xi2 + 27.0*xi1*xi2**2 - 22.5*xi1*xi2 + 13.5*xi2**3 - 22.5*xi2**2 + 9.0*xi2,
                 -27*xi1**2*xi2 - 27*xi1*xi2**2 + 27*xi1*xi2 ])

K = zeros(numberOfDimensions*numberOfNodes,numberOfDimensions*numberOfNodes)

dNdxi = zeros(numberOfNodes,numberOfXi)
for nodeIdx in range(0,numberOfNodes):
    for xiIdx in range(0,numberOfXi):
        dNdxi[nodeIdx,xiIdx] = N[nodeIdx].diff(xi[xiIdx])

print("dNdxi = ",dNdxi)

c = E/(1-v**2)*Matrix([[  1, v,       0 ],
                       [  v, 1,       0 ],
                       [  0, 0, (1-v)/2 ]])    

J = dx*dy

for subElementIdx in range(0,2):
    print("\n\n Sub-element : %1d\n\n" % (subElementIdx))
    if(subElementIdx == 0):
        dxidx = Matrix([[  1/dx, -1/dy ],
                        [     0,  1/dy ]])       
    elif(subElementIdx == 1):
        dxidx = Matrix([[  1/dx,     0 ],
                        [ -1/dx,  1/dy ]])

    dNdx = dNdxi*dxidx

    print("dNdx = ",dNdx)

    B = zeros(numberOfDimensions+1,numberOfNodes*numberOfDimensions)
    for nodeIdx in range(0,numberOfNodes):
        B[0,nodeIdx] = B[2,nodeIdx+numberOfNodes] = dNdx[nodeIdx,0]
        B[1,nodeIdx+numberOfNodes] = B[2,nodeIdx] = dNdx[nodeIdx,1]

    print("\nB: ", simplify(B))

    integrandMatrix = B.transpose()*c*B*J

    print("\nintegrandMatrix : ",integrandMatrix)

    K = Matrix([[simplify(integrate(integrandMatrix[i,j],(xi2,0,1-xi1),(xi1,0,1))) for i in range(0,numberOfDimensions*numberOfNodes)] for j in range(0,numberOfDimensions*numberOfNodes)])

    print("\nK : ",K)

    K1 = K.subs(E,30000000)
    K2 = K1.subs(v,0.3)

    print("\nK2: ", simplify(K2))

    K3=K2.subs(dx,dy)

    print("\nK3: ", simplify(K3))


# for iIdx in range(0,numberOfDimensions):
#     for mIdx in range(0,numberOfNodes):
#         for kIdx in range(0,numberOfDimensions):
#             for nIdx in range(0,numberOfNodes):
#                 integral = 0
#                 for jIdx in range(0,numberOfDimensions):
#                     cIdx1 = tensorToVoigt[iIdx,jIdx]
#                     dPhimdxi = 0.0
#                     for xiIdx in range(0,numberOfXi):
#                         dPhimdxi = dPhimdxi + dPhidxi[mIdx,xiIdx]*dxidx[xiIdx,jIdx]
#                     for lIdx in range(0,numberOfDimensions):
#                         cIdx2 = tensorToVoigt[kIdx,lIdx]
#                         dPhindxi = 0.0
#                         for xiIdx in range(0,numberOfXi):
#                                 dPhindxi = dPhindxi + dPhidxi[nIdx,xiIdx]*dxidx[xiIdx,lIdx]
#                         integrand = c[cIdx1,cIdx2]*dPhimdxi*dPhindxi*J
#                         integral1 = integrate(integrand,(xi2,0,1))
#                         integral2 = simplify(integrate(integral1,(xi1,0,1)))
#                         integral = integral + integral2
#                 K[iIdx*numberOfNodes+mIdx,kIdx*numberOfNodes+nIdx] = integral
#                 print("i=%1d, m=%2d, k=%1d, n=%2d, K = %s" % (iIdx+1,mIdx+1,kIdx+1,nIdx+1,integral))


# K1=K.subs(E,30000000)
# K2=K1.subs(v,0.3)

# print("\nK2: ", simplify(K2))

# K3=K2.subs(dx,dy)

# print("\nK3: ", simplify(K3))

