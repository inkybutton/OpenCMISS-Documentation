from sympy import *

xi, xi1, xi2, xi3 = symbols('xi,xi1,xi2,xi3')
l1, l2, l3, l4 = symbols('l1,l2,l3,l4')

print("\n\nArea coordinates:\n\n")

def l11(xi):
    return 1-xi
def l12(xi):
    return xi

print("l11 = %s\n"%(expand(l11(xi))))
print("l12 = %s\n"%(expand(l12(xi))))

def dl11dxi(xi):
    return diff(l11(xi),xi)
def dl12dxi(xi):
    return diff(l12(xi),xi)

print("dl11dxi = %s\n"%(expand(dl11dxi(xi))))
print("dl12dxi = %s\n"%(expand(dl12dxi(xi))))

def d2l11dxidxi(xi):
    return diff(dl11dxi(xi),xi)
def d2l12dxidxi(xi):
    return diff(dl12dxi(xi),xi)

print("d2l11dxidxi = %s\n"%(expand(d2l11dxidxi(xi))))
print("d2l12dxidxi = %s\n"%(expand(d2l12dxidxi(xi))))

def l21(xi1,xi2):
    return 1-xi1-xi2
def l22(xi1,xi2):
    return xi1
def l23(xi1,xi2):
    return xi2

print("l21 = %s\n"%(expand(l21(xi1,xi2))))
print("l22 = %s\n"%(expand(l22(xi1,xi2))))
print("l23 = %s\n"%(expand(l23(xi1,xi2))))

def dl21dxi1(xi1,xi2):
    return diff(l21(xi1,xi2),xi1)
def dl22dxi1(xi1,xi2):
    return diff(l22(xi1,xi2),xi1)
def dl23dxi1(xi1,xi2):
    return diff(l23(xi1,xi2),xi1)

print("dl21dxi1 = %s\n"%(expand(dl21dxi1(xi1,xi2))))
print("dl22dxi1 = %s\n"%(expand(dl22dxi1(xi1,xi2))))
print("dl23dxi1 = %s\n"%(expand(dl23dxi1(xi1,xi2))))

def dl21dxi2(xi1,xi2):
    return diff(l21(xi1,xi2),xi2)
def dl22dxi2(xi1,xi2):
    return diff(l22(xi1,xi2),xi2)
def dl23dxi2(xi1,xi2):
    return diff(l23(xi1,xi2),xi2)

print("dl21dxi2 = %s\n"%(expand(dl21dxi2(xi1,xi2))))
print("dl22dxi2 = %s\n"%(expand(dl22dxi2(xi1,xi2))))
print("dl23dxi2 = %s\n"%(expand(dl23dxi2(xi1,xi2))))

def d2l21dxi1dxi2(xi1,xi2):
    return diff(dl21dxi1(xi1,xi2),xi2)
def d2l22dxi1dxi2(xi1,xi2):
    return diff(dl22dxi1(xi1,xi2),xi2)
def d2l23dxi1dxi2(xi1,xi2):
    return diff(dl23dxi1(xi1,xi2),xi2)

print("d2l21dxi1dxi2 = %s\n"%(expand(d2l21dxi1dxi2(xi1,xi2))))
print("d2l22dxi1dxi2 = %s\n"%(expand(d2l22dxi1dxi2(xi1,xi2))))
print("d2l23dxi1dxi2 = %s\n"%(expand(d2l23dxi1dxi2(xi1,xi2))))

def l31(xi1,xi2,xi3):
    return 1-xi1-xi2-xi3
def l32(xi1,xi2,xi3):
    return xi1
def l33(xi1,xi2,xi3):
    return xi2
def l34(xi1,xi2,xi3):
    return xi3

print("l31 = %s\n"%(expand(l31(xi1,xi2,xi3))))
print("l32 = %s\n"%(expand(l32(xi1,xi2,xi3))))
print("l33 = %s\n"%(expand(l33(xi1,xi2,xi3))))
print("l34 = %s\n"%(expand(l34(xi1,xi2,xi3))))

print("\n\nLinear Line Simplex Basis Functions:\n\n")

def L1N1(xi):
    return l11(xi)
def L1N2(xi):
    return l12(xi)

print("L1N1 = %s\n"%(expand(L1N1(xi))))
print("L1N2 = %s\n"%(expand(L1N2(xi))))

def dL1N1dxi(xi):
    return diff(L1N1(xi),xi)
def dL1N2dxi(xi):
    return diff(L1N2(xi),xi)

print("dL1N1dxi = %s\n"%(expand(dL1N1dxi(xi))))
print("dL1N2dxi = %s\n"%(expand(dL1N2dxi(xi))))

def d2L1N1dxidxi(xi):
    return diff(dL1N1dxi(xi),xi)
def d2L1N2dxidxi(xi):
    return diff(dL1N2dxi(xi),xi)

print("d2L1N1dxidxi = %s\n"%(expand(d2L1N1dxidxi(xi))))
print("d2L1N2dxidxi = %s\n"%(expand(d2L1N2dxidxi(xi))))

print("\n\nLinear Triangle Simplex Basis Functions:\n\n")

def L2N1(xi1,xi2):
    return l21(xi1,xi2)
def L2N2(xi1,xi2):
    return l22(xi1,xi2)
def L2N3(xi1,xi2):
    return l23(xi1,xi2)

print("L2N1 = %s\n"%(expand(L2N1(xi1,xi2))))
print("L2N2 = %s\n"%(expand(L2N2(xi1,xi2))))
print("L2N3 = %s\n"%(expand(L2N3(xi1,xi2))))

def dL2N1dxi1(xi1,xi2):
    return diff(L2N1(xi1,xi2),xi1)
def dL2N2dxi1(xi1,xi2):
    return diff(L2N2(xi1,xi2),xi1)
def dL2N3dxi1(xi1,xi2):
    return diff(L2N3(xi1,xi2),xi1)

print("dL2N1dxi1 = %s\n"%(expand(dL2N1dxi1(xi1,xi2))))
print("dL2N2dxi1 = %s\n"%(expand(dL2N2dxi1(xi1,xi2))))
print("dL2N3dxi1 = %s\n"%(expand(dL2N3dxi1(xi1,xi2))))

def dL2N1dxi2(xi1,xi2):
    return diff(L2N1(xi1,xi2),xi2)
def dL2N2dxi2(xi1,xi2):
    return diff(L2N2(xi1,xi2),xi2)
def dL2N3dxi2(xi1,xi2):
    return diff(L2N3(xi1,xi2),xi2)

print("dL2N1dxi2 = %s\n"%(expand(dL2N1dxi2(xi1,xi2))))
print("dL2N2dxi2 = %s\n"%(expand(dL2N2dxi2(xi1,xi2))))
print("dL2N3dxi2 = %s\n"%(expand(dL2N3dxi2(xi1,xi2))))

def d2L2N1dxi1dxi1(xi1,xi2):
    return diff(dL2N1dxi1(xi1,xi2),xi1)
def d2L2N2dxi1dxi1(xi1,xi2):
    return diff(dL2N2dxi1(xi1,xi2),xi1)
def d2L2N3dxi1dxi1(xi1,xi2):
    return diff(dL2N3dxi1(xi1,xi2),xi1)

print("d2L2N1dxi1dxi1 = %s\n"%(expand(d2L2N1dxi1dxi1(xi1,xi2))))
print("d2L2N2dxi1dxi1 = %s\n"%(expand(d2L2N2dxi1dxi1(xi1,xi2))))
print("d2L2N3dxi1dxi1 = %s\n"%(expand(d2L2N3dxi1dxi1(xi1,xi2))))

def d2L2N1dxi2dxi2(xi1,xi2):
    return diff(dL2N1dxi2(xi1,xi2),xi2)
def d2L2N2dxi2dxi2(xi1,xi2):
    return diff(dL2N2dxi2(xi1,xi2),xi2)
def d2L2N3dxi2dxi2(xi1,xi2):
    return diff(dL2N3dxi2(xi1,xi2),xi2)

print("d2L2N1dxi2dxi2 = %s\n"%(expand(d2L2N1dxi2dxi2(xi1,xi2))))
print("d2L2N2dxi2dxi2 = %s\n"%(expand(d2L2N2dxi2dxi2(xi1,xi2))))
print("d2L2N3dxi2dxi2 = %s\n"%(expand(d2L2N3dxi2dxi2(xi1,xi2))))

def d2L2N1dxi1dxi2(xi1,xi2):
    return diff(dL2N1dxi1(xi1,xi2),xi2)
def d2L2N2dxi1dxi2(xi1,xi2):
    return diff(dL2N2dxi1(xi1,xi2),xi2)
def d2L2N3dxi1dxi2(xi1,xi2):
    return diff(dL2N3dxi1(xi1,xi2),xi2)

print("d2L2N1dxi1dxi2 = %s\n"%(expand(d2L2N1dxi1dxi2(xi1,xi2))))
print("d2L2N2dxi1dxi2 = %s\n"%(expand(d2L2N2dxi1dxi2(xi1,xi2))))
print("d2L2N3dxi1dxi2 = %s\n"%(expand(d2L2N3dxi1dxi2(xi1,xi2))))


print("\n\nLinear Tetrahedral Simplex Basis Functions:\n\n")

def L3N1(xi1,xi2,xi3):
    return l31(xi1,xi2,xi3)
def L3N2(xi1,xi2,xi3):
    return l32(xi1,xi2,xi3)
def L3N3(xi1,xi2,xi3):
    return l33(xi1,xi2,xi3)
def L3N4(xi1,xi2,xi3):
    return l34(xi1,xi2,xi3)

print("L3N1 = %s\n"%(expand(L3N1(xi1,xi2,xi3))))
print("L3N2 = %s\n"%(expand(L3N2(xi1,xi2,xi3))))
print("L3N3 = %s\n"%(expand(L3N3(xi1,xi2,xi3))))
print("L3N4 = %s\n"%(expand(L3N4(xi1,xi2,xi3))))

def dL3N1dxi1(xi1,xi2,xi3):
    return diff(L3N1(xi1,xi2,xi3),xi1)
def dL3N2dxi1(xi1,xi2,xi3):
    return diff(L3N2(xi1,xi2,xi3),xi1)
def dL3N3dxi1(xi1,xi2,xi3):
    return diff(L3N3(xi1,xi2,xi3),xi1)
def dL3N4dxi1(xi1,xi2,xi3):
    return diff(L3N4(xi1,xi2,xi3),xi1)

print("dL3N1dxi1 = %s\n"%(expand(dL3N1dxi1(xi1,xi2,xi3))))
print("dL3N2dxi1 = %s\n"%(expand(dL3N2dxi1(xi1,xi2,xi3))))
print("dL3N3dxi1 = %s\n"%(expand(dL3N3dxi1(xi1,xi2,xi3))))
print("dL3N4dxi1 = %s\n"%(expand(dL3N4dxi1(xi1,xi2,xi3))))

def dL3N1dxi2(xi1,xi2,xi3):
    return diff(L3N1(xi1,xi2,xi3),xi2)
def dL3N2dxi2(xi1,xi2,xi3):
    return diff(L3N2(xi1,xi2,xi3),xi2)
def dL3N3dxi2(xi1,xi2,xi3):
    return diff(L3N3(xi1,xi2,xi3),xi2)
def dL3N4dxi2(xi1,xi2,xi3):
    return diff(L3N4(xi1,xi2,xi3),xi2)

print("dL3N1dxi2 = %s\n"%(expand(dL3N1dxi2(xi1,xi2,xi3))))
print("dL3N2dxi2 = %s\n"%(expand(dL3N2dxi2(xi1,xi2,xi3))))
print("dL3N3dxi2 = %s\n"%(expand(dL3N3dxi2(xi1,xi2,xi3))))
print("dL3N4dxi2 = %s\n"%(expand(dL3N4dxi2(xi1,xi2,xi3))))

def dL3N1dxi3(xi1,xi2,xi3):
    return diff(L3N1(xi1,xi2,xi3),xi3)
def dL3N2dxi3(xi1,xi2,xi3):
    return diff(L3N2(xi1,xi2,xi3),xi3)
def dL3N3dxi3(xi1,xi2,xi3):
    return diff(L3N3(xi1,xi2,xi3),xi3)
def dL3N4dxi3(xi1,xi2,xi3):
    return diff(L3N4(xi1,xi2,xi3),xi3)

print("dL3N1dxi3 = %s\n"%(expand(dL3N1dxi3(xi1,xi2,xi3))))
print("dL3N2dxi3 = %s\n"%(expand(dL3N2dxi3(xi1,xi2,xi3))))
print("dL3N3dxi3 = %s\n"%(expand(dL3N3dxi3(xi1,xi2,xi3))))
print("dL3N4dxi3 = %s\n"%(expand(dL3N4dxi3(xi1,xi2,xi3))))

def d2L3N1dxi1dxi1(xi1,xi2,xi3):
    return diff(dL3N1dxi1(xi1,xi2,xi3),xi1)
def d2L3N2dxi1dxi1(xi1,xi2,xi3):
    return diff(dL3N2dxi1(xi1,xi2,xi3),xi1)
def d2L3N3dxi1dxi1(xi1,xi2,xi3):
    return diff(dL3N3dxi1(xi1,xi2,xi3),xi1)
def d2L3N4dxi1dxi1(xi1,xi2,xi3):
    return diff(dL3N4dxi1(xi1,xi2,xi3),xi1)

print("d2L3N1dxi1dxi1 = %s\n"%(expand(d2L3N1dxi1dxi1(xi1,xi2,xi3))))
print("d2L3N2dxi1dxi1 = %s\n"%(expand(d2L3N2dxi1dxi1(xi1,xi2,xi3))))
print("d2L3N3dxi1dxi1 = %s\n"%(expand(d2L3N3dxi1dxi1(xi1,xi2,xi3))))
print("d2L3N4dxi1dxi1 = %s\n"%(expand(d2L3N4dxi1dxi1(xi1,xi2,xi3))))

def d2L3N1dxi2dxi2(xi1,xi2,xi3):
    return diff(dL3N1dxi2(xi1,xi2,xi3),xi2)
def d2L3N2dxi2dxi2(xi1,xi2,xi3):
    return diff(dL3N2dxi2(xi1,xi2,xi3),xi2)
def d2L3N3dxi2dxi2(xi1,xi2,xi3):
    return diff(dL3N3dxi2(xi1,xi2,xi3),xi2)
def d2L3N4dxi2dxi2(xi1,xi2,xi3):
    return diff(dL3N4dxi2(xi1,xi2,xi3),xi2)

print("d2L3N1dxi2dxi2 = %s\n"%(expand(d2L3N1dxi2dxi2(xi1,xi2,xi3))))
print("d2L3N2dxi2dxi2 = %s\n"%(expand(d2L3N2dxi2dxi2(xi1,xi2,xi3))))
print("d2L3N3dxi2dxi2 = %s\n"%(expand(d2L3N3dxi2dxi2(xi1,xi2,xi3))))
print("d2L3N4dxi2dxi2 = %s\n"%(expand(d2L3N4dxi2dxi2(xi1,xi2,xi3))))

def d2L3N1dxi3dxi3(xi1,xi2,xi3):
    return diff(dL3N1dxi3(xi1,xi2,xi3),xi3)
def d2L3N2dxi3dxi3(xi1,xi2,xi3):
    return diff(dL3N2dxi3(xi1,xi2,xi3),xi3)
def d2L3N3dxi3dxi3(xi1,xi2,xi3):
    return diff(dL3N3dxi3(xi1,xi2,xi3),xi3)
def d2L3N4dxi3dxi3(xi1,xi2,xi3):
    return diff(dL3N4dxi3(xi1,xi2,xi3),xi3)

print("d2L3N1dxi3dxi3 = %s\n"%(expand(d2L3N1dxi3dxi3(xi1,xi2,xi3))))
print("d2L3N2dxi3dxi3 = %s\n"%(expand(d2L3N2dxi3dxi3(xi1,xi2,xi3))))
print("d2L3N3dxi3dxi3 = %s\n"%(expand(d2L3N3dxi3dxi3(xi1,xi2,xi3))))
print("d2L3N4dxi3dxi3 = %s\n"%(expand(d2L3N4dxi3dxi3(xi1,xi2,xi3))))

def d2L3N1dxi1dxi2(xi1,xi2,xi3):
    return diff(dL3N1dxi1(xi1,xi2,xi3),xi2)
def d2L3N2dxi1dxi2(xi1,xi2,xi3):
    return diff(dL3N2dxi1(xi1,xi2,xi3),xi2)
def d2L3N3dxi1dxi2(xi1,xi2,xi3):
    return diff(dL3N3dxi1(xi1,xi2,xi3),xi2)
def d2L3N4dxi1dxi2(xi1,xi2,xi3):
    return diff(dL3N4dxi1(xi1,xi2,xi3),xi2)

print("d2L3N1dxi1dxi2 = %s\n"%(expand(d2L3N1dxi1dxi2(xi1,xi2,xi3))))
print("d2L3N2dxi1dxi2 = %s\n"%(expand(d2L3N2dxi1dxi2(xi1,xi2,xi3))))
print("d2L3N3dxi1dxi2 = %s\n"%(expand(d2L3N3dxi1dxi2(xi1,xi2,xi3))))
print("d2L3N4dxi1dxi2 = %s\n"%(expand(d2L3N4dxi1dxi2(xi1,xi2,xi3))))

def d2L3N1dxi1dxi3(xi1,xi2,xi3):
    return diff(dL3N1dxi1(xi1,xi2,xi3),xi3)
def d2L3N2dxi1dxi3(xi1,xi2,xi3):
    return diff(dL3N2dxi1(xi1,xi2,xi3),xi3)
def d2L3N3dxi1dxi3(xi1,xi2,xi3):
    return diff(dL3N3dxi1(xi1,xi2,xi3),xi3)
def d2L3N4dxi1dxi3(xi1,xi2,xi3):
    return diff(dL3N4dxi1(xi1,xi2,xi3),xi3)

print("d2L3N1dxi1dxi3 = %s\n"%(expand(d2L3N1dxi1dxi3(xi1,xi2,xi3))))
print("d2L3N2dxi1dxi3 = %s\n"%(expand(d2L3N2dxi1dxi3(xi1,xi2,xi3))))
print("d2L3N3dxi1dxi3 = %s\n"%(expand(d2L3N3dxi1dxi3(xi1,xi2,xi3))))
print("d2L3N4dxi1dxi3 = %s\n"%(expand(d2L3N4dxi1dxi3(xi1,xi2,xi3))))

def d2L3N1dxi2dxi3(xi1,xi2,xi3):
    return diff(dL3N1dxi2(xi1,xi2,xi3),xi3)
def d2L3N2dxi2dxi3(xi1,xi2,xi3):
    return diff(dL3N2dxi2(xi1,xi2,xi3),xi3)
def d2L3N3dxi2dxi3(xi1,xi2,xi3):
    return diff(dL3N3dxi2(xi1,xi2,xi3),xi3)
def d2L3N4dxi2dxi3(xi1,xi2,xi3):
    return diff(dL3N4dxi2(xi1,xi2,xi3),xi3)

print("d2L3N1dxi2dxi3 = %s\n"%(expand(d2L3N1dxi2dxi3(xi1,xi2,xi3))))
print("d2L3N2dxi2dxi3 = %s\n"%(expand(d2L3N2dxi2dxi3(xi1,xi2,xi3))))
print("d2L3N3dxi2dxi3 = %s\n"%(expand(d2L3N3dxi2dxi3(xi1,xi2,xi3))))
print("d2L3N4dxi2dxi3 = %s\n"%(expand(d2L3N4dxi2dxi3(xi1,xi2,xi3))))

def d3L3N1dxi1dxi2dxi3(xi1,xi2,xi3):
    return diff(d2L3N1dxi1dxi2(xi1,xi2,xi3),xi3)
def d3L3N2dxi1dxi2dxi3(xi1,xi2,xi3):
    return diff(d2L3N2dxi1dxi2(xi1,xi2,xi3),xi3)
def d3L3N3dxi1dxi2dxi3(xi1,xi2,xi3):
    return diff(d2L3N3dxi1dxi2(xi1,xi2,xi3),xi3)
def d3L3N4dxi1dxi2dxi3(xi1,xi2,xi3):
    return diff(d2L3N4dxi1dxi2(xi1,xi2,xi3),xi3)

print("d3L3N1dxi1dxi2dxi3 = %s\n"%(expand(d3L3N1dxi1dxi2dxi3(xi1,xi2,xi3))))
print("d3L3N2dxi1dxi2dxi3 = %s\n"%(expand(d3L3N2dxi1dxi2dxi3(xi1,xi2,xi3))))
print("d3L3N3dxi1dxi2dxi3 = %s\n"%(expand(d3L3N3dxi1dxi2dxi3(xi1,xi2,xi3))))
print("d3L3N4dxi1dxi2dxi3 = %s\n"%(expand(d3L3N4dxi1dxi2dxi3(xi1,xi2,xi3))))

print("\n\nQuadratic Line Simplex Basis Functions:\n\n")

def Q1N1(xi):
    return l11(xi)*(2*l11(xi)-1)
def Q1N2(xi):
    return 4*l11(xi)*l12(xi)
def Q1N3(xi):
    return l12(xi)*(2*l12(xi)-1)

print("Q1N1 = %s\n"%(expand(Q1N1(xi))))
print("Q1N2 = %s\n"%(expand(Q1N2(xi))))
print("Q1N3 = %s\n"%(expand(Q1N3(xi))))

def dQ1N1dxi(xi):
    return diff(Q1N1(xi),xi)
def dQ1N2dxi(xi):
    return diff(Q1N2(xi),xi)
def dQ1N3dxi(xi):
    return diff(Q1N3(xi),xi)

print("dQ1N1dxi = %s\n"%(expand(dQ1N1dxi(xi))))
print("dQ1N2dxi = %s\n"%(expand(dQ1N2dxi(xi))))
print("dQ1N3dxi = %s\n"%(expand(dQ1N3dxi(xi))))

def d2Q1N1dxidxi(xi):
    return diff(dQ1N1dxi(xi),xi)
def d2Q1N2dxidxi(xi):
    return diff(dQ1N2dxi(xi),xi)
def d2Q1N3dxidxi(xi):
    return diff(dQ1N3dxi(xi),xi)

print("d2Q1N1dxidxi = %s\n"%(expand(d2Q1N1dxidxi(xi))))
print("d2Q1N2dxidxi = %s\n"%(expand(d2Q1N2dxidxi(xi))))
print("d2Q1N3dxidxi = %s\n"%(expand(d2Q1N3dxidxi(xi))))


print("\n\nQuadratic Triangle Simplex Basis Functions:\n\n")

def Q2N1(xi1,xi2):
    return l21(xi1,xi2)*(2*l21(xi1,xi2)-1)
def Q2N2(xi1,xi2):
    return l22(xi1,xi2)*(2*l22(xi1,xi2)-1)
def Q2N3(xi1,xi2):
    return l23(xi1,xi2)*(2*l23(xi1,xi2)-1)
def Q2N4(xi1,xi2):
    return 4*l21(xi1,xi2)*l22(xi1,xi2)
def Q2N5(xi1,xi2):
    return 4*l22(xi1,xi2)*l23(xi1,xi2)
def Q2N6(xi1,xi2):
    return 4*l21(xi1,xi2)*l23(xi1,xi2)

print("Q2N1 = %s\n"%(expand(Q2N1(xi1,xi2))))
print("Q2N2 = %s\n"%(expand(Q2N2(xi1,xi2))))
print("Q2N3 = %s\n"%(expand(Q2N3(xi1,xi2))))
print("Q2N4 = %s\n"%(expand(Q2N4(xi1,xi2))))
print("Q2N5 = %s\n"%(expand(Q2N5(xi1,xi2))))
print("Q2N6 = %s\n"%(expand(Q2N6(xi1,xi2))))

def dQ2N1dxi1(xi1,xi2):
    return diff(Q2N1(xi1,xi2),xi1)
def dQ2N2dxi1(xi1,xi2):
    return diff(Q2N2(xi1,xi2),xi1)
def dQ2N3dxi1(xi1,xi2):
    return diff(Q2N3(xi1,xi2),xi1)
def dQ2N4dxi1(xi1,xi2):
    return diff(Q2N4(xi1,xi2),xi1)
def dQ2N5dxi1(xi1,xi2):
    return diff(Q2N5(xi1,xi2),xi1)
def dQ2N6dxi1(xi1,xi2):
    return diff(Q2N6(xi1,xi2),xi1)

print("dQ2N1dxi1 = %s\n"%(expand(dQ2N1dxi1(xi1,xi2))))
print("dQ2N2dxi1 = %s\n"%(expand(dQ2N2dxi1(xi1,xi2))))
print("dQ2N3dxi1 = %s\n"%(expand(dQ2N3dxi1(xi1,xi2))))
print("dQ2N4dxi1 = %s\n"%(expand(dQ2N4dxi1(xi1,xi2))))
print("dQ2N5dxi1 = %s\n"%(expand(dQ2N5dxi1(xi1,xi2))))
print("dQ2N6dxi1 = %s\n"%(expand(dQ2N6dxi1(xi1,xi2))))

def dQ2N1dxi2(xi1,xi2):
    return diff(Q2N1(xi1,xi2),xi2)
def dQ2N2dxi2(xi1,xi2):
    return diff(Q2N2(xi1,xi2),xi2)
def dQ2N3dxi2(xi1,xi2):
    return diff(Q2N3(xi1,xi2),xi2)
def dQ2N4dxi2(xi1,xi2):
    return diff(Q2N4(xi1,xi2),xi2)
def dQ2N5dxi2(xi1,xi2):
    return diff(Q2N5(xi1,xi2),xi2)
def dQ2N6dxi2(xi1,xi2):
    return diff(Q2N6(xi1,xi2),xi2)

print("dQ2N1dxi2 = %s\n"%(expand(dQ2N1dxi2(xi1,xi2))))
print("dQ2N2dxi2 = %s\n"%(expand(dQ2N2dxi2(xi1,xi2))))
print("dQ2N3dxi2 = %s\n"%(expand(dQ2N3dxi2(xi1,xi2))))
print("dQ2N4dxi2 = %s\n"%(expand(dQ2N4dxi2(xi1,xi2))))
print("dQ2N5dxi2 = %s\n"%(expand(dQ2N5dxi2(xi1,xi2))))
print("dQ2N6dxi2 = %s\n"%(expand(dQ2N6dxi2(xi1,xi2))))

def d2Q2N1dxi1dxi1(xi1,xi2):
    return diff(dQ2N1dxi1(xi1,xi2),xi1)
def d2Q2N2dxi1dxi1(xi1,xi2):
    return diff(dQ2N2dxi1(xi1,xi2),xi1)
def d2Q2N3dxi1dxi1(xi1,xi2):
    return diff(dQ2N3dxi1(xi1,xi2),xi1)
def d2Q2N4dxi1dxi1(xi1,xi2):
    return diff(dQ2N4dxi1(xi1,xi2),xi1)
def d2Q2N5dxi1dxi1(xi1,xi2):
    return diff(dQ2N5dxi1(xi1,xi2),xi1)
def d2Q2N6dxi1dxi1(xi1,xi2):
    return diff(dQ2N6dxi1(xi1,xi2),xi1)

print("d2Q2N1dxi1dxi1 = %s\n"%(expand(d2Q2N1dxi1dxi1(xi1,xi2))))
print("d2Q2N2dxi1dxi1 = %s\n"%(expand(d2Q2N2dxi1dxi1(xi1,xi2))))
print("d2Q2N3dxi1dxi1 = %s\n"%(expand(d2Q2N3dxi1dxi1(xi1,xi2))))
print("d2Q2N4dxi1dxi1 = %s\n"%(expand(d2Q2N4dxi1dxi1(xi1,xi2))))
print("d2Q2N5dxi1dxi1 = %s\n"%(expand(d2Q2N5dxi1dxi1(xi1,xi2))))
print("d2Q2N6dxi1dxi1 = %s\n"%(expand(d2Q2N6dxi1dxi1(xi1,xi2))))

def d2Q2N1dxi2dxi2(xi1,xi2):
    return diff(dQ2N1dxi2(xi1,xi2),xi2)
def d2Q2N2dxi2dxi2(xi1,xi2):
    return diff(dQ2N2dxi2(xi1,xi2),xi2)
def d2Q2N3dxi2dxi2(xi1,xi2):
    return diff(dQ2N3dxi2(xi1,xi2),xi2)
def d2Q2N4dxi2dxi2(xi1,xi2):
    return diff(dQ2N4dxi2(xi1,xi2),xi2)
def d2Q2N5dxi2dxi2(xi1,xi2):
    return diff(dQ2N5dxi2(xi1,xi2),xi2)
def d2Q2N6dxi2dxi2(xi1,xi2):
    return diff(dQ2N6dxi2(xi1,xi2),xi2)

print("d2Q2N1dxi2dxi2 = %s\n"%(expand(d2Q2N1dxi2dxi2(xi1,xi2))))
print("d2Q2N2dxi2dxi2 = %s\n"%(expand(d2Q2N2dxi2dxi2(xi1,xi2))))
print("d2Q2N3dxi2dxi2 = %s\n"%(expand(d2Q2N3dxi2dxi2(xi1,xi2))))
print("d2Q2N4dxi2dxi2 = %s\n"%(expand(d2Q2N4dxi2dxi2(xi1,xi2))))
print("d2Q2N5dxi2dxi2 = %s\n"%(expand(d2Q2N5dxi2dxi2(xi1,xi2))))
print("d2Q2N6dxi2dxi2 = %s\n"%(expand(d2Q2N6dxi2dxi2(xi1,xi2))))

def d2Q2N1dxi1dxi2(xi1,xi2):
    return diff(dQ2N1dxi1(xi1,xi2),xi2)
def d2Q2N2dxi1dxi2(xi1,xi2):
    return diff(dQ2N2dxi1(xi1,xi2),xi2)
def d2Q2N3dxi1dxi2(xi1,xi2):
    return diff(dQ2N3dxi1(xi1,xi2),xi2)
def d2Q2N4dxi1dxi2(xi1,xi2):
    return diff(dQ2N4dxi1(xi1,xi2),xi2)
def d2Q2N5dxi1dxi2(xi1,xi2):
    return diff(dQ2N5dxi1(xi1,xi2),xi2)
def d2Q2N6dxi1dxi2(xi1,xi2):
    return diff(dQ2N6dxi1(xi1,xi2),xi2)

print("d2Q2N1dxi1dxi2 = %s\n"%(expand(d2Q2N1dxi1dxi2(xi1,xi2))))
print("d2Q2N2dxi1dxi2 = %s\n"%(expand(d2Q2N2dxi1dxi2(xi1,xi2))))
print("d2Q2N3dxi1dxi2 = %s\n"%(expand(d2Q2N3dxi1dxi2(xi1,xi2))))
print("d2Q2N4dxi1dxi2 = %s\n"%(expand(d2Q2N4dxi1dxi2(xi1,xi2))))
print("d2Q2N5dxi1dxi2 = %s\n"%(expand(d2Q2N5dxi1dxi2(xi1,xi2))))
print("d2Q2N6dxi1dxi2 = %s\n"%(expand(d2Q2N6dxi1dxi2(xi1,xi2))))


print("\n\nQuadratic Tetrahedral Simplex Basis Functions:\n\n")

def Q3N1(xi1,xi2,xi3):
    return l31(xi1,xi2,xi3)*(2*l31(xi1,xi2,xi3)-1)
def Q3N2(xi1,xi2,xi3):
    return l32(xi1,xi2,xi3)*(2*l32(xi1,xi2,xi3)-1)
def Q3N3(xi1,xi2,xi3):
    return l33(xi1,xi2,xi3)*(2*l33(xi1,xi2,xi3)-1)
def Q3N4(xi1,xi2,xi3):
    return l34(xi1,xi2,xi3)*(2*l34(xi1,xi2,xi3)-1)
def Q3N5(xi1,xi2,xi3):
    return 4*l31(xi1,xi2,xi3)*l32(xi1,xi2,xi3)
def Q3N6(xi1,xi2,xi3):
    return 4*l31(xi1,xi2,xi3)*l33(xi1,xi2,xi3)
def Q3N7(xi1,xi2,xi3):
    return 4*l31(xi1,xi2,xi3)*l34(xi1,xi2,xi3)
def Q3N8(xi1,xi2,xi3):
    return 4*l32(xi1,xi2,xi3)*l33(xi1,xi2,xi3)
def Q3N9(xi1,xi2,xi3):
    return 4*l33(xi1,xi2,xi3)*l34(xi1,xi2,xi3)
def Q3N10(xi1,xi2,xi3):
    return 4*l32(xi1,xi2,xi3)*l34(xi1,xi2,xi3)

print("Q3N1 = %s\n"%(expand(Q3N1(xi1,xi2,xi3))))
print("Q3N2 = %s\n"%(expand(Q3N2(xi1,xi2,xi3))))
print("Q3N3 = %s\n"%(expand(Q3N3(xi1,xi2,xi3))))
print("Q3N4 = %s\n"%(expand(Q3N4(xi1,xi2,xi3))))
print("Q3N5 = %s\n"%(expand(Q3N5(xi1,xi2,xi3))))
print("Q3N6 = %s\n"%(expand(Q3N6(xi1,xi2,xi3))))
print("Q3N7 = %s\n"%(expand(Q3N7(xi1,xi2,xi3))))
print("Q3N8 = %s\n"%(expand(Q3N8(xi1,xi2,xi3))))
print("Q3N9 = %s\n"%(expand(Q3N9(xi1,xi2,xi3))))
print("Q3N10 = %s\n"%(expand(Q3N10(xi1,xi2,xi3))))

def dQ3N1dxi1(xi1,xi2,xi3):
    return diff(Q3N1(xi1,xi2,xi3),xi1)
def dQ3N2dxi1(xi1,xi2,xi3):
    return diff(Q3N2(xi1,xi2,xi3),xi1)
def dQ3N3dxi1(xi1,xi2,xi3):
    return diff(Q3N3(xi1,xi2,xi3),xi1)
def dQ3N4dxi1(xi1,xi2,xi3):
    return diff(Q3N4(xi1,xi2,xi3),xi1)
def dQ3N5dxi1(xi1,xi2,xi3):
    return diff(Q3N5(xi1,xi2,xi3),xi1)
def dQ3N6dxi1(xi1,xi2,xi3):
    return diff(Q3N6(xi1,xi2,xi3),xi1)
def dQ3N7dxi1(xi1,xi2,xi3):
    return diff(Q3N7(xi1,xi2,xi3),xi1)
def dQ3N8dxi1(xi1,xi2,xi3):
    return diff(Q3N8(xi1,xi2,xi3),xi1)
def dQ3N9dxi1(xi1,xi2,xi3):
    return diff(Q3N9(xi1,xi2,xi3),xi1)
def dQ3N10dxi1(xi1,xi2,xi3):
    return diff(Q3N10(xi1,xi2,xi3),xi1)

print("dQ3N1dxi1 = %s\n"%(expand(dQ3N1dxi1(xi1,xi2,xi3))))
print("dQ3N2dxi1 = %s\n"%(expand(dQ3N2dxi1(xi1,xi2,xi3))))
print("dQ3N3dxi1 = %s\n"%(expand(dQ3N3dxi1(xi1,xi2,xi3))))
print("dQ3N4dxi1 = %s\n"%(expand(dQ3N4dxi1(xi1,xi2,xi3))))
print("dQ3N5dxi1 = %s\n"%(expand(dQ3N5dxi1(xi1,xi2,xi3))))
print("dQ3N6dxi1 = %s\n"%(expand(dQ3N6dxi1(xi1,xi2,xi3))))
print("dQ3N7dxi1 = %s\n"%(expand(dQ3N7dxi1(xi1,xi2,xi3))))
print("dQ3N8dxi1 = %s\n"%(expand(dQ3N8dxi1(xi1,xi2,xi3))))
print("dQ3N9dxi1 = %s\n"%(expand(dQ3N9dxi1(xi1,xi2,xi3))))
print("dQ3N10dxi1 = %s\n"%(expand(dQ3N10dxi1(xi1,xi2,xi3))))

def dQ3N1dxi2(xi1,xi2,xi3):
    return diff(Q3N1(xi1,xi2,xi3),xi2)
def dQ3N2dxi2(xi1,xi2,xi3):
    return diff(Q3N2(xi1,xi2,xi3),xi2)
def dQ3N3dxi2(xi1,xi2,xi3):
    return diff(Q3N3(xi1,xi2,xi3),xi2)
def dQ3N4dxi2(xi1,xi2,xi3):
    return diff(Q3N4(xi1,xi2,xi3),xi2)
def dQ3N5dxi2(xi1,xi2,xi3):
    return diff(Q3N5(xi1,xi2,xi3),xi2)
def dQ3N6dxi2(xi1,xi2,xi3):
    return diff(Q3N6(xi1,xi2,xi3),xi2)
def dQ3N7dxi2(xi1,xi2,xi3):
    return diff(Q3N7(xi1,xi2,xi3),xi2)
def dQ3N8dxi2(xi1,xi2,xi3):
    return diff(Q3N8(xi1,xi2,xi3),xi2)
def dQ3N9dxi2(xi1,xi2,xi3):
    return diff(Q3N9(xi1,xi2,xi3),xi2)
def dQ3N10dxi2(xi1,xi2,xi3):
    return diff(Q3N10(xi1,xi2,xi3),xi2)

print("dQ3N1dxi2 = %s\n"%(expand(dQ3N1dxi2(xi1,xi2,xi3))))
print("dQ3N2dxi2 = %s\n"%(expand(dQ3N2dxi2(xi1,xi2,xi3))))
print("dQ3N3dxi2 = %s\n"%(expand(dQ3N3dxi2(xi1,xi2,xi3))))
print("dQ3N4dxi2 = %s\n"%(expand(dQ3N4dxi2(xi1,xi2,xi3))))
print("dQ3N5dxi2 = %s\n"%(expand(dQ3N5dxi2(xi1,xi2,xi3))))
print("dQ3N6dxi2 = %s\n"%(expand(dQ3N6dxi2(xi1,xi2,xi3))))
print("dQ3N7dxi2 = %s\n"%(expand(dQ3N7dxi2(xi1,xi2,xi3))))
print("dQ3N8dxi2 = %s\n"%(expand(dQ3N8dxi2(xi1,xi2,xi3))))
print("dQ3N9dxi2 = %s\n"%(expand(dQ3N9dxi2(xi1,xi2,xi3))))
print("dQ3N10dxi2 = %s\n"%(expand(dQ3N10dxi2(xi1,xi2,xi3))))

def dQ3N1dxi3(xi1,xi2,xi3):
    return diff(Q3N1(xi1,xi2,xi3),xi3)
def dQ3N2dxi3(xi1,xi2,xi3):
    return diff(Q3N2(xi1,xi2,xi3),xi3)
def dQ3N3dxi3(xi1,xi2,xi3):
    return diff(Q3N3(xi1,xi2,xi3),xi3)
def dQ3N4dxi3(xi1,xi2,xi3):
    return diff(Q3N4(xi1,xi2,xi3),xi3)
def dQ3N5dxi3(xi1,xi2,xi3):
    return diff(Q3N5(xi1,xi2,xi3),xi3)
def dQ3N6dxi3(xi1,xi2,xi3):
    return diff(Q3N6(xi1,xi2,xi3),xi3)
def dQ3N7dxi3(xi1,xi2,xi3):
    return diff(Q3N7(xi1,xi2,xi3),xi3)
def dQ3N8dxi3(xi1,xi2,xi3):
    return diff(Q3N8(xi1,xi2,xi3),xi3)
def dQ3N9dxi3(xi1,xi2,xi3):
    return diff(Q3N9(xi1,xi2,xi3),xi3)
def dQ3N10dxi3(xi1,xi2,xi3):
    return diff(Q3N10(xi1,xi2,xi3),xi3)

print("dQ3N1dxi3 = %s\n"%(expand(dQ3N1dxi3(xi1,xi2,xi3))))
print("dQ3N2dxi3 = %s\n"%(expand(dQ3N2dxi3(xi1,xi2,xi3))))
print("dQ3N3dxi3 = %s\n"%(expand(dQ3N3dxi3(xi1,xi2,xi3))))
print("dQ3N4dxi3 = %s\n"%(expand(dQ3N4dxi3(xi1,xi2,xi3))))
print("dQ3N5dxi3 = %s\n"%(expand(dQ3N5dxi3(xi1,xi2,xi3))))
print("dQ3N6dxi3 = %s\n"%(expand(dQ3N6dxi3(xi1,xi2,xi3))))
print("dQ3N7dxi3 = %s\n"%(expand(dQ3N7dxi3(xi1,xi2,xi3))))
print("dQ3N8dxi3 = %s\n"%(expand(dQ3N8dxi3(xi1,xi2,xi3))))
print("dQ3N9dxi3 = %s\n"%(expand(dQ3N9dxi3(xi1,xi2,xi3))))
print("dQ3N10dxi3 = %s\n"%(expand(dQ3N10dxi3(xi1,xi2,xi3))))

def d2Q3N1dxi1dxi1(xi1,xi2,xi3):
    return diff(dQ3N1dxi1(xi1,xi2,xi3),xi1)
def d2Q3N2dxi1dxi1(xi1,xi2,xi3):
    return diff(dQ3N2dxi1(xi1,xi2,xi3),xi1)
def d2Q3N3dxi1dxi1(xi1,xi2,xi3):
    return diff(dQ3N3dxi1(xi1,xi2,xi3),xi1)
def d2Q3N4dxi1dxi1(xi1,xi2,xi3):
    return diff(dQ3N4dxi1(xi1,xi2,xi3),xi1)
def d2Q3N5dxi1dxi1(xi1,xi2,xi3):
    return diff(dQ3N5dxi1(xi1,xi2,xi3),xi1)
def d2Q3N6dxi1dxi1(xi1,xi2,xi3):
    return diff(dQ3N6dxi1(xi1,xi2,xi3),xi1)
def d2Q3N7dxi1dxi1(xi1,xi2,xi3):
    return diff(dQ3N7dxi1(xi1,xi2,xi3),xi1)
def d2Q3N8dxi1dxi1(xi1,xi2,xi3):
    return diff(dQ3N8dxi1(xi1,xi2,xi3),xi1)
def d2Q3N9dxi1dxi1(xi1,xi2,xi3):
    return diff(dQ3N9dxi1(xi1,xi2,xi3),xi1)
def d2Q3N10dxi1dxi1(xi1,xi2,xi3):
    return diff(dQ3N10dxi1(xi1,xi2,xi3),xi1)

print("d2Q3N1dxi1dxi1 = %s\n"%(expand(d2Q3N1dxi1dxi1(xi1,xi2,xi3))))
print("d2Q3N2dxi1dxi1 = %s\n"%(expand(d2Q3N2dxi1dxi1(xi1,xi2,xi3))))
print("d2Q3N3dxi1dxi1 = %s\n"%(expand(d2Q3N3dxi1dxi1(xi1,xi2,xi3))))
print("d2Q3N4dxi1dxi1 = %s\n"%(expand(d2Q3N4dxi1dxi1(xi1,xi2,xi3))))
print("d2Q3N5dxi1dxi1 = %s\n"%(expand(d2Q3N5dxi1dxi1(xi1,xi2,xi3))))
print("d2Q3N6dxi1dxi1 = %s\n"%(expand(d2Q3N6dxi1dxi1(xi1,xi2,xi3))))
print("d2Q3N7dxi1dxi1 = %s\n"%(expand(d2Q3N7dxi1dxi1(xi1,xi2,xi3))))
print("d2Q3N8dxi1dxi1 = %s\n"%(expand(d2Q3N8dxi1dxi1(xi1,xi2,xi3))))
print("d2Q3N9dxi1dxi1 = %s\n"%(expand(d2Q3N9dxi1dxi1(xi1,xi2,xi3))))
print("d2Q3N10dxi1dxi1 = %s\n"%(expand(d2Q3N10dxi1dxi1(xi1,xi2,xi3))))

def d2Q3N1dxi2dxi2(xi1,xi2,xi3):
    return diff(dQ3N1dxi2(xi1,xi2,xi3),xi2)
def d2Q3N2dxi2dxi2(xi1,xi2,xi3):
    return diff(dQ3N2dxi2(xi1,xi2,xi3),xi2)
def d2Q3N3dxi2dxi2(xi1,xi2,xi3):
    return diff(dQ3N3dxi2(xi1,xi2,xi3),xi2)
def d2Q3N4dxi2dxi2(xi1,xi2,xi3):
    return diff(dQ3N4dxi2(xi1,xi2,xi3),xi2)
def d2Q3N5dxi2dxi2(xi1,xi2,xi3):
    return diff(dQ3N5dxi2(xi1,xi2,xi3),xi2)
def d2Q3N6dxi2dxi2(xi1,xi2,xi3):
    return diff(dQ3N6dxi2(xi1,xi2,xi3),xi2)
def d2Q3N7dxi2dxi2(xi1,xi2,xi3):
    return diff(dQ3N7dxi2(xi1,xi2,xi3),xi2)
def d2Q3N8dxi2dxi2(xi1,xi2,xi3):
    return diff(dQ3N8dxi2(xi1,xi2,xi3),xi2)
def d2Q3N9dxi2dxi2(xi1,xi2,xi3):
    return diff(dQ3N9dxi2(xi1,xi2,xi3),xi2)
def d2Q3N10dxi2dxi2(xi1,xi2,xi3):
    return diff(dQ3N10dxi2(xi1,xi2,xi3),xi2)

print("d2Q3N1dxi2dxi2 = %s\n"%(expand(d2Q3N1dxi2dxi2(xi1,xi2,xi3))))
print("d2Q3N2dxi2dxi2 = %s\n"%(expand(d2Q3N2dxi2dxi2(xi1,xi2,xi3))))
print("d2Q3N3dxi2dxi2 = %s\n"%(expand(d2Q3N3dxi2dxi2(xi1,xi2,xi3))))
print("d2Q3N4dxi2dxi2 = %s\n"%(expand(d2Q3N4dxi2dxi2(xi1,xi2,xi3))))
print("d2Q3N5dxi2dxi2 = %s\n"%(expand(d2Q3N5dxi2dxi2(xi1,xi2,xi3))))
print("d2Q3N6dxi2dxi2 = %s\n"%(expand(d2Q3N6dxi2dxi2(xi1,xi2,xi3))))
print("d2Q3N7dxi2dxi2 = %s\n"%(expand(d2Q3N7dxi2dxi2(xi1,xi2,xi3))))
print("d2Q3N8dxi2dxi2 = %s\n"%(expand(d2Q3N8dxi2dxi2(xi1,xi2,xi3))))
print("d2Q3N9dxi2dxi2 = %s\n"%(expand(d2Q3N9dxi2dxi2(xi1,xi2,xi3))))
print("d2Q3N10dxi2dxi2 = %s\n"%(expand(d2Q3N10dxi2dxi2(xi1,xi2,xi3))))

def d2Q3N1dxi3dxi3(xi1,xi2,xi3):
    return diff(dQ3N1dxi3(xi1,xi2,xi3),xi3)
def d2Q3N2dxi3dxi3(xi1,xi2,xi3):
    return diff(dQ3N2dxi3(xi1,xi2,xi3),xi3)
def d2Q3N3dxi3dxi3(xi1,xi2,xi3):
    return diff(dQ3N3dxi3(xi1,xi2,xi3),xi3)
def d2Q3N4dxi3dxi3(xi1,xi2,xi3):
    return diff(dQ3N4dxi3(xi1,xi2,xi3),xi3)
def d2Q3N5dxi3dxi3(xi1,xi2,xi3):
    return diff(dQ3N5dxi3(xi1,xi2,xi3),xi3)
def d2Q3N6dxi3dxi3(xi1,xi2,xi3):
    return diff(dQ3N6dxi3(xi1,xi2,xi3),xi3)
def d2Q3N7dxi3dxi3(xi1,xi2,xi3):
    return diff(dQ3N7dxi3(xi1,xi2,xi3),xi3)
def d2Q3N8dxi3dxi3(xi1,xi2,xi3):
    return diff(dQ3N8dxi3(xi1,xi2,xi3),xi3)
def d2Q3N9dxi3dxi3(xi1,xi2,xi3):
    return diff(dQ3N9dxi3(xi1,xi2,xi3),xi3)
def d2Q3N10dxi3dxi3(xi1,xi2,xi3):
    return diff(dQ3N10dxi3(xi1,xi2,xi3),xi3)

print("d2Q3N1dxi3dxi3 = %s\n"%(expand(d2Q3N1dxi3dxi3(xi1,xi2,xi3))))
print("d2Q3N2dxi3dxi3 = %s\n"%(expand(d2Q3N2dxi3dxi3(xi1,xi2,xi3))))
print("d2Q3N3dxi3dxi3 = %s\n"%(expand(d2Q3N3dxi3dxi3(xi1,xi2,xi3))))
print("d2Q3N4dxi3dxi3 = %s\n"%(expand(d2Q3N4dxi3dxi3(xi1,xi2,xi3))))
print("d2Q3N5dxi3dxi3 = %s\n"%(expand(d2Q3N5dxi3dxi3(xi1,xi2,xi3))))
print("d2Q3N6dxi3dxi3 = %s\n"%(expand(d2Q3N6dxi3dxi3(xi1,xi2,xi3))))
print("d2Q3N7dxi3dxi3 = %s\n"%(expand(d2Q3N7dxi3dxi3(xi1,xi2,xi3))))
print("d2Q3N8dxi3dxi3 = %s\n"%(expand(d2Q3N8dxi3dxi3(xi1,xi2,xi3))))
print("d2Q3N9dxi3dxi3 = %s\n"%(expand(d2Q3N9dxi3dxi3(xi1,xi2,xi3))))
print("d2Q3N10dxi3dxi3 = %s\n"%(expand(d2Q3N10dxi3dxi3(xi1,xi2,xi3))))

def d2Q3N1dxi1dxi2(xi1,xi2,xi3):
    return diff(dQ3N1dxi1(xi1,xi2,xi3),xi2)
def d2Q3N2dxi1dxi2(xi1,xi2,xi3):
    return diff(dQ3N2dxi1(xi1,xi2,xi3),xi2)
def d2Q3N3dxi1dxi2(xi1,xi2,xi3):
    return diff(dQ3N3dxi1(xi1,xi2,xi3),xi2)
def d2Q3N4dxi1dxi2(xi1,xi2,xi3):
    return diff(dQ3N4dxi1(xi1,xi2,xi3),xi2)
def d2Q3N5dxi1dxi2(xi1,xi2,xi3):
    return diff(dQ3N5dxi1(xi1,xi2,xi3),xi2)
def d2Q3N6dxi1dxi2(xi1,xi2,xi3):
    return diff(dQ3N6dxi1(xi1,xi2,xi3),xi2)
def d2Q3N7dxi1dxi2(xi1,xi2,xi3):
    return diff(dQ3N7dxi1(xi1,xi2,xi3),xi2)
def d2Q3N8dxi1dxi2(xi1,xi2,xi3):
    return diff(dQ3N8dxi1(xi1,xi2,xi3),xi2)
def d2Q3N9dxi1dxi2(xi1,xi2,xi3):
    return diff(dQ3N9dxi1(xi1,xi2,xi3),xi2)
def d2Q3N10dxi1dxi2(xi1,xi2,xi3):
    return diff(dQ3N10dxi1(xi1,xi2,xi3),xi2)

print("d2Q3N1dxi1dxi2 = %s\n"%(expand(d2Q3N1dxi1dxi2(xi1,xi2,xi3))))
print("d2Q3N2dxi1dxi2 = %s\n"%(expand(d2Q3N2dxi1dxi2(xi1,xi2,xi3))))
print("d2Q3N3dxi1dxi2 = %s\n"%(expand(d2Q3N3dxi1dxi2(xi1,xi2,xi3))))
print("d2Q3N4dxi1dxi2 = %s\n"%(expand(d2Q3N4dxi1dxi2(xi1,xi2,xi3))))
print("d2Q3N5dxi1dxi2 = %s\n"%(expand(d2Q3N5dxi1dxi2(xi1,xi2,xi3))))
print("d2Q3N6dxi1dxi2 = %s\n"%(expand(d2Q3N6dxi1dxi2(xi1,xi2,xi3))))
print("d2Q3N7dxi1dxi2 = %s\n"%(expand(d2Q3N7dxi1dxi2(xi1,xi2,xi3))))
print("d2Q3N8dxi1dxi2 = %s\n"%(expand(d2Q3N8dxi1dxi2(xi1,xi2,xi3))))
print("d2Q3N9dxi1dxi2 = %s\n"%(expand(d2Q3N9dxi1dxi2(xi1,xi2,xi3))))
print("d2Q3N10dxi1dxi2 = %s\n"%(expand(d2Q3N10dxi1dxi2(xi1,xi2,xi3))))

def d2Q3N1dxi1dxi3(xi1,xi2,xi3):
    return diff(dQ3N1dxi1(xi1,xi2,xi3),xi3)
def d2Q3N2dxi1dxi3(xi1,xi2,xi3):
    return diff(dQ3N2dxi1(xi1,xi2,xi3),xi3)
def d2Q3N3dxi1dxi3(xi1,xi2,xi3):
    return diff(dQ3N3dxi1(xi1,xi2,xi3),xi3)
def d2Q3N4dxi1dxi3(xi1,xi2,xi3):
    return diff(dQ3N4dxi1(xi1,xi2,xi3),xi3)
def d2Q3N5dxi1dxi3(xi1,xi2,xi3):
    return diff(dQ3N5dxi1(xi1,xi2,xi3),xi3)
def d2Q3N6dxi1dxi3(xi1,xi2,xi3):
    return diff(dQ3N6dxi1(xi1,xi2,xi3),xi3)
def d2Q3N7dxi1dxi3(xi1,xi2,xi3):
    return diff(dQ3N7dxi1(xi1,xi2,xi3),xi3)
def d2Q3N8dxi1dxi3(xi1,xi2,xi3):
    return diff(dQ3N8dxi1(xi1,xi2,xi3),xi3)
def d2Q3N9dxi1dxi3(xi1,xi2,xi3):
    return diff(dQ3N9dxi1(xi1,xi2,xi3),xi3)
def d2Q3N10dxi1dxi3(xi1,xi2,xi3):
    return diff(dQ3N10dxi1(xi1,xi2,xi3),xi3)

print("d2Q3N1dxi1dxi3 = %s\n"%(expand(d2Q3N1dxi1dxi3(xi1,xi2,xi3))))
print("d2Q3N2dxi1dxi3 = %s\n"%(expand(d2Q3N2dxi1dxi3(xi1,xi2,xi3))))
print("d2Q3N3dxi1dxi3 = %s\n"%(expand(d2Q3N3dxi1dxi3(xi1,xi2,xi3))))
print("d2Q3N4dxi1dxi3 = %s\n"%(expand(d2Q3N4dxi1dxi3(xi1,xi2,xi3))))
print("d2Q3N5dxi1dxi3 = %s\n"%(expand(d2Q3N5dxi1dxi3(xi1,xi2,xi3))))
print("d2Q3N6dxi1dxi3 = %s\n"%(expand(d2Q3N6dxi1dxi3(xi1,xi2,xi3))))
print("d2Q3N7dxi1dxi3 = %s\n"%(expand(d2Q3N7dxi1dxi3(xi1,xi2,xi3))))
print("d2Q3N8dxi1dxi3 = %s\n"%(expand(d2Q3N8dxi1dxi3(xi1,xi2,xi3))))
print("d2Q3N9dxi1dxi3 = %s\n"%(expand(d2Q3N9dxi1dxi3(xi1,xi2,xi3))))
print("d2Q3N10dxi1dxi3 = %s\n"%(expand(d2Q3N10dxi1dxi3(xi1,xi2,xi3))))

def d2Q3N1dxi2dxi3(xi1,xi2,xi3):
    return diff(dQ3N1dxi2(xi1,xi2,xi3),xi3)
def d2Q3N2dxi2dxi3(xi1,xi2,xi3):
    return diff(dQ3N2dxi2(xi1,xi2,xi3),xi3)
def d2Q3N3dxi2dxi3(xi1,xi2,xi3):
    return diff(dQ3N3dxi2(xi1,xi2,xi3),xi3)
def d2Q3N4dxi2dxi3(xi1,xi2,xi3):
    return diff(dQ3N4dxi2(xi1,xi2,xi3),xi3)
def d2Q3N5dxi2dxi3(xi1,xi2,xi3):
    return diff(dQ3N5dxi2(xi1,xi2,xi3),xi3)
def d2Q3N6dxi2dxi3(xi1,xi2,xi3):
    return diff(dQ3N6dxi2(xi1,xi2,xi3),xi3)
def d2Q3N7dxi2dxi3(xi1,xi2,xi3):
    return diff(dQ3N7dxi2(xi1,xi2,xi3),xi3)
def d2Q3N8dxi2dxi3(xi1,xi2,xi3):
    return diff(dQ3N8dxi2(xi1,xi2,xi3),xi3)
def d2Q3N9dxi2dxi3(xi1,xi2,xi3):
    return diff(dQ3N9dxi2(xi1,xi2,xi3),xi3)
def d2Q3N10dxi2dxi3(xi1,xi2,xi3):
    return diff(dQ3N10dxi2(xi1,xi2,xi3),xi3)

print("d2Q3N1dxi2dxi3 = %s\n"%(expand(d2Q3N1dxi2dxi3(xi1,xi2,xi3))))
print("d2Q3N2dxi2dxi3 = %s\n"%(expand(d2Q3N2dxi2dxi3(xi1,xi2,xi3))))
print("d2Q3N3dxi2dxi3 = %s\n"%(expand(d2Q3N3dxi2dxi3(xi1,xi2,xi3))))
print("d2Q3N4dxi2dxi3 = %s\n"%(expand(d2Q3N4dxi2dxi3(xi1,xi2,xi3))))
print("d2Q3N5dxi2dxi3 = %s\n"%(expand(d2Q3N5dxi2dxi3(xi1,xi2,xi3))))
print("d2Q3N6dxi2dxi3 = %s\n"%(expand(d2Q3N6dxi2dxi3(xi1,xi2,xi3))))
print("d2Q3N7dxi2dxi3 = %s\n"%(expand(d2Q3N7dxi2dxi3(xi1,xi2,xi3))))
print("d2Q3N8dxi2dxi3 = %s\n"%(expand(d2Q3N8dxi2dxi3(xi1,xi2,xi3))))
print("d2Q3N9dxi2dxi3 = %s\n"%(expand(d2Q3N9dxi2dxi3(xi1,xi2,xi3))))
print("d2Q3N10dxi2dxi3 = %s\n"%(expand(d2Q3N10dxi2dxi3(xi1,xi2,xi3))))

def d3Q3N1dxi1dxi2dxi3(xi1,xi2,xi3):
    return diff(d2Q3N1dxi1dxi2(xi1,xi2,xi3),xi3)
def d3Q3N2dxi1dxi2dxi3(xi1,xi2,xi3):
    return diff(d2Q3N2dxi1dxi2(xi1,xi2,xi3),xi3)
def d3Q3N3dxi1dxi2dxi3(xi1,xi2,xi3):
    return diff(d2Q3N3dxi1dxi2(xi1,xi2,xi3),xi3)
def d3Q3N4dxi1dxi2dxi3(xi1,xi2,xi3):
    return diff(d2Q3N4dxi1dxi2(xi1,xi2,xi3),xi3)
def d3Q3N5dxi1dxi2dxi3(xi1,xi2,xi3):
    return diff(d2Q3N5dxi1dxi2(xi1,xi2,xi3),xi3)
def d3Q3N6dxi1dxi2dxi3(xi1,xi2,xi3):
    return diff(d2Q3N6dxi1dxi2(xi1,xi2,xi3),xi3)
def d3Q3N7dxi1dxi2dxi3(xi1,xi2,xi3):
    return diff(d2Q3N7dxi1dxi2(xi1,xi2,xi3),xi3)
def d3Q3N8dxi1dxi2dxi3(xi1,xi2,xi3):
    return diff(d2Q3N8dxi1dxi2(xi1,xi2,xi3),xi3)
def d3Q3N9dxi1dxi2dxi3(xi1,xi2,xi3):
    return diff(d2Q3N9dxi1dxi2(xi1,xi2,xi3),xi3)
def d3Q3N10dxi1dxi2dxi3(xi1,xi2,xi3):
    return diff(d2Q3N10dxi1dxi2(xi1,xi2,xi3),xi3)

print("d3Q3N1dxi1dxi2dxi3 = %s\n"%(expand(d3Q3N1dxi1dxi2dxi3(xi1,xi2,xi3))))
print("d3Q3N2dxi1dxi2dxi3 = %s\n"%(expand(d3Q3N2dxi1dxi2dxi3(xi1,xi2,xi3))))
print("d3Q3N3dxi1dxi2dxi3 = %s\n"%(expand(d3Q3N3dxi1dxi2dxi3(xi1,xi2,xi3))))
print("d3Q3N4dxi1dxi2dxi3 = %s\n"%(expand(d3Q3N4dxi1dxi2dxi3(xi1,xi2,xi3))))
print("d3Q3N5dxi1dxi2dxi3 = %s\n"%(expand(d3Q3N5dxi1dxi2dxi3(xi1,xi2,xi3))))
print("d3Q3N6dxi1dxi2dxi3 = %s\n"%(expand(d3Q3N6dxi1dxi2dxi3(xi1,xi2,xi3))))
print("d3Q3N7dxi1dxi2dxi3 = %s\n"%(expand(d3Q3N7dxi1dxi2dxi3(xi1,xi2,xi3))))
print("d3Q3N8dxi1dxi2dxi3 = %s\n"%(expand(d3Q3N8dxi1dxi2dxi3(xi1,xi2,xi3))))
print("d3Q3N9dxi1dxi2dxi3 = %s\n"%(expand(d3Q3N9dxi1dxi2dxi3(xi1,xi2,xi3))))
print("d3Q3N10dxi1dxi2dxi3 = %s\n"%(expand(d3Q3N10dxi1dxi2dxi3(xi1,xi2,xi3))))


print("\n\nCubic Line Simplex Basis Functions:\n\n")

def C1N1(xi):
    return 1/2*l11(xi)*(3*l11(xi)-1)*(3*l11(xi)-1)
def C1N2(xi):
    return 9/2*l11(xi)*(3*l11(xi)-1)*l12(xi)
def C1N3(xi):
    return 9/2*l11(xi)*(3*l12(xi)-1)*l12(xi)
def C1N4(xi):
    return 1/2*l12(xi)*(3*l12(xi)-1)*(3*l12(xi)-1)

print("C1N1 = %s\n"%(expand(C1N1(xi))))
print("C1N2 = %s\n"%(expand(C1N2(xi))))
print("C1N3 = %s\n"%(expand(C1N3(xi))))
print("C1N4 = %s\n"%(expand(C1N4(xi))))

def dC1N1dxi(xi):
    return diff(C1N1(xi),xi)
def dC1N2dxi(xi):
    return diff(C1N2(xi),xi)
def dC1N3dxi(xi):
    return diff(C1N3(xi),xi)
def dC1N4dxi(xi):
    return diff(C1N4(xi),xi)

print("dC1N1dxi = %s\n"%(expand(dC1N1dxi(xi))))
print("dC1N2dxi = %s\n"%(expand(dC1N2dxi(xi))))
print("dC1N3dxi = %s\n"%(expand(dC1N3dxi(xi))))
print("dC1N4dxi = %s\n"%(expand(dC1N4dxi(xi))))

def d2C1N1dxidxi(xi):
    return diff(dC1N1dxi(xi),xi)
def d2C1N2dxidxi(xi):
    return diff(dC1N2dxi(xi),xi)
def d2C1N3dxidxi(xi):
    return diff(dC1N3dxi(xi),xi)
def d2C1N4dxidxi(xi):
    return diff(dC1N4dxi(xi),xi)

print("d2C1N1dxidxi = %s\n"%(expand(d2C1N1dxidxi(xi))))
print("d2C1N2dxidxi = %s\n"%(expand(d2C1N2dxidxi(xi))))
print("d2C1N3dxidxi = %s\n"%(expand(d2C1N3dxidxi(xi))))
print("d2C1N4dxidxi = %s\n"%(expand(d2C1N4dxidxi(xi))))

print("\n\nCubic Triangle Simplex Basis Functions:\n\n")

def C2N1(xi1,xi2):
    return 1/2*l21(xi1,xi2)*(3*l21(xi1,xi2)-1)*(3*l21(xi1,xi2)-2)
def C2N2(xi1,xi2):
    return 1/2*l22(xi1,xi2)*(3*l22(xi1,xi2)-1)*(3*l22(xi1,xi2)-2)
def C2N3(xi1,xi2):
    return 1/2*l23(xi1,xi2)*(3*l23(xi1,xi2)-1)*(3*l23(xi1,xi2)-2)
def C2N4(xi1,xi2):
    return 9/2*l21(xi1,xi2)*(3*l21(xi1,xi2)-1)*l22(xi1,xi2)
def C2N5(xi1,xi2):
    return 9/2*l21(xi1,xi2)*(3*l22(xi1,xi2)-1)*l22(xi1,xi2)
def C2N6(xi1,xi2):
    return 9/2*l22(xi1,xi2)*(3*l22(xi1,xi2)-1)*l23(xi1,xi2)
def C2N7(xi1,xi2):
    return 9/2*l22(xi1,xi2)*(3*l23(xi1,xi2)-1)*l23(xi1,xi2)
def C2N8(xi1,xi2):
    return 9/2*l21(xi1,xi2)*(3*l23(xi1,xi2)-1)*l23(xi1,xi2)
def C2N9(xi1,xi2):
    return 9/2*l21(xi1,xi2)*(3*l21(xi1,xi2)-1)*l23(xi1,xi2)
def C2N10(xi1,xi2):
    return 27*l21(xi1,xi2)*l22(xi1,xi2)*l23(xi1,xi2)

print("C2N1 = %s\n"%(expand(C2N1(xi1,xi2))))
print("C2N2 = %s\n"%(expand(C2N2(xi1,xi2))))
print("C2N3 = %s\n"%(expand(C2N3(xi1,xi2))))
print("C2N4 = %s\n"%(expand(C2N4(xi1,xi2))))
print("C2N5 = %s\n"%(expand(C2N5(xi1,xi2))))
print("C2N6 = %s\n"%(expand(C2N6(xi1,xi2))))
print("C2N7 = %s\n"%(expand(C2N7(xi1,xi2))))
print("C2N8 = %s\n"%(expand(C2N8(xi1,xi2))))
print("C2N9 = %s\n"%(expand(C2N9(xi1,xi2))))
print("C2N10 = %s\n"%(expand(C2N10(xi1,xi2))))

def dC2N1dxi1(xi1,xi2):
    return diff(C2N1(xi1,xi2),xi1)
def dC2N2dxi1(xi1,xi2):
    return diff(C2N2(xi1,xi2),xi1)
def dC2N3dxi1(xi1,xi2):
    return diff(C2N3(xi1,xi2),xi1)
def dC2N4dxi1(xi1,xi2):
    return diff(C2N4(xi1,xi2),xi1)
def dC2N5dxi1(xi1,xi2):
    return diff(C2N5(xi1,xi2),xi1)
def dC2N6dxi1(xi1,xi2):
    return diff(C2N6(xi1,xi2),xi1)
def dC2N7dxi1(xi1,xi2):
    return diff(C2N7(xi1,xi2),xi1)
def dC2N8dxi1(xi1,xi2):
    return diff(C2N8(xi1,xi2),xi1)
def dC2N9dxi1(xi1,xi2):
    return diff(C2N9(xi1,xi2),xi1)
def dC2N10dxi1(xi1,xi2):
    return diff(C2N10(xi1,xi2),xi1)

print("dC2N1dxi1 = %s\n"%(expand(dC2N1dxi1(xi1,xi2))))
print("dC2N2dxi1 = %s\n"%(expand(dC2N2dxi1(xi1,xi2))))
print("dC2N3dxi1 = %s\n"%(expand(dC2N3dxi1(xi1,xi2))))
print("dC2N4dxi1 = %s\n"%(expand(dC2N4dxi1(xi1,xi2))))
print("dC2N5dxi1 = %s\n"%(expand(dC2N5dxi1(xi1,xi2))))
print("dC2N6dxi1 = %s\n"%(expand(dC2N6dxi1(xi1,xi2))))
print("dC2N7dxi1 = %s\n"%(expand(dC2N7dxi1(xi1,xi2))))
print("dC2N8dxi1 = %s\n"%(expand(dC2N8dxi1(xi1,xi2))))
print("dC2N9dxi1 = %s\n"%(expand(dC2N9dxi1(xi1,xi2))))
print("dC2N10dxi1 = %s\n"%(expand(dC2N10dxi1(xi1,xi2))))

def dC2N1dxi2(xi1,xi2):
    return diff(C2N1(xi1,xi2),xi2)
def dC2N2dxi2(xi1,xi2):
    return diff(C2N2(xi1,xi2),xi2)
def dC2N3dxi2(xi1,xi2):
    return diff(C2N3(xi1,xi2),xi2)
def dC2N4dxi2(xi1,xi2):
    return diff(C2N4(xi1,xi2),xi2)
def dC2N5dxi2(xi1,xi2):
    return diff(C2N5(xi1,xi2),xi2)
def dC2N6dxi2(xi1,xi2):
    return diff(C2N6(xi1,xi2),xi2)
def dC2N7dxi2(xi1,xi2):
    return diff(C2N7(xi1,xi2),xi2)
def dC2N8dxi2(xi1,xi2):
    return diff(C2N8(xi1,xi2),xi2)
def dC2N9dxi2(xi1,xi2):
    return diff(C2N9(xi1,xi2),xi2)
def dC2N10dxi2(xi1,xi2):
    return diff(C2N10(xi1,xi2),xi2)

print("dC2N1dxi2 = %s\n"%(expand(dC2N1dxi2(xi1,xi2))))
print("dC2N2dxi2 = %s\n"%(expand(dC2N2dxi2(xi1,xi2))))
print("dC2N3dxi2 = %s\n"%(expand(dC2N3dxi2(xi1,xi2))))
print("dC2N4dxi2 = %s\n"%(expand(dC2N4dxi2(xi1,xi2))))
print("dC2N5dxi2 = %s\n"%(expand(dC2N5dxi2(xi1,xi2))))
print("dC2N6dxi2 = %s\n"%(expand(dC2N6dxi2(xi1,xi2))))
print("dC2N7dxi2 = %s\n"%(expand(dC2N7dxi2(xi1,xi2))))
print("dC2N8dxi2 = %s\n"%(expand(dC2N8dxi2(xi1,xi2))))
print("dC2N9dxi2 = %s\n"%(expand(dC2N9dxi2(xi1,xi2))))
print("dC2N10dxi2 = %s\n"%(expand(dC2N10dxi2(xi1,xi2))))

def d2C2N1dxi1dxi1(xi1,xi2):
    return diff(dC2N1dxi1(xi1,xi2),xi1)
def d2C2N2dxi1dxi1(xi1,xi2):
    return diff(dC2N2dxi1(xi1,xi2),xi1)
def d2C2N3dxi1dxi1(xi1,xi2):
    return diff(dC2N3dxi1(xi1,xi2),xi1)
def d2C2N4dxi1dxi1(xi1,xi2):
    return diff(dC2N4dxi1(xi1,xi2),xi1)
def d2C2N5dxi1dxi1(xi1,xi2):
    return diff(dC2N5dxi1(xi1,xi2),xi1)
def d2C2N6dxi1dxi1(xi1,xi2):
    return diff(dC2N6dxi1(xi1,xi2),xi1)
def d2C2N7dxi1dxi1(xi1,xi2):
    return diff(dC2N7dxi1(xi1,xi2),xi1)
def d2C2N8dxi1dxi1(xi1,xi2):
    return diff(dC2N8dxi1(xi1,xi2),xi1)
def d2C2N9dxi1dxi1(xi1,xi2):
    return diff(dC2N9dxi1(xi1,xi2),xi1)
def d2C2N10dxi1dxi1(xi1,xi2):
    return diff(dC2N10dxi1(xi1,xi2),xi1)

print("d2C2N1dxi1dxi1 = %s\n"%(expand(d2C2N1dxi1dxi1(xi1,xi2))))
print("d2C2N2dxi1dxi1 = %s\n"%(expand(d2C2N2dxi1dxi1(xi1,xi2))))
print("d2C2N3dxi1dxi1 = %s\n"%(expand(d2C2N3dxi1dxi1(xi1,xi2))))
print("d2C2N4dxi1dxi1 = %s\n"%(expand(d2C2N4dxi1dxi1(xi1,xi2))))
print("d2C2N5dxi1dxi1 = %s\n"%(expand(d2C2N5dxi1dxi1(xi1,xi2))))
print("d2C2N6dxi1dxi1 = %s\n"%(expand(d2C2N6dxi1dxi1(xi1,xi2))))
print("d2C2N7dxi1dxi1 = %s\n"%(expand(d2C2N7dxi1dxi1(xi1,xi2))))
print("d2C2N8dxi1dxi1 = %s\n"%(expand(d2C2N8dxi1dxi1(xi1,xi2))))
print("d2C2N9dxi1dxi1 = %s\n"%(expand(d2C2N9dxi1dxi1(xi1,xi2))))
print("d2C2N10dxi1dxi1 = %s\n"%(expand(d2C2N10dxi1dxi1(xi1,xi2))))

def d2C2N1dxi2dxi2(xi1,xi2):
    return diff(dC2N1dxi2(xi1,xi2),xi2)
def d2C2N2dxi2dxi2(xi1,xi2):
    return diff(dC2N2dxi2(xi1,xi2),xi2)
def d2C2N3dxi2dxi2(xi1,xi2):
    return diff(dC2N3dxi2(xi1,xi2),xi2)
def d2C2N4dxi2dxi2(xi1,xi2):
    return diff(dC2N4dxi2(xi1,xi2),xi2)
def d2C2N5dxi2dxi2(xi1,xi2):
    return diff(dC2N5dxi2(xi1,xi2),xi2)
def d2C2N6dxi2dxi2(xi1,xi2):
    return diff(dC2N6dxi2(xi1,xi2),xi2)
def d2C2N7dxi2dxi2(xi1,xi2):
    return diff(dC2N7dxi2(xi1,xi2),xi2)
def d2C2N8dxi2dxi2(xi1,xi2):
    return diff(dC2N8dxi2(xi1,xi2),xi2)
def d2C2N9dxi2dxi2(xi1,xi2):
    return diff(dC2N9dxi2(xi1,xi2),xi2)
def d2C2N10dxi2dxi2(xi1,xi2):
    return diff(dC2N10dxi2(xi1,xi2),xi2)

print("d2C2N1dxi2dxi2 = %s\n"%(expand(d2C2N1dxi2dxi2(xi1,xi2))))
print("d2C2N2dxi2dxi2 = %s\n"%(expand(d2C2N2dxi2dxi2(xi1,xi2))))
print("d2C2N3dxi2dxi2 = %s\n"%(expand(d2C2N3dxi2dxi2(xi1,xi2))))
print("d2C2N4dxi2dxi2 = %s\n"%(expand(d2C2N4dxi2dxi2(xi1,xi2))))
print("d2C2N5dxi2dxi2 = %s\n"%(expand(d2C2N5dxi2dxi2(xi1,xi2))))
print("d2C2N6dxi2dxi2 = %s\n"%(expand(d2C2N6dxi2dxi2(xi1,xi2))))
print("d2C2N7dxi2dxi2 = %s\n"%(expand(d2C2N7dxi2dxi2(xi1,xi2))))
print("d2C2N8dxi2dxi2 = %s\n"%(expand(d2C2N8dxi2dxi2(xi1,xi2))))
print("d2C2N9dxi2dxi2 = %s\n"%(expand(d2C2N9dxi2dxi2(xi1,xi2))))
print("d2C2N10dxi2dxi2 = %s\n"%(expand(d2C2N10dxi2dxi2(xi1,xi2))))

def d2C2N1dxi1dxi2(xi1,xi2):
    return diff(dC2N1dxi1(xi1,xi2),xi2)
def d2C2N2dxi1dxi2(xi1,xi2):
    return diff(dC2N2dxi1(xi1,xi2),xi2)
def d2C2N3dxi1dxi2(xi1,xi2):
    return diff(dC2N3dxi1(xi1,xi2),xi2)
def d2C2N4dxi1dxi2(xi1,xi2):
    return diff(dC2N4dxi1(xi1,xi2),xi2)
def d2C2N5dxi1dxi2(xi1,xi2):
    return diff(dC2N5dxi1(xi1,xi2),xi2)
def d2C2N6dxi1dxi2(xi1,xi2):
    return diff(dC2N6dxi1(xi1,xi2),xi2)
def d2C2N7dxi1dxi2(xi1,xi2):
    return diff(dC2N7dxi1(xi1,xi2),xi2)
def d2C2N8dxi1dxi2(xi1,xi2):
    return diff(dC2N7dxi1(xi1,xi2),xi2)
def d2C2N9dxi1dxi2(xi1,xi2):
    return diff(dC2N8dxi1(xi1,xi2),xi2)
def d2C2N10dxi1dxi2(xi1,xi2):
    return diff(dC2N10dxi1(xi1,xi2),xi2)

print("d2C2N1dxi1dxi2 = %s\n"%(expand(d2C2N1dxi1dxi2(xi1,xi2))))
print("d2C2N2dxi1dxi2 = %s\n"%(expand(d2C2N2dxi1dxi2(xi1,xi2))))
print("d2C2N3dxi1dxi2 = %s\n"%(expand(d2C2N3dxi1dxi2(xi1,xi2))))
print("d2C2N4dxi1dxi2 = %s\n"%(expand(d2C2N4dxi1dxi2(xi1,xi2))))
print("d2C2N5dxi1dxi2 = %s\n"%(expand(d2C2N5dxi1dxi2(xi1,xi2))))
print("d2C2N6dxi1dxi2 = %s\n"%(expand(d2C2N6dxi1dxi2(xi1,xi2))))
print("d2C2N7dxi1dxi2 = %s\n"%(expand(d2C2N7dxi1dxi2(xi1,xi2))))
print("d2C2N8dxi1dxi2 = %s\n"%(expand(d2C2N8dxi1dxi2(xi1,xi2))))
print("d2C2N9dxi1dxi2 = %s\n"%(expand(d2C2N9dxi1dxi2(xi1,xi2))))
print("d2C2N10dxi1dxi2 = %s\n"%(expand(d2C2N10dxi1dxi2(xi1,xi2))))


print("\n\nCubic Tetrahedral Simplex Basis Functions:\n\n")

def C3N1(xi1,xi2,xi3):
    return l31(xi1,xi2,xi3)*(3*l31(xi1,xi2,xi3)-1)*(3*l31(xi1,xi2,xi3)-2)
def C3N2(xi1,xi2,xi3):
    return l32(xi1,xi2,xi3)*(3*l32(xi1,xi2,xi3)-1)*(3*l32(xi1,xi2,xi3)-1)
def C3N3(xi1,xi2,xi3):
    return l33(xi1,xi2,xi3)*(3*l33(xi1,xi2,xi3)-1)*(3*l33(xi1,xi2,xi3)-1)
def C3N4(xi1,xi2,xi3):
    return l34(xi1,xi2,xi3)*(3*l34(xi1,xi2,xi3)-1)*(3*l34(xi1,xi2,xi3)-1)
def C3N5(xi1,xi2,xi3):
    return 9/2*l31(xi1,xi2,xi3)*(3*l31(xi1,xi2,xi3)-1)*l32(xi1,xi2,xi3)
def C3N6(xi1,xi2,xi3):
    return 9/2*l31(xi1,xi2,xi3)*(3*l32(xi1,xi2,xi3)-1)*l32(xi1,xi2,xi3)
def C3N7(xi1,xi2,xi3):
    return 9/2*l31(xi1,xi2,xi3)*(3*l31(xi1,xi2,xi3)-1)*l33(xi1,xi2,xi3)
def C3N8(xi1,xi2,xi3):
    return 9/2*l31(xi1,xi2,xi3)*(3*l33(xi1,xi2,xi3)-1)*l33(xi1,xi2,xi3)
def C3N9(xi1,xi2,xi3):
    return 9/2*l31(xi1,xi2,xi3)*(3*l31(xi1,xi2,xi3)-1)*l34(xi1,xi2,xi3)
def C3N10(xi1,xi2,xi3):
    return 9/2*l31(xi1,xi2,xi3)*(3*l34(xi1,xi2,xi3)-1)*l34(xi1,xi2,xi3)
def C3N11(xi1,xi2,xi3):
    return 9/2*l32(xi1,xi2,xi3)*(3*l32(xi1,xi2,xi3)-1)*l33(xi1,xi2,xi3)
def C3N12(xi1,xi2,xi3):
    return 9/2*l32(xi1,xi2,xi3)*(3*l33(xi1,xi2,xi3)-1)*l33(xi1,xi2,xi3)
def C3N13(xi1,xi2,xi3):
    return 9/2*l33(xi1,xi2,xi3)*(3*l33(xi1,xi2,xi3)-1)*l34(xi1,xi2,xi3)
def C3N14(xi1,xi2,xi3):
    return 9/2*l33(xi1,xi2,xi3)*(3*l34(xi1,xi2,xi3)-1)*l34(xi1,xi2,xi3)
def C3N15(xi1,xi2,xi3):
    return 9/2*l32(xi1,xi2,xi3)*(3*l32(xi1,xi2,xi3)-1)*l34(xi1,xi2,xi3)
def C3N16(xi1,xi2,xi3):
    return 9/2*l32(xi1,xi2,xi3)*(3*l34(xi1,xi2,xi3)-1)*l34(xi1,xi2,xi3)
def C3N17(xi1,xi2,xi3):
    return 27*l31(xi1,xi2,xi3)*l32(xi1,xi2,xi3)*l33(xi1,xi2,xi3)
def C3N18(xi1,xi2,xi3):
    return 27*l31(xi1,xi2,xi3)*l32(xi1,xi2,xi3)*l34(xi1,xi2,xi3)
def C3N19(xi1,xi2,xi3):
    return 27*l31(xi1,xi2,xi3)*l33(xi1,xi2,xi3)*l34(xi1,xi2,xi3)
def C3N20(xi1,xi2,xi3):
    return 27*l32(xi1,xi2,xi3)*l33(xi1,xi2,xi3)*l34(xi1,xi2,xi3)

print("C3N1 = %s\n"%(expand(C3N1(xi1,xi2,xi3))))
print("C3N2 = %s\n"%(expand(C3N2(xi1,xi2,xi3))))
print("C3N3 = %s\n"%(expand(C3N3(xi1,xi2,xi3))))
print("C3N4 = %s\n"%(expand(C3N4(xi1,xi2,xi3))))
print("C3N5 = %s\n"%(expand(C3N5(xi1,xi2,xi3))))
print("C3N6 = %s\n"%(expand(C3N6(xi1,xi2,xi3))))
print("C3N7 = %s\n"%(expand(C3N7(xi1,xi2,xi3))))
print("C3N8 = %s\n"%(expand(C3N8(xi1,xi2,xi3))))
print("C3N9 = %s\n"%(expand(C3N9(xi1,xi2,xi3))))
print("C3N10 = %s\n"%(expand(C3N10(xi1,xi2,xi3))))
print("C3N11 = %s\n"%(expand(C3N11(xi1,xi2,xi3))))
print("C3N12 = %s\n"%(expand(C3N12(xi1,xi2,xi3))))
print("C3N13 = %s\n"%(expand(C3N13(xi1,xi2,xi3))))
print("C3N14 = %s\n"%(expand(C3N14(xi1,xi2,xi3))))
print("C3N15 = %s\n"%(expand(C3N15(xi1,xi2,xi3))))
print("C3N16 = %s\n"%(expand(C3N16(xi1,xi2,xi3))))
print("C3N17 = %s\n"%(expand(C3N17(xi1,xi2,xi3))))
print("C3N18 = %s\n"%(expand(C3N18(xi1,xi2,xi3))))
print("C3N19 = %s\n"%(expand(C3N19(xi1,xi2,xi3))))
print("C3N20 = %s\n"%(expand(C3N20(xi1,xi2,xi3))))

def dC3N1dxi1(xi1,xi2,xi3):
    return diff(C3N1(xi1,xi2,xi3),xi1)
def dC3N2dxi1(xi1,xi2,xi3):
    return diff(C3N2(xi1,xi2,xi3),xi1)
def dC3N3dxi1(xi1,xi2,xi3):
    return diff(C3N3(xi1,xi2,xi3),xi1)
def dC3N4dxi1(xi1,xi2,xi3):
    return diff(C3N4(xi1,xi2,xi3),xi1)
def dC3N5dxi1(xi1,xi2,xi3):
    return diff(C3N5(xi1,xi2,xi3),xi1)
def dC3N6dxi1(xi1,xi2,xi3):
    return diff(C3N6(xi1,xi2,xi3),xi1)
def dC3N7dxi1(xi1,xi2,xi3):
    return diff(C3N7(xi1,xi2,xi3),xi1)
def dC3N8dxi1(xi1,xi2,xi3):
    return diff(C3N8(xi1,xi2,xi3),xi1)
def dC3N9dxi1(xi1,xi2,xi3):
    return diff(C3N8(xi1,xi2,xi3),xi1)
def dC3N10dxi1(xi1,xi2,xi3):
    return diff(C3N10(xi1,xi2,xi3),xi1)
def dC3N11dxi1(xi1,xi2,xi3):
    return diff(C3N11(xi1,xi2,xi3),xi1)
def dC3N12dxi1(xi1,xi2,xi3):
    return diff(C3N12(xi1,xi2,xi3),xi1)
def dC3N13dxi1(xi1,xi2,xi3):
    return diff(C3N13(xi1,xi2,xi3),xi1)
def dC3N14dxi1(xi1,xi2,xi3):
    return diff(C3N14(xi1,xi2,xi3),xi1)
def dC3N15dxi1(xi1,xi2,xi3):
    return diff(C3N15(xi1,xi2,xi3),xi1)
def dC3N16dxi1(xi1,xi2,xi3):
    return diff(C3N16(xi1,xi2,xi3),xi1)
def dC3N17dxi1(xi1,xi2,xi3):
    return diff(C3N17(xi1,xi2,xi3),xi1)
def dC3N18dxi1(xi1,xi2,xi3):
    return diff(C3N18(xi1,xi2,xi3),xi1)
def dC3N19dxi1(xi1,xi2,xi3):
    return diff(C3N19(xi1,xi2,xi3),xi1)
def dC3N20dxi1(xi1,xi2,xi3):
    return diff(C3N20(xi1,xi2,xi3),xi1)

print("dC3N1dxi1 = %s\n"%(expand(dC3N1dxi1(xi1,xi2,xi3))))
print("dC3N2dxi1 = %s\n"%(expand(dC3N2dxi1(xi1,xi2,xi3))))
print("dC3N3dxi1 = %s\n"%(expand(dC3N3dxi1(xi1,xi2,xi3))))
print("dC3N4dxi1 = %s\n"%(expand(dC3N4dxi1(xi1,xi2,xi3))))
print("dC3N5dxi1 = %s\n"%(expand(dC3N5dxi1(xi1,xi2,xi3))))
print("dC3N6dxi1 = %s\n"%(expand(dC3N6dxi1(xi1,xi2,xi3))))
print("dC3N7dxi1 = %s\n"%(expand(dC3N7dxi1(xi1,xi2,xi3))))
print("dC3N8dxi1 = %s\n"%(expand(dC3N8dxi1(xi1,xi2,xi3))))
print("dC3N9dxi1 = %s\n"%(expand(dC3N9dxi1(xi1,xi2,xi3))))
print("dC3N10dxi1 = %s\n"%(expand(dC3N10dxi1(xi1,xi2,xi3))))
print("dC3N11dxi1 = %s\n"%(expand(dC3N11dxi1(xi1,xi2,xi3))))
print("dC3N12dxi1 = %s\n"%(expand(dC3N12dxi1(xi1,xi2,xi3))))
print("dC3N13dxi1 = %s\n"%(expand(dC3N13dxi1(xi1,xi2,xi3))))
print("dC3N14dxi1 = %s\n"%(expand(dC3N14dxi1(xi1,xi2,xi3))))
print("dC3N15dxi1 = %s\n"%(expand(dC3N15dxi1(xi1,xi2,xi3))))
print("dC3N16dxi1 = %s\n"%(expand(dC3N16dxi1(xi1,xi2,xi3))))
print("dC3N17dxi1 = %s\n"%(expand(dC3N17dxi1(xi1,xi2,xi3))))
print("dC3N18dxi1 = %s\n"%(expand(dC3N18dxi1(xi1,xi2,xi3))))
print("dC3N19dxi1 = %s\n"%(expand(dC3N19dxi1(xi1,xi2,xi3))))
print("dC3N20dxi1 = %s\n"%(expand(dC3N20dxi1(xi1,xi2,xi3))))

def dC3N1dxi2(xi1,xi2,xi3):
    return diff(C3N1(xi1,xi2,xi3),xi2)
def dC3N2dxi2(xi1,xi2,xi3):
    return diff(C3N2(xi1,xi2,xi3),xi2)
def dC3N3dxi2(xi1,xi2,xi3):
    return diff(C3N3(xi1,xi2,xi3),xi2)
def dC3N4dxi2(xi1,xi2,xi3):
    return diff(C3N4(xi1,xi2,xi3),xi2)
def dC3N5dxi2(xi1,xi2,xi3):
    return diff(C3N5(xi1,xi2,xi3),xi2)
def dC3N6dxi2(xi1,xi2,xi3):
    return diff(C3N6(xi1,xi2,xi3),xi2)
def dC3N7dxi2(xi1,xi2,xi3):
    return diff(C3N7(xi1,xi2,xi3),xi2)
def dC3N8dxi2(xi1,xi2,xi3):
    return diff(C3N8(xi1,xi2,xi3),xi2)
def dC3N9dxi2(xi1,xi2,xi3):
    return diff(C3N9(xi1,xi2,xi3),xi2)
def dC3N10dxi2(xi1,xi2,xi3):
    return diff(C3N10(xi1,xi2,xi3),xi2)
def dC3N11dxi2(xi1,xi2,xi3):
    return diff(C3N11(xi1,xi2,xi3),xi2)
def dC3N12dxi2(xi1,xi2,xi3):
    return diff(C3N12(xi1,xi2,xi3),xi2)
def dC3N13dxi2(xi1,xi2,xi3):
    return diff(C3N13(xi1,xi2,xi3),xi2)
def dC3N14dxi2(xi1,xi2,xi3):
    return diff(C3N14(xi1,xi2,xi3),xi2)
def dC3N15dxi2(xi1,xi2,xi3):
    return diff(C3N15(xi1,xi2,xi3),xi2)
def dC3N16dxi2(xi1,xi2,xi3):
    return diff(C3N16(xi1,xi2,xi3),xi2)
def dC3N17dxi2(xi1,xi2,xi3):
    return diff(C3N17(xi1,xi2,xi3),xi2)
def dC3N18dxi2(xi1,xi2,xi3):
    return diff(C3N18(xi1,xi2,xi3),xi2)
def dC3N19dxi2(xi1,xi2,xi3):
    return diff(C3N19(xi1,xi2,xi3),xi2)
def dC3N20dxi2(xi1,xi2,xi3):
    return diff(C3N20(xi1,xi2,xi3),xi2)

print("dC3N1dxi2 = %s\n"%(expand(dC3N1dxi2(xi1,xi2,xi3))))
print("dC3N2dxi2 = %s\n"%(expand(dC3N2dxi2(xi1,xi2,xi3))))
print("dC3N3dxi2 = %s\n"%(expand(dC3N3dxi2(xi1,xi2,xi3))))
print("dC3N4dxi2 = %s\n"%(expand(dC3N4dxi2(xi1,xi2,xi3))))
print("dC3N5dxi2 = %s\n"%(expand(dC3N5dxi2(xi1,xi2,xi3))))
print("dC3N6dxi2 = %s\n"%(expand(dC3N6dxi2(xi1,xi2,xi3))))
print("dC3N7dxi2 = %s\n"%(expand(dC3N7dxi2(xi1,xi2,xi3))))
print("dC3N8dxi2 = %s\n"%(expand(dC3N8dxi2(xi1,xi2,xi3))))
print("dC3N9dxi2 = %s\n"%(expand(dC3N9dxi2(xi1,xi2,xi3))))
print("dC3N10dxi2 = %s\n"%(expand(dC3N10dxi2(xi1,xi2,xi3))))
print("dC3N11dxi2 = %s\n"%(expand(dC3N11dxi2(xi1,xi2,xi3))))
print("dC3N12dxi2 = %s\n"%(expand(dC3N12dxi2(xi1,xi2,xi3))))
print("dC3N13dxi2 = %s\n"%(expand(dC3N13dxi2(xi1,xi2,xi3))))
print("dC3N14dxi2 = %s\n"%(expand(dC3N14dxi2(xi1,xi2,xi3))))
print("dC3N15dxi2 = %s\n"%(expand(dC3N15dxi2(xi1,xi2,xi3))))
print("dC3N16dxi2 = %s\n"%(expand(dC3N16dxi2(xi1,xi2,xi3))))
print("dC3N17dxi2 = %s\n"%(expand(dC3N17dxi2(xi1,xi2,xi3))))
print("dC3N18dxi2 = %s\n"%(expand(dC3N18dxi2(xi1,xi2,xi3))))
print("dC3N19dxi2 = %s\n"%(expand(dC3N19dxi2(xi1,xi2,xi3))))
print("dC3N20dxi2 = %s\n"%(expand(dC3N20dxi2(xi1,xi2,xi3))))

def dC3N1dxi3(xi1,xi2,xi3):
    return diff(C3N1(xi1,xi2,xi3),xi3)
def dC3N2dxi3(xi1,xi2,xi3):
    return diff(C3N2(xi1,xi2,xi3),xi3)
def dC3N3dxi3(xi1,xi2,xi3):
    return diff(C3N3(xi1,xi2,xi3),xi3)
def dC3N4dxi3(xi1,xi2,xi3):
    return diff(C3N4(xi1,xi2,xi3),xi3)
def dC3N5dxi3(xi1,xi2,xi3):
    return diff(C3N5(xi1,xi2,xi3),xi3)
def dC3N6dxi3(xi1,xi2,xi3):
    return diff(C3N6(xi1,xi2,xi3),xi3)
def dC3N7dxi3(xi1,xi2,xi3):
    return diff(C3N7(xi1,xi2,xi3),xi3)
def dC3N8dxi3(xi1,xi2,xi3):
    return diff(C3N8(xi1,xi2,xi3),xi3)
def dC3N9dxi3(xi1,xi2,xi3):
    return diff(C3N9(xi1,xi2,xi3),xi3)
def dC3N10dxi3(xi1,xi2,xi3):
    return diff(C3N10(xi1,xi2,xi3),xi3)
def dC3N11dxi3(xi1,xi2,xi3):
    return diff(C3N11(xi1,xi2,xi3),xi3)
def dC3N12dxi3(xi1,xi2,xi3):
    return diff(C3N12(xi1,xi2,xi3),xi3)
def dC3N13dxi3(xi1,xi2,xi3):
    return diff(C3N13(xi1,xi2,xi3),xi3)
def dC3N14dxi3(xi1,xi2,xi3):
    return diff(C3N14(xi1,xi2,xi3),xi3)
def dC3N15dxi3(xi1,xi2,xi3):
    return diff(C3N15(xi1,xi2,xi3),xi3)
def dC3N16dxi3(xi1,xi2,xi3):
    return diff(C3N16(xi1,xi2,xi3),xi3)
def dC3N17dxi3(xi1,xi2,xi3):
    return diff(C3N17(xi1,xi2,xi3),xi3)
def dC3N18dxi3(xi1,xi2,xi3):
    return diff(C3N18(xi1,xi2,xi3),xi3)
def dC3N19dxi3(xi1,xi2,xi3):
    return diff(C3N19(xi1,xi2,xi3),xi3)
def dC3N20dxi3(xi1,xi2,xi3):
    return diff(C3N20(xi1,xi2,xi3),xi3)

print("dC3N1dxi3 = %s\n"%(expand(dC3N1dxi3(xi1,xi2,xi3))))
print("dC3N2dxi3 = %s\n"%(expand(dC3N2dxi3(xi1,xi2,xi3))))
print("dC3N3dxi3 = %s\n"%(expand(dC3N3dxi3(xi1,xi2,xi3))))
print("dC3N4dxi3 = %s\n"%(expand(dC3N4dxi3(xi1,xi2,xi3))))
print("dC3N5dxi3 = %s\n"%(expand(dC3N5dxi3(xi1,xi2,xi3))))
print("dC3N6dxi3 = %s\n"%(expand(dC3N6dxi3(xi1,xi2,xi3))))
print("dC3N7dxi3 = %s\n"%(expand(dC3N7dxi3(xi1,xi2,xi3))))
print("dC3N8dxi3 = %s\n"%(expand(dC3N8dxi3(xi1,xi2,xi3))))
print("dC3N9dxi3 = %s\n"%(expand(dC3N9dxi3(xi1,xi2,xi3))))
print("dC3N10dxi3 = %s\n"%(expand(dC3N10dxi3(xi1,xi2,xi3))))
print("dC3N11dxi3 = %s\n"%(expand(dC3N11dxi3(xi1,xi2,xi3))))
print("dC3N12dxi3 = %s\n"%(expand(dC3N12dxi3(xi1,xi2,xi3))))
print("dC3N13dxi3 = %s\n"%(expand(dC3N13dxi3(xi1,xi2,xi3))))
print("dC3N14dxi3 = %s\n"%(expand(dC3N14dxi3(xi1,xi2,xi3))))
print("dC3N15dxi3 = %s\n"%(expand(dC3N15dxi3(xi1,xi2,xi3))))
print("dC3N16dxi3 = %s\n"%(expand(dC3N16dxi3(xi1,xi2,xi3))))
print("dC3N17dxi3 = %s\n"%(expand(dC3N17dxi3(xi1,xi2,xi3))))
print("dC3N18dxi3 = %s\n"%(expand(dC3N18dxi3(xi1,xi2,xi3))))
print("dC3N19dxi3 = %s\n"%(expand(dC3N19dxi3(xi1,xi2,xi3))))
print("dC3N20dxi3 = %s\n"%(expand(dC3N20dxi3(xi1,xi2,xi3))))

def d2C3N1dxi1dxi1(xi1,xi2,xi3):
    return diff(dC3N1dxi1(xi1,xi2,xi3),xi1)
def d2C3N2dxi1dxi1(xi1,xi2,xi3):
    return diff(dC3N2dxi1(xi1,xi2,xi3),xi1)
def d2C3N3dxi1dxi1(xi1,xi2,xi3):
    return diff(dC3N3dxi1(xi1,xi2,xi3),xi1)
def d2C3N4dxi1dxi1(xi1,xi2,xi3):
    return diff(dC3N4dxi1(xi1,xi2,xi3),xi1)
def d2C3N5dxi1dxi1(xi1,xi2,xi3):
    return diff(dC3N5dxi1(xi1,xi2,xi3),xi1)
def d2C3N6dxi1dxi1(xi1,xi2,xi3):
    return diff(dC3N6dxi1(xi1,xi2,xi3),xi1)
def d2C3N7dxi1dxi1(xi1,xi2,xi3):
    return diff(dC3N7dxi1(xi1,xi2,xi3),xi1)
def d2C3N8dxi1dxi1(xi1,xi2,xi3):
    return diff(dC3N8dxi1(xi1,xi2,xi3),xi1)
def d2C3N9dxi1dxi1(xi1,xi2,xi3):
    return diff(dC3N9dxi1(xi1,xi2,xi3),xi1)
def d2C3N10dxi1dxi1(xi1,xi2,xi3):
    return diff(dC3N10dxi1(xi1,xi2,xi3),xi1)
def d2C3N11dxi1dxi1(xi1,xi2,xi3):
    return diff(dC3N11dxi1(xi1,xi2,xi3),xi1)
def d2C3N12dxi1dxi1(xi1,xi2,xi3):
    return diff(dC3N12dxi1(xi1,xi2,xi3),xi1)
def d2C3N13dxi1dxi1(xi1,xi2,xi3):
    return diff(dC3N13dxi1(xi1,xi2,xi3),xi1)
def d2C3N14dxi1dxi1(xi1,xi2,xi3):
    return diff(dC3N14dxi1(xi1,xi2,xi3),xi1)
def d2C3N15dxi1dxi1(xi1,xi2,xi3):
    return diff(dC3N15dxi1(xi1,xi2,xi3),xi1)
def d2C3N16dxi1dxi1(xi1,xi2,xi3):
    return diff(dC3N16dxi1(xi1,xi2,xi3),xi1)
def d2C3N17dxi1dxi1(xi1,xi2,xi3):
    return diff(dC3N17dxi1(xi1,xi2,xi3),xi1)
def d2C3N18dxi1dxi1(xi1,xi2,xi3):
    return diff(dC3N18dxi1(xi1,xi2,xi3),xi1)
def d2C3N19dxi1dxi1(xi1,xi2,xi3):
    return diff(dC3N19dxi1(xi1,xi2,xi3),xi1)
def d2C3N20dxi1dxi1(xi1,xi2,xi3):
    return diff(dC3N20dxi1(xi1,xi2,xi3),xi1)

print("d2C3N1dxi1dxi1 = %s\n"%(expand(d2C3N1dxi1dxi1(xi1,xi2,xi3))))
print("d2C3N2dxi1dxi1 = %s\n"%(expand(d2C3N2dxi1dxi1(xi1,xi2,xi3))))
print("d2C3N3dxi1dxi1 = %s\n"%(expand(d2C3N3dxi1dxi1(xi1,xi2,xi3))))
print("d2C3N4dxi1dxi1 = %s\n"%(expand(d2C3N4dxi1dxi1(xi1,xi2,xi3))))
print("d2C3N5dxi1dxi1 = %s\n"%(expand(d2C3N5dxi1dxi1(xi1,xi2,xi3))))
print("d2C3N6dxi1dxi1 = %s\n"%(expand(d2C3N6dxi1dxi1(xi1,xi2,xi3))))
print("d2C3N7dxi1dxi1 = %s\n"%(expand(d2C3N7dxi1dxi1(xi1,xi2,xi3))))
print("d2C3N8dxi1dxi1 = %s\n"%(expand(d2C3N8dxi1dxi1(xi1,xi2,xi3))))
print("d2C3N9dxi1dxi1 = %s\n"%(expand(d2C3N9dxi1dxi1(xi1,xi2,xi3))))
print("d2C3N10dxi1dxi1 = %s\n"%(expand(d2C3N10dxi1dxi1(xi1,xi2,xi3))))
print("d2C3N11dxi1dxi1 = %s\n"%(expand(d2C3N11dxi1dxi1(xi1,xi2,xi3))))
print("d2C3N12dxi1dxi1 = %s\n"%(expand(d2C3N12dxi1dxi1(xi1,xi2,xi3))))
print("d2C3N13dxi1dxi1 = %s\n"%(expand(d2C3N13dxi1dxi1(xi1,xi2,xi3))))
print("d2C3N14dxi1dxi1 = %s\n"%(expand(d2C3N14dxi1dxi1(xi1,xi2,xi3))))
print("d2C3N15dxi1dxi1 = %s\n"%(expand(d2C3N15dxi1dxi1(xi1,xi2,xi3))))
print("d2C3N16dxi1dxi1 = %s\n"%(expand(d2C3N16dxi1dxi1(xi1,xi2,xi3))))
print("d2C3N17dxi1dxi1 = %s\n"%(expand(d2C3N17dxi1dxi1(xi1,xi2,xi3))))
print("d2C3N18dxi1dxi1 = %s\n"%(expand(d2C3N18dxi1dxi1(xi1,xi2,xi3))))
print("d2C3N19dxi1dxi1 = %s\n"%(expand(d2C3N19dxi1dxi1(xi1,xi2,xi3))))
print("d2C3N20dxi1dxi1 = %s\n"%(expand(d2C3N20dxi1dxi1(xi1,xi2,xi3))))

def d2C3N1dxi2dxi2(xi1,xi2,xi3):
    return diff(dC3N1dxi2(xi1,xi2,xi3),xi2)
def d2C3N2dxi2dxi2(xi1,xi2,xi3):
    return diff(dC3N2dxi2(xi1,xi2,xi3),xi2)
def d2C3N3dxi2dxi2(xi1,xi2,xi3):
    return diff(dC3N3dxi2(xi1,xi2,xi3),xi2)
def d2C3N4dxi2dxi2(xi1,xi2,xi3):
    return diff(dC3N4dxi2(xi1,xi2,xi3),xi2)
def d2C3N5dxi2dxi2(xi1,xi2,xi3):
    return diff(dC3N5dxi2(xi1,xi2,xi3),xi2)
def d2C3N6dxi2dxi2(xi1,xi2,xi3):
    return diff(dC3N6dxi2(xi1,xi2,xi3),xi2)
def d2C3N7dxi2dxi2(xi1,xi2,xi3):
    return diff(dC3N7dxi2(xi1,xi2,xi3),xi2)
def d2C3N8dxi2dxi2(xi1,xi2,xi3):
    return diff(dC3N8dxi2(xi1,xi2,xi3),xi2)
def d2C3N9dxi2dxi2(xi1,xi2,xi3):
    return diff(dC3N9dxi2(xi1,xi2,xi3),xi2)
def d2C3N10dxi2dxi2(xi1,xi2,xi3):
    return diff(dC3N10dxi2(xi1,xi2,xi3),xi2)
def d2C3N11dxi2dxi2(xi1,xi2,xi3):
    return diff(dC3N11dxi2(xi1,xi2,xi3),xi2)
def d2C3N12dxi2dxi2(xi1,xi2,xi3):
    return diff(dC3N12dxi2(xi1,xi2,xi3),xi2)
def d2C3N13dxi2dxi2(xi1,xi2,xi3):
    return diff(dC3N13dxi2(xi1,xi2,xi3),xi2)
def d2C3N14dxi2dxi2(xi1,xi2,xi3):
    return diff(dC3N14dxi2(xi1,xi2,xi3),xi2)
def d2C3N15dxi2dxi2(xi1,xi2,xi3):
    return diff(dC3N15dxi2(xi1,xi2,xi3),xi2)
def d2C3N16dxi2dxi2(xi1,xi2,xi3):
    return diff(dC3N16dxi2(xi1,xi2,xi3),xi2)
def d2C3N17dxi2dxi2(xi1,xi2,xi3):
    return diff(dC3N17dxi2(xi1,xi2,xi3),xi2)
def d2C3N18dxi2dxi2(xi1,xi2,xi3):
    return diff(dC3N18dxi2(xi1,xi2,xi3),xi2)
def d2C3N19dxi2dxi2(xi1,xi2,xi3):
    return diff(dC3N19dxi2(xi1,xi2,xi3),xi2)
def d2C3N20dxi2dxi2(xi1,xi2,xi3):
    return diff(dC3N20dxi2(xi1,xi2,xi3),xi2)

print("d2C3N1dxi2dxi2 = %s\n"%(expand(d2C3N1dxi2dxi2(xi1,xi2,xi3))))
print("d2C3N2dxi2dxi2 = %s\n"%(expand(d2C3N2dxi2dxi2(xi1,xi2,xi3))))
print("d2C3N3dxi2dxi2 = %s\n"%(expand(d2C3N3dxi2dxi2(xi1,xi2,xi3))))
print("d2C3N4dxi2dxi2 = %s\n"%(expand(d2C3N4dxi2dxi2(xi1,xi2,xi3))))
print("d2C3N5dxi2dxi2 = %s\n"%(expand(d2C3N5dxi2dxi2(xi1,xi2,xi3))))
print("d2C3N6dxi2dxi2 = %s\n"%(expand(d2C3N6dxi2dxi2(xi1,xi2,xi3))))
print("d2C3N7dxi2dxi2 = %s\n"%(expand(d2C3N7dxi2dxi2(xi1,xi2,xi3))))
print("d2C3N8dxi2dxi2 = %s\n"%(expand(d2C3N8dxi2dxi2(xi1,xi2,xi3))))
print("d2C3N9dxi2dxi2 = %s\n"%(expand(d2C3N9dxi2dxi2(xi1,xi2,xi3))))
print("d2C3N10dxi2dxi2 = %s\n"%(expand(d2C3N10dxi2dxi2(xi1,xi2,xi3))))
print("d2C3N11dxi2dxi2 = %s\n"%(expand(d2C3N11dxi2dxi2(xi1,xi2,xi3))))
print("d2C3N12dxi2dxi2 = %s\n"%(expand(d2C3N12dxi2dxi2(xi1,xi2,xi3))))
print("d2C3N13dxi2dxi2 = %s\n"%(expand(d2C3N13dxi2dxi2(xi1,xi2,xi3))))
print("d2C3N14dxi2dxi2 = %s\n"%(expand(d2C3N14dxi2dxi2(xi1,xi2,xi3))))
print("d2C3N15dxi2dxi2 = %s\n"%(expand(d2C3N15dxi2dxi2(xi1,xi2,xi3))))
print("d2C3N16dxi2dxi2 = %s\n"%(expand(d2C3N16dxi2dxi2(xi1,xi2,xi3))))
print("d2C3N17dxi2dxi2 = %s\n"%(expand(d2C3N17dxi2dxi2(xi1,xi2,xi3))))
print("d2C3N18dxi2dxi2 = %s\n"%(expand(d2C3N18dxi2dxi2(xi1,xi2,xi3))))
print("d2C3N19dxi2dxi2 = %s\n"%(expand(d2C3N19dxi2dxi2(xi1,xi2,xi3))))
print("d2C3N20dxi2dxi2 = %s\n"%(expand(d2C3N20dxi2dxi2(xi1,xi2,xi3))))

def d2C3N1dxi3dxi3(xi1,xi2,xi3):
    return diff(dC3N1dxi3(xi1,xi2,xi3),xi3)
def d2C3N2dxi3dxi3(xi1,xi2,xi3):
    return diff(dC3N2dxi3(xi1,xi2,xi3),xi3)
def d2C3N3dxi3dxi3(xi1,xi2,xi3):
    return diff(dC3N3dxi3(xi1,xi2,xi3),xi3)
def d2C3N4dxi3dxi3(xi1,xi2,xi3):
    return diff(dC3N4dxi3(xi1,xi2,xi3),xi3)
def d2C3N5dxi3dxi3(xi1,xi2,xi3):
    return diff(dC3N5dxi3(xi1,xi2,xi3),xi3)
def d2C3N6dxi3dxi3(xi1,xi2,xi3):
    return diff(dC3N6dxi3(xi1,xi2,xi3),xi3)
def d2C3N7dxi3dxi3(xi1,xi2,xi3):
    return diff(dC3N7dxi3(xi1,xi2,xi3),xi3)
def d2C3N8dxi3dxi3(xi1,xi2,xi3):
    return diff(dC3N8dxi3(xi1,xi2,xi3),xi3)
def d2C3N9dxi3dxi3(xi1,xi2,xi3):
    return diff(dC3N9dxi3(xi1,xi2,xi3),xi3)
def d2C3N10dxi3dxi3(xi1,xi2,xi3):
    return diff(dC3N10dxi3(xi1,xi2,xi3),xi3)
def d2C3N11dxi3dxi3(xi1,xi2,xi3):
    return diff(dC3N11dxi3(xi1,xi2,xi3),xi3)
def d2C3N12dxi3dxi3(xi1,xi2,xi3):
    return diff(dC3N12dxi3(xi1,xi2,xi3),xi3)
def d2C3N13dxi3dxi3(xi1,xi2,xi3):
    return diff(dC3N13dxi3(xi1,xi2,xi3),xi3)
def d2C3N14dxi3dxi3(xi1,xi2,xi3):
    return diff(dC3N14dxi3(xi1,xi2,xi3),xi3)
def d2C3N15dxi3dxi3(xi1,xi2,xi3):
    return diff(dC3N15dxi3(xi1,xi2,xi3),xi3)
def d2C3N16dxi3dxi3(xi1,xi2,xi3):
    return diff(dC3N16dxi3(xi1,xi2,xi3),xi3)
def d2C3N17dxi3dxi3(xi1,xi2,xi3):
    return diff(dC3N17dxi3(xi1,xi2,xi3),xi3)
def d2C3N18dxi3dxi3(xi1,xi2,xi3):
    return diff(dC3N18dxi3(xi1,xi2,xi3),xi3)
def d2C3N19dxi3dxi3(xi1,xi2,xi3):
    return diff(dC3N19dxi3(xi1,xi2,xi3),xi3)
def d2C3N20dxi3dxi3(xi1,xi2,xi3):
    return diff(dC3N20dxi3(xi1,xi2,xi3),xi3)

print("d2C3N1dxi3dxi3 = %s\n"%(expand(d2C3N1dxi3dxi3(xi1,xi2,xi3))))
print("d2C3N2dxi3dxi3 = %s\n"%(expand(d2C3N2dxi3dxi3(xi1,xi2,xi3))))
print("d2C3N3dxi3dxi3 = %s\n"%(expand(d2C3N3dxi3dxi3(xi1,xi2,xi3))))
print("d2C3N4dxi3dxi3 = %s\n"%(expand(d2C3N4dxi3dxi3(xi1,xi2,xi3))))
print("d2C3N5dxi3dxi3 = %s\n"%(expand(d2C3N5dxi3dxi3(xi1,xi2,xi3))))
print("d2C3N6dxi3dxi3 = %s\n"%(expand(d2C3N6dxi3dxi3(xi1,xi2,xi3))))
print("d2C3N7dxi3dxi3 = %s\n"%(expand(d2C3N7dxi3dxi3(xi1,xi2,xi3))))
print("d2C3N8dxi3dxi3 = %s\n"%(expand(d2C3N8dxi3dxi3(xi1,xi2,xi3))))
print("d2C3N9dxi3dxi3 = %s\n"%(expand(d2C3N9dxi3dxi3(xi1,xi2,xi3))))
print("d2C3N10dxi3dxi3 = %s\n"%(expand(d2C3N10dxi3dxi3(xi1,xi2,xi3))))
print("d2C3N11dxi3dxi3 = %s\n"%(expand(d2C3N11dxi3dxi3(xi1,xi2,xi3))))
print("d2C3N12dxi3dxi3 = %s\n"%(expand(d2C3N12dxi3dxi3(xi1,xi2,xi3))))
print("d2C3N13dxi3dxi3 = %s\n"%(expand(d2C3N13dxi3dxi3(xi1,xi2,xi3))))
print("d2C3N14dxi3dxi3 = %s\n"%(expand(d2C3N14dxi3dxi3(xi1,xi2,xi3))))
print("d2C3N15dxi3dxi3 = %s\n"%(expand(d2C3N15dxi3dxi3(xi1,xi2,xi3))))
print("d2C3N16dxi3dxi3 = %s\n"%(expand(d2C3N16dxi3dxi3(xi1,xi2,xi3))))
print("d2C3N17dxi3dxi3 = %s\n"%(expand(d2C3N17dxi3dxi3(xi1,xi2,xi3))))
print("d2C3N18dxi3dxi3 = %s\n"%(expand(d2C3N18dxi3dxi3(xi1,xi2,xi3))))
print("d2C3N19dxi3dxi3 = %s\n"%(expand(d2C3N9dxi3dxi3(xi1,xi2,xi3))))
print("d2C3N20dxi3dxi3 = %s\n"%(expand(d2C3N10dxi3dxi3(xi1,xi2,xi3))))

def d2C3N1dxi1dxi2(xi1,xi2,xi3):
    return diff(dC3N1dxi1(xi1,xi2,xi3),xi2)
def d2C3N2dxi1dxi2(xi1,xi2,xi3):
    return diff(dC3N2dxi1(xi1,xi2,xi3),xi2)
def d2C3N3dxi1dxi2(xi1,xi2,xi3):
    return diff(dC3N3dxi1(xi1,xi2,xi3),xi2)
def d2C3N4dxi1dxi2(xi1,xi2,xi3):
    return diff(dC3N4dxi1(xi1,xi2,xi3),xi2)
def d2C3N5dxi1dxi2(xi1,xi2,xi3):
    return diff(dC3N5dxi1(xi1,xi2,xi3),xi2)
def d2C3N6dxi1dxi2(xi1,xi2,xi3):
    return diff(dC3N6dxi1(xi1,xi2,xi3),xi2)
def d2C3N7dxi1dxi2(xi1,xi2,xi3):
    return diff(dC3N7dxi1(xi1,xi2,xi3),xi2)
def d2C3N8dxi1dxi2(xi1,xi2,xi3):
    return diff(dC3N8dxi1(xi1,xi2,xi3),xi2)
def d2C3N9dxi1dxi2(xi1,xi2,xi3):
    return diff(dC3N9dxi1(xi1,xi2,xi3),xi2)
def d2C3N10dxi1dxi2(xi1,xi2,xi3):
    return diff(dC3N10dxi1(xi1,xi2,xi3),xi2)
def d2C3N11dxi1dxi2(xi1,xi2,xi3):
    return diff(dC3N11dxi1(xi1,xi2,xi3),xi2)
def d2C3N12dxi1dxi2(xi1,xi2,xi3):
    return diff(dC3N12dxi1(xi1,xi2,xi3),xi2)
def d2C3N13dxi1dxi2(xi1,xi2,xi3):
    return diff(dC3N13dxi1(xi1,xi2,xi3),xi2)
def d2C3N14dxi1dxi2(xi1,xi2,xi3):
    return diff(dC3N14dxi1(xi1,xi2,xi3),xi2)
def d2C3N15dxi1dxi2(xi1,xi2,xi3):
    return diff(dC3N15dxi1(xi1,xi2,xi3),xi2)
def d2C3N16dxi1dxi2(xi1,xi2,xi3):
    return diff(dC3N16dxi1(xi1,xi2,xi3),xi2)
def d2C3N17dxi1dxi2(xi1,xi2,xi3):
    return diff(dC3N17dxi1(xi1,xi2,xi3),xi2)
def d2C3N18dxi1dxi2(xi1,xi2,xi3):
    return diff(dC3N18dxi1(xi1,xi2,xi3),xi2)
def d2C3N19dxi1dxi2(xi1,xi2,xi3):
    return diff(dC3N19dxi1(xi1,xi2,xi3),xi2)
def d2C3N20dxi1dxi2(xi1,xi2,xi3):
    return diff(dC3N20dxi1(xi1,xi2,xi3),xi2)

print("d2C3N1dxi1dxi2 = %s\n"%(expand(d2C3N1dxi1dxi2(xi1,xi2,xi3))))
print("d2C3N2dxi1dxi2 = %s\n"%(expand(d2C3N2dxi1dxi2(xi1,xi2,xi3))))
print("d2C3N3dxi1dxi2 = %s\n"%(expand(d2C3N3dxi1dxi2(xi1,xi2,xi3))))
print("d2C3N4dxi1dxi2 = %s\n"%(expand(d2C3N4dxi1dxi2(xi1,xi2,xi3))))
print("d2C3N5dxi1dxi2 = %s\n"%(expand(d2C3N5dxi1dxi2(xi1,xi2,xi3))))
print("d2C3N6dxi1dxi2 = %s\n"%(expand(d2C3N6dxi1dxi2(xi1,xi2,xi3))))
print("d2C3N7dxi1dxi2 = %s\n"%(expand(d2C3N7dxi1dxi2(xi1,xi2,xi3))))
print("d2C3N8dxi1dxi2 = %s\n"%(expand(d2C3N8dxi1dxi2(xi1,xi2,xi3))))
print("d2C3N9dxi1dxi2 = %s\n"%(expand(d2C3N9dxi1dxi2(xi1,xi2,xi3))))
print("d2C3N10dxi1dxi2 = %s\n"%(expand(d2C3N10dxi1dxi2(xi1,xi2,xi3))))
print("d2C3N11dxi1dxi2 = %s\n"%(expand(d2C3N11dxi1dxi2(xi1,xi2,xi3))))
print("d2C3N12dxi1dxi2 = %s\n"%(expand(d2C3N12dxi1dxi2(xi1,xi2,xi3))))
print("d2C3N13dxi1dxi2 = %s\n"%(expand(d2C3N13dxi1dxi2(xi1,xi2,xi3))))
print("d2C3N14dxi1dxi2 = %s\n"%(expand(d2C3N14dxi1dxi2(xi1,xi2,xi3))))
print("d2C3N15dxi1dxi2 = %s\n"%(expand(d2C3N15dxi1dxi2(xi1,xi2,xi3))))
print("d2C3N16dxi1dxi2 = %s\n"%(expand(d2C3N16dxi1dxi2(xi1,xi2,xi3))))
print("d2C3N17dxi1dxi2 = %s\n"%(expand(d2C3N17dxi1dxi2(xi1,xi2,xi3))))
print("d2C3N18dxi1dxi2 = %s\n"%(expand(d2C3N18dxi1dxi2(xi1,xi2,xi3))))
print("d2C3N19dxi1dxi2 = %s\n"%(expand(d2C3N19dxi1dxi2(xi1,xi2,xi3))))
print("d2C3N20dxi1dxi2 = %s\n"%(expand(d2C3N20dxi1dxi2(xi1,xi2,xi3))))

def d2C3N1dxi1dxi3(xi1,xi2,xi3):
    return diff(dC3N1dxi1(xi1,xi2,xi3),xi3)
def d2C3N2dxi1dxi3(xi1,xi2,xi3):
    return diff(dC3N2dxi1(xi1,xi2,xi3),xi3)
def d2C3N3dxi1dxi3(xi1,xi2,xi3):
    return diff(dC3N3dxi1(xi1,xi2,xi3),xi3)
def d2C3N4dxi1dxi3(xi1,xi2,xi3):
    return diff(dC3N4dxi1(xi1,xi2,xi3),xi3)
def d2C3N5dxi1dxi3(xi1,xi2,xi3):
    return diff(dC3N5dxi1(xi1,xi2,xi3),xi3)
def d2C3N6dxi1dxi3(xi1,xi2,xi3):
    return diff(dC3N6dxi1(xi1,xi2,xi3),xi3)
def d2C3N7dxi1dxi3(xi1,xi2,xi3):
    return diff(dC3N7dxi1(xi1,xi2,xi3),xi3)
def d2C3N8dxi1dxi3(xi1,xi2,xi3):
    return diff(dC3N8dxi1(xi1,xi2,xi3),xi3)
def d2C3N9dxi1dxi3(xi1,xi2,xi3):
    return diff(dC3N9dxi1(xi1,xi2,xi3),xi3)
def d2C3N10dxi1dxi3(xi1,xi2,xi3):
    return diff(dC3N10dxi1(xi1,xi2,xi3),xi3)
def d2C3N11dxi1dxi3(xi1,xi2,xi3):
    return diff(dC3N11dxi1(xi1,xi2,xi3),xi3)
def d2C3N12dxi1dxi3(xi1,xi2,xi3):
    return diff(dC3N12dxi1(xi1,xi2,xi3),xi3)
def d2C3N13dxi1dxi3(xi1,xi2,xi3):
    return diff(dC3N13dxi1(xi1,xi2,xi3),xi3)
def d2C3N14dxi1dxi3(xi1,xi2,xi3):
    return diff(dC3N14dxi1(xi1,xi2,xi3),xi3)
def d2C3N15dxi1dxi3(xi1,xi2,xi3):
    return diff(dC3N15dxi1(xi1,xi2,xi3),xi3)
def d2C3N16dxi1dxi3(xi1,xi2,xi3):
    return diff(dC3N16dxi1(xi1,xi2,xi3),xi3)
def d2C3N17dxi1dxi3(xi1,xi2,xi3):
    return diff(dC3N17dxi1(xi1,xi2,xi3),xi3)
def d2C3N18dxi1dxi3(xi1,xi2,xi3):
    return diff(dC3N18dxi1(xi1,xi2,xi3),xi3)
def d2C3N19dxi1dxi3(xi1,xi2,xi3):
    return diff(dC3N19dxi1(xi1,xi2,xi3),xi3)
def d2C3N20dxi1dxi3(xi1,xi2,xi3):
    return diff(dC3N20dxi1(xi1,xi2,xi3),xi3)

print("d2C3N1dxi1dxi3 = %s\n"%(expand(d2C3N1dxi1dxi3(xi1,xi2,xi3))))
print("d2C3N2dxi1dxi3 = %s\n"%(expand(d2C3N2dxi1dxi3(xi1,xi2,xi3))))
print("d2C3N3dxi1dxi3 = %s\n"%(expand(d2C3N3dxi1dxi3(xi1,xi2,xi3))))
print("d2C3N4dxi1dxi3 = %s\n"%(expand(d2C3N4dxi1dxi3(xi1,xi2,xi3))))
print("d2C3N5dxi1dxi3 = %s\n"%(expand(d2C3N5dxi1dxi3(xi1,xi2,xi3))))
print("d2C3N6dxi1dxi3 = %s\n"%(expand(d2C3N6dxi1dxi3(xi1,xi2,xi3))))
print("d2C3N7dxi1dxi3 = %s\n"%(expand(d2C3N7dxi1dxi3(xi1,xi2,xi3))))
print("d2C3N8dxi1dxi3 = %s\n"%(expand(d2C3N8dxi1dxi3(xi1,xi2,xi3))))
print("d2C3N9dxi1dxi3 = %s\n"%(expand(d2C3N9dxi1dxi3(xi1,xi2,xi3))))
print("d2C3N10dxi1dxi3 = %s\n"%(expand(d2C3N10dxi1dxi3(xi1,xi2,xi3))))
print("d2C3N11dxi1dxi3 = %s\n"%(expand(d2C3N11dxi1dxi3(xi1,xi2,xi3))))
print("d2C3N12dxi1dxi3 = %s\n"%(expand(d2C3N12dxi1dxi3(xi1,xi2,xi3))))
print("d2C3N13dxi1dxi3 = %s\n"%(expand(d2C3N13dxi1dxi3(xi1,xi2,xi3))))
print("d2C3N14dxi1dxi3 = %s\n"%(expand(d2C3N14dxi1dxi3(xi1,xi2,xi3))))
print("d2C3N15dxi1dxi3 = %s\n"%(expand(d2C3N15dxi1dxi3(xi1,xi2,xi3))))
print("d2C3N16dxi1dxi3 = %s\n"%(expand(d2C3N16dxi1dxi3(xi1,xi2,xi3))))
print("d2C3N17dxi1dxi3 = %s\n"%(expand(d2C3N17dxi1dxi3(xi1,xi2,xi3))))
print("d2C3N18dxi1dxi3 = %s\n"%(expand(d2C3N18dxi1dxi3(xi1,xi2,xi3))))
print("d2C3N19dxi1dxi3 = %s\n"%(expand(d2C3N19dxi1dxi3(xi1,xi2,xi3))))
print("d2C3N20dxi1dxi3 = %s\n"%(expand(d2C3N20dxi1dxi3(xi1,xi2,xi3))))

def d2C3N1dxi2dxi3(xi1,xi2,xi3):
    return diff(dC3N1dxi2(xi1,xi2,xi3),xi3)
def d2C3N2dxi2dxi3(xi1,xi2,xi3):
    return diff(dC3N2dxi2(xi1,xi2,xi3),xi3)
def d2C3N3dxi2dxi3(xi1,xi2,xi3):
    return diff(dC3N3dxi2(xi1,xi2,xi3),xi3)
def d2C3N4dxi2dxi3(xi1,xi2,xi3):
    return diff(dC3N4dxi2(xi1,xi2,xi3),xi3)
def d2C3N5dxi2dxi3(xi1,xi2,xi3):
    return diff(dC3N5dxi2(xi1,xi2,xi3),xi3)
def d2C3N6dxi2dxi3(xi1,xi2,xi3):
    return diff(dC3N6dxi2(xi1,xi2,xi3),xi3)
def d2C3N7dxi2dxi3(xi1,xi2,xi3):
    return diff(dC3N7dxi2(xi1,xi2,xi3),xi3)
def d2C3N8dxi2dxi3(xi1,xi2,xi3):
    return diff(dC3N8dxi2(xi1,xi2,xi3),xi3)
def d2C3N9dxi2dxi3(xi1,xi2,xi3):
    return diff(dC3N9dxi2(xi1,xi2,xi3),xi3)
def d2C3N10dxi2dxi3(xi1,xi2,xi3):
    return diff(dC3N10dxi2(xi1,xi2,xi3),xi3)
def d2C3N11dxi2dxi3(xi1,xi2,xi3):
    return diff(dC3N11dxi2(xi1,xi2,xi3),xi3)
def d2C3N12dxi2dxi3(xi1,xi2,xi3):
    return diff(dC3N12dxi2(xi1,xi2,xi3),xi3)
def d2C3N13dxi2dxi3(xi1,xi2,xi3):
    return diff(dC3N13dxi2(xi1,xi2,xi3),xi3)
def d2C3N14dxi2dxi3(xi1,xi2,xi3):
    return diff(dC3N14dxi2(xi1,xi2,xi3),xi3)
def d2C3N15dxi2dxi3(xi1,xi2,xi3):
    return diff(dC3N15dxi2(xi1,xi2,xi3),xi3)
def d2C3N16dxi2dxi3(xi1,xi2,xi3):
    return diff(dC3N16dxi2(xi1,xi2,xi3),xi3)
def d2C3N17dxi2dxi3(xi1,xi2,xi3):
    return diff(dC3N17dxi2(xi1,xi2,xi3),xi3)
def d2C3N18dxi2dxi3(xi1,xi2,xi3):
    return diff(dC3N18dxi2(xi1,xi2,xi3),xi3)
def d2C3N19dxi2dxi3(xi1,xi2,xi3):
    return diff(dC3N19dxi2(xi1,xi2,xi3),xi3)
def d2C3N20dxi2dxi3(xi1,xi2,xi3):
    return diff(dC3N20dxi2(xi1,xi2,xi3),xi3)

print("d2C3N1dxi2dxi3 = %s\n"%(expand(d2C3N1dxi2dxi3(xi1,xi2,xi3))))
print("d2C3N2dxi2dxi3 = %s\n"%(expand(d2C3N2dxi2dxi3(xi1,xi2,xi3))))
print("d2C3N3dxi2dxi3 = %s\n"%(expand(d2C3N3dxi2dxi3(xi1,xi2,xi3))))
print("d2C3N4dxi2dxi3 = %s\n"%(expand(d2C3N4dxi2dxi3(xi1,xi2,xi3))))
print("d2C3N5dxi2dxi3 = %s\n"%(expand(d2C3N5dxi2dxi3(xi1,xi2,xi3))))
print("d2C3N6dxi2dxi3 = %s\n"%(expand(d2C3N6dxi2dxi3(xi1,xi2,xi3))))
print("d2C3N7dxi2dxi3 = %s\n"%(expand(d2C3N7dxi2dxi3(xi1,xi2,xi3))))
print("d2C3N8dxi2dxi3 = %s\n"%(expand(d2C3N8dxi2dxi3(xi1,xi2,xi3))))
print("d2C3N9dxi2dxi3 = %s\n"%(expand(d2C3N9dxi2dxi3(xi1,xi2,xi3))))
print("d2C3N10dxi2dxi3 = %s\n"%(expand(d2C3N10dxi2dxi3(xi1,xi2,xi3))))
print("d2C3N11dxi2dxi3 = %s\n"%(expand(d2C3N11dxi2dxi3(xi1,xi2,xi3))))
print("d2C3N12dxi2dxi3 = %s\n"%(expand(d2C3N12dxi2dxi3(xi1,xi2,xi3))))
print("d2C3N13dxi2dxi3 = %s\n"%(expand(d2C3N13dxi2dxi3(xi1,xi2,xi3))))
print("d2C3N14dxi2dxi3 = %s\n"%(expand(d2C3N14dxi2dxi3(xi1,xi2,xi3))))
print("d2C3N15dxi2dxi3 = %s\n"%(expand(d2C3N15dxi2dxi3(xi1,xi2,xi3))))
print("d2C3N16dxi2dxi3 = %s\n"%(expand(d2C3N16dxi2dxi3(xi1,xi2,xi3))))
print("d2C3N17dxi2dxi3 = %s\n"%(expand(d2C3N17dxi2dxi3(xi1,xi2,xi3))))
print("d2C3N18dxi2dxi3 = %s\n"%(expand(d2C3N18dxi2dxi3(xi1,xi2,xi3))))
print("d2C3N19dxi2dxi3 = %s\n"%(expand(d2C3N19dxi2dxi3(xi1,xi2,xi3))))
print("d2C3N20dxi2dxi3 = %s\n"%(expand(d2C3N20dxi2dxi3(xi1,xi2,xi3))))

def d3C3N1dxi1dxi2dxi3(xi1,xi2,xi3):
    return diff(d2C3N1dxi1dxi2(xi1,xi2,xi3),xi3)
def d3C3N2dxi1dxi2dxi3(xi1,xi2,xi3):
    return diff(d2C3N2dxi1dxi2(xi1,xi2,xi3),xi3)
def d3C3N3dxi1dxi2dxi3(xi1,xi2,xi3):
    return diff(d2C3N3dxi1dxi2(xi1,xi2,xi3),xi3)
def d3C3N4dxi1dxi2dxi3(xi1,xi2,xi3):
    return diff(d2C3N4dxi1dxi2(xi1,xi2,xi3),xi3)
def d3C3N5dxi1dxi2dxi3(xi1,xi2,xi3):
    return diff(d2C3N5dxi1dxi2(xi1,xi2,xi3),xi3)
def d3C3N6dxi1dxi2dxi3(xi1,xi2,xi3):
    return diff(d2C3N6dxi1dxi2(xi1,xi2,xi3),xi3)
def d3C3N7dxi1dxi2dxi3(xi1,xi2,xi3):
    return diff(d2C3N7dxi1dxi2(xi1,xi2,xi3),xi3)
def d3C3N8dxi1dxi2dxi3(xi1,xi2,xi3):
    return diff(d2C3N8dxi1dxi2(xi1,xi2,xi3),xi3)
def d3C3N9dxi1dxi2dxi3(xi1,xi2,xi3):
    return diff(d2C3N9dxi1dxi2(xi1,xi2,xi3),xi3)
def d3C3N10dxi1dxi2dxi3(xi1,xi2,xi3):
    return diff(d2C3N10dxi1dxi2(xi1,xi2,xi3),xi3)
def d3C3N11dxi1dxi2dxi3(xi1,xi2,xi3):
    return diff(d2C3N11dxi1dxi2(xi1,xi2,xi3),xi3)
def d3C3N12dxi1dxi2dxi3(xi1,xi2,xi3):
    return diff(d2C3N12dxi1dxi2(xi1,xi2,xi3),xi3)
def d3C3N13dxi1dxi2dxi3(xi1,xi2,xi3):
    return diff(d2C3N13dxi1dxi2(xi1,xi2,xi3),xi3)
def d3C3N14dxi1dxi2dxi3(xi1,xi2,xi3):
    return diff(d2C3N14dxi1dxi2(xi1,xi2,xi3),xi3)
def d3C3N15dxi1dxi2dxi3(xi1,xi2,xi3):
    return diff(d2C3N15dxi1dxi2(xi1,xi2,xi3),xi3)
def d3C3N16dxi1dxi2dxi3(xi1,xi2,xi3):
    return diff(d2C3N16dxi1dxi2(xi1,xi2,xi3),xi3)
def d3C3N17dxi1dxi2dxi3(xi1,xi2,xi3):
    return diff(d2C3N17dxi1dxi2(xi1,xi2,xi3),xi3)
def d3C3N18dxi1dxi2dxi3(xi1,xi2,xi3):
    return diff(d2C3N18dxi1dxi2(xi1,xi2,xi3),xi3)
def d3C3N19dxi1dxi2dxi3(xi1,xi2,xi3):
    return diff(d2C3N19dxi1dxi2(xi1,xi2,xi3),xi3)
def d3C3N20dxi1dxi2dxi3(xi1,xi2,xi3):
    return diff(d2C3N20dxi1dxi2(xi1,xi2,xi3),xi3)

print("d3C3N1dxi1dxi2dxi3 = %s\n"%(expand(d3C3N1dxi1dxi2dxi3(xi1,xi2,xi3))))
print("d3C3N2dxi1dxi2dxi3 = %s\n"%(expand(d3C3N2dxi1dxi2dxi3(xi1,xi2,xi3))))
print("d3C3N3dxi1dxi2dxi3 = %s\n"%(expand(d3C3N3dxi1dxi2dxi3(xi1,xi2,xi3))))
print("d3C3N4dxi1dxi2dxi3 = %s\n"%(expand(d3C3N4dxi1dxi2dxi3(xi1,xi2,xi3))))
print("d3C3N5dxi1dxi2dxi3 = %s\n"%(expand(d3C3N5dxi1dxi2dxi3(xi1,xi2,xi3))))
print("d3C3N6dxi1dxi2dxi3 = %s\n"%(expand(d3C3N6dxi1dxi2dxi3(xi1,xi2,xi3))))
print("d3C3N7dxi1dxi2dxi3 = %s\n"%(expand(d3C3N7dxi1dxi2dxi3(xi1,xi2,xi3))))
print("d3C3N8dxi1dxi2dxi3 = %s\n"%(expand(d3C3N8dxi1dxi2dxi3(xi1,xi2,xi3))))
print("d3C3N9dxi1dxi2dxi3 = %s\n"%(expand(d3C3N9dxi1dxi2dxi3(xi1,xi2,xi3))))
print("d3C3N10dxi1dxi2dxi3 = %s\n"%(expand(d3C3N10dxi1dxi2dxi3(xi1,xi2,xi3))))
print("d3C3N11dxi1dxi2dxi3 = %s\n"%(expand(d3C3N11dxi1dxi2dxi3(xi1,xi2,xi3))))
print("d3C3N12dxi1dxi2dxi3 = %s\n"%(expand(d3C3N12dxi1dxi2dxi3(xi1,xi2,xi3))))
print("d3C3N13dxi1dxi2dxi3 = %s\n"%(expand(d3C3N13dxi1dxi2dxi3(xi1,xi2,xi3))))
print("d3C3N14dxi1dxi2dxi3 = %s\n"%(expand(d3C3N14dxi1dxi2dxi3(xi1,xi2,xi3))))
print("d3C3N15dxi1dxi2dxi3 = %s\n"%(expand(d3C3N15dxi1dxi2dxi3(xi1,xi2,xi3))))
print("d3C3N16dxi1dxi2dxi3 = %s\n"%(expand(d3C3N16dxi1dxi2dxi3(xi1,xi2,xi3))))
print("d3C3N17dxi1dxi2dxi3 = %s\n"%(expand(d3C3N17dxi1dxi2dxi3(xi1,xi2,xi3))))
print("d3C3N18dxi1dxi2dxi3 = %s\n"%(expand(d3C3N18dxi1dxi2dxi3(xi1,xi2,xi3))))
print("d3C3N19dxi1dxi2dxi3 = %s\n"%(expand(d3C3N19dxi1dxi2dxi3(xi1,xi2,xi3))))
print("d3C3N20dxi1dxi2dxi3 = %s\n"%(expand(d3C3N20dxi1dxi2dxi3(xi1,xi2,xi3))))


