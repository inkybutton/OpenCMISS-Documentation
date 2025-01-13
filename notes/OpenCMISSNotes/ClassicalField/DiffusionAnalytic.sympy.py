from sympy import *

u, x, y, z, t = symbols("u,x,y,z,t")
A, B, C, D, E, F, G, H, I, J, K, L = symbols("A,B,C,D,E,F,G,H,I,J,K,L")
a, b, c, k = symbols("a,b,c,k")
alpha, beta, lamda, mu, phi, sigma = symbols("alpha,beta,lamda,mu,phi,sigma")

u = A*exp(4*pi**2*sigma*t/(L**2))*cos(2*pi*x/L + B) + C

dudt = simplify(u.diff(t))
d2udt2 = simplify(dudt.diff(t))
dudx = simplify(u.diff(x))
d2udx2 = simplify(dudx.diff(x))

resid = simplify(dudt + sigma*d2udx2)

print("")
print("resid = ",resid)
print("u = ",u)
print("dudt = ",dudt)
print("d2udt2 = ",d2udt2)
print("dudx = ",dudx)
print("d2udx2 = ",d2udx2)


u = A*exp((4*pi**2*sigma*(H**2*cos(phi)**2+L**2*sin(phi)**2)/(L**2*H**2))*t)*sin(2*pi*x*cos(phi)/L+2*pi*y*sin(phi)/H)

dudt = simplify(u.diff(t))
d2udt2 = simplify(dudt.diff(t))
dudx = simplify(u.diff(x))
d2udx2 = simplify(dudx.diff(x))
dudy = simplify(u.diff(y))
d2udy2 = simplify(dudy.diff(y))
d2udxdy= simplify(dudx.diff(y))

resid = simplify(dudt + sigma*(d2udx2+d2udy2))

print("")
print("resid = ",resid)
print("u = ",u)
print("dudt = ",dudt)
print("d2udt2 = ",d2udt2)
print("dudx = ",dudx)
print("d2udx2 = ",d2udx2)
print("dudy = ",dudy)
print("d2udy2 = ",d2udy2)
print("d2udxdy = ",d2udxdy)



u = A*exp(-t)*(x**2+y**2+z**2)

dudt = simplify(u.diff(t))
d2udt2 = simplify(dudt.diff(t))
dudx = simplify(u.diff(x))
d2udx2 = simplify(dudx.diff(x))
dudy = simplify(u.diff(y))
d2udy2 = simplify(dudy.diff(y))
dudz = simplify(u.diff(z))
d2udz2 = simplify(dudz.diff(z))
d2udxdy = simplify(dudx.diff(y))
d2udxdz = simplify(dudx.diff(z))
d2udydz = simplify(dudy.diff(z))

resid = simplify(dudt - (d2udx2+d2udy2+d2udz2))

print("")
print("resid = ",resid)
print("u = ",u)
print("dudt = ",dudt)
print("d2udt2 = ",d2udt2)
print("dudx = ",dudx)
print("d2udx2 = ",d2udx2)
print("dudy = ",dudy)
print("d2udy2 = ",d2udy2)
print("dudz = ",dudz)
print("d2udz2 = ",d2udz2)
print("d2udxdy = ",d2udxdy)
print("d2udxdz = ",d2udxdz)
print("d2udydz = ",d2udydz)

#beta = sqrt(-c/b)
#lamda =5*b/6
#mu = sqrt(-b/6)

u = 1/((sqrt(c/b)+A*exp(5*b*t/6-sqrt(b/6)*x))**2)

dudt = simplify(u.diff(t))
d2udt2 = simplify(dudt.diff(t))
dudx = simplify(u.diff(x))
d2udx2 = simplify(dudx.diff(x))

resid = simplify(dudt + d2udx2 + b*u + c*u**2)

print("")
print("resid = ",resid)
print("u = ",u)
print("dudt = ",dudt)
print("d2udt2 = ",d2udt2)
print("dudx = ",dudx)
print("d2udx2 = ",d2udx2)

beta = sqrt(-b/a)
mu = sqrt(-a*c/2)

u = (-2/c)*ln(sqrt(b)+A*exp(c*x-c*t/2))

dudt = simplify(u.diff(t))
d2udt2 = simplify(dudt.diff(t))
dudx = simplify(u.diff(x))
d2udx2 = simplify(dudx.diff(x))

resid = simplify(dudt - d2udx2 -1 + b*exp(c*x))

print("")
print("resid = ",resid)
print("u = ",u)
print("dudt = ",dudt)
print("d2udt2 = ",d2udt2)
print("dudx = ",dudx)
print("d2udx2 = ",d2udx2)


