from sympy import *

xi, xi1, xi2, xi3 = symbols('xi,xi1,xi2,xi3')

print("\n\nLinear Lagrange Basis Functions:\n\n")

def LPhi1(xi):
    return 1-xi
def LPhi2(xi):
    return xi

print("LPhi1 = %s\n"%(expand(LPhi1(xi))))
print("LPhi2 = %s\n"%(expand(LPhi2(xi))))

def dLPhi1dxi(xi):
    return diff(LPhi1(xi),xi)
def dLPhi2dxi(xi):
    return diff(LPhi2(xi),xi)

print("dLPhi1dxi = %s\n"%(expand(dLPhi1dxi(xi))))
print("dLPhi2dxi = %s\n"%(expand(dLPhi2dxi(xi))))

def d2LPhi1dxidxi(xi):
    return diff(dLPhi1dxi(xi),xi)
def d2LPhi2dxidxi(xi):
    return diff(dLPhi2dxi(xi),xi)

print("d2LPhi1dxidxi = %s\n"%(expand(d2LPhi1dxidxi(xi))))
print("d2LPhi2dxidxi = %s\n"%(expand(d2LPhi2dxidxi(xi))))

print("\n\nBilinear Lagranage Basis Functions:\n\n")

def LPhi11(xi1,xi2):
    return LPhi1(xi1)*LPhi1(xi2)
def LPhi21(xi1,xi2):
    return LPhi2(xi1)*LPhi1(xi2)
def LPhi12(xi1,xi2):
    return LPhi1(xi1)*LPhi2(xi2)
def LPhi22(xi1,xi2):
    return LPhi2(xi1)*LPhi2(xi2)

print("LPhi11 = %s\n"%(expand(LPhi11(xi1,xi2))))
print("LPhi21 = %s\n"%(expand(LPhi21(xi1,xi2))))
print("LPhi12 = %s\n"%(expand(LPhi12(xi1,xi2))))
print("LPhi22 = %s\n"%(expand(LPhi22(xi1,xi2))))

def dLPhi11dxi1(xi1,xi2):
    return diff(LPhi11(xi1,xi2),xi1)
def dLPhi21dxi1(xi1,xi2):
    return diff(LPhi21(xi1,xi2),xi1)
def dLPhi12dxi1(xi1,xi2):
    return diff(LPhi12(xi1,xi2),xi1)
def dLPhi22dxi1(xi1,xi2):
    return diff(LPhi22(xi1,xi2),xi1)

print("dLPhi11dxi1 = %s\n"%(expand(dLPhi11dxi1(xi1,xi2))))
print("dLPhi21dxi1 = %s\n"%(expand(dLPhi21dxi1(xi1,xi2))))
print("dLPhi12dxi1 = %s\n"%(expand(dLPhi12dxi1(xi1,xi2))))
print("dLPhi22dxi1 = %s\n"%(expand(dLPhi22dxi1(xi1,xi2))))

def dLPhi11dxi2(xi1,xi2):
    return diff(LPhi11(xi1,xi2),xi2)
def dLPhi21dxi2(xi1,xi2):
    return diff(LPhi21(xi1,xi2),xi2)
def dLPhi12dxi2(xi1,xi2):
    return diff(LPhi12(xi1,xi2),xi2)
def dLPhi22dxi2(xi1,xi2):
    return diff(LPhi22(xi1,xi2),xi2)

print("dLPhi11dxi2 = %s\n"%(expand(dLPhi11dxi2(xi1,xi2))))
print("dLPhi21dxi2 = %s\n"%(expand(dLPhi21dxi2(xi1,xi2))))
print("dLPhi12dxi2 = %s\n"%(expand(dLPhi12dxi2(xi1,xi2))))
print("dLPhi22dxi2 = %s\n"%(expand(dLPhi22dxi2(xi1,xi2))))

def d2LPhi11dxi1dxi1(xi1,xi2):
    return diff(dLPhi11dxi1(xi1,xi2),xi1)
def d2LPhi21dxi1dxi1(xi1,xi2):
    return diff(dLPhi21dxi1(xi1,xi2),xi1)
def d2LPhi12dxi1dxi1(xi1,xi2):
    return diff(dLPhi12dxi1(xi1,xi2),xi1)
def d2LPhi22dxi1dxi1(xi1,xi2):
    return diff(dLPhi22dxi1(xi1,xi2),xi1)

print("d2LPhi11dxi1dxi1 = %s\n"%(expand(d2LPhi11dxi1dxi1(xi1,xi2))))
print("d2LPhi21dxi1dxi1 = %s\n"%(expand(d2LPhi21dxi1dxi1(xi1,xi2))))
print("d2LPhi12dxi1dxi1 = %s\n"%(expand(d2LPhi12dxi1dxi1(xi1,xi2))))
print("d2LPhi22dxi1dxi1 = %s\n"%(expand(d2LPhi22dxi1dxi1(xi1,xi2))))

def d2LPhi11dxi2dxi2(xi1,xi2):
    return diff(dLPhi11dxi2(xi1,xi2),xi2)
def d2LPhi21dxi2dxi2(xi1,xi2):
    return diff(dLPhi21dxi2(xi1,xi2),xi2)
def d2LPhi12dxi2dxi2(xi1,xi2):
    return diff(dLPhi12dxi2(xi1,xi2),xi2)
def d2LPhi22dxi2dxi2(xi1,xi2):
    return diff(dLPhi22dxi2(xi1,xi2),xi2)

print("d2LPhi11dxi2dxi2 = %s\n"%(expand(d2LPhi11dxi2dxi2(xi1,xi2))))
print("d2LPhi21dxi2dxi2 = %s\n"%(expand(d2LPhi21dxi2dxi2(xi1,xi2))))
print("d2LPhi12dxi2dxi2 = %s\n"%(expand(d2LPhi12dxi2dxi2(xi1,xi2))))
print("d2LPhi22dxi2dxi2 = %s\n"%(expand(d2LPhi22dxi2dxi2(xi1,xi2))))

def d2LPhi11dxi1dxi2(xi1,xi2):
    return diff(dLPhi11dxi1(xi1,xi2),xi2)
def d2LPhi21dxi1dxi2(xi1,xi2):
    return diff(dLPhi21dxi1(xi1,xi2),xi2)
def d2LPhi12dxi1dxi2(xi1,xi2):
    return diff(dLPhi12dxi1(xi1,xi2),xi2)
def d2LPhi22dxi1dxi2(xi1,xi2):
    return diff(dLPhi22dxi1(xi1,xi2),xi2)

print("d2LPhi11dxi1dxi2 = %s\n"%(expand(d2LPhi11dxi1dxi2(xi1,xi2))))
print("d2LPhi21dxi1dxi2 = %s\n"%(expand(d2LPhi21dxi1dxi2(xi1,xi2))))
print("d2LPhi12dxi1dxi2 = %s\n"%(expand(d2LPhi12dxi1dxi2(xi1,xi2))))
print("d2LPhi22dxi1dxi2 = %s\n"%(expand(d2LPhi22dxi1dxi2(xi1,xi2))))


print("\n\nTrilinear Lagranage Basis Functions:\n\n")

def LPhi111(xi1,xi2,xi3):
    return LPhi1(xi1)*LPhi1(xi2)*LPhi1(xi3)
def LPhi211(xi1,xi2,xi3):
    return LPhi2(xi1)*LPhi1(xi2)*LPhi1(xi3)
def LPhi121(xi1,xi2,xi3):
    return LPhi1(xi1)*LPhi2(xi2)*LPhi1(xi3)
def LPhi221(xi1,xi2,xi3):
    return LPhi2(xi1)*LPhi2(xi2)*LPhi1(xi3)
def LPhi112(xi1,xi2,xi3):
    return LPhi1(xi1)*LPhi1(xi2)*LPhi2(xi3)
def LPhi212(xi1,xi2,xi3):
    return LPhi2(xi1)*LPhi1(xi2)*LPhi2(xi3)
def LPhi122(xi1,xi2,xi3):
    return LPhi1(xi1)*LPhi2(xi2)*LPhi2(xi3)
def LPhi222(xi1,xi2,xi3):
    return LPhi2(xi1)*LPhi2(xi2)*LPhi2(xi3)

print("LPhi111 = %s\n"%(expand(LPhi111(xi1,xi2,xi3))))
print("LPhi211 = %s\n"%(expand(LPhi211(xi1,xi2,xi3))))
print("LPhi121 = %s\n"%(expand(LPhi121(xi1,xi2,xi3))))
print("LPhi221 = %s\n"%(expand(LPhi221(xi1,xi2,xi3))))
print("LPhi112 = %s\n"%(expand(LPhi112(xi1,xi2,xi3))))
print("LPhi212 = %s\n"%(expand(LPhi212(xi1,xi2,xi3))))
print("LPhi122 = %s\n"%(expand(LPhi122(xi1,xi2,xi3))))
print("LPhi222 = %s\n"%(expand(LPhi222(xi1,xi2,xi3))))


def QPhi1(xi):
    return 2*(xi-1/2)*(xi-1)
def QPhi2(xi):
    return 4*xi*(1-xi)
def QPhi3(xi):
    return 2*xi*(xi-1/2)
def CPhi1(xi):
    return 1/2*(3*xi-1)*(3*xi-2)*(1-xi)
def CPhi2(xi):
    return 9/2*(3*xi-2)*(xi-1)
def CPhi3(xi):
    return 9/2*(3*xi-1)*(1-xi)
def CPhi4(xi):
    return 1/2*xi*(3*xi-1)*(3*xi-2)



