
from geographiclib.geodesic import Geodesic
from math import sin,cos,atan,radians,degrees,sqrt,pi
geod = Geodesic.WGS84
a = geod.a 
f = geod.f 
esq =f*(2-f)

x = -986191.859500
y = 5975733.405300
z = 1993725.945500

p = 18.33534070827
l = 99.37121312036
h = 240.173055

def Geodetic2Cartesian(phi,lamda,h):
    N = a / sqrt(1-esq*(sin(radians(phi))**2))
    X = (N+h)*cos(radians(phi))*cos(radians(lamda))
    Y = (N+h)*cos(radians(phi))*sin(radians(lamda))
    Z = ((1-esq)*N + h )*sin(radians(phi))
    return print('X = {:.4f} m Y = {:.4f} m Z = {:.4f} m'.format(X,Y,Z))

def Cartesian2Geodetic(X,Y,Z):
    ## lamda
    if X > 0 and Y > 0 :
        lamda = (atan(Y/X))
    elif (X < 0 and Y > 0) or (X < 0 and Y < 0):
        lamda = pi + (atan(Y/X))
    else :
        lamda = 2*pi - (atan(Y/X))
    ## phi 
    iter = 100
    tol =  1E-5
    found = False
    phi = 0
    N = a / sqrt(1-esq*(sin(phi)**2))
    for i in range(iter):
        phinew = atan(
            ((Z+esq*N*sin(phi))/sqrt(X**2+Y**2))
        )
        if abs(phi-phinew) < tol :
            found = True
        phi = phinew 
        N = N = a / sqrt(1-esq*(sin(phi)**2))
        h = (sqrt(X**2+Y**2)/cos(phi)) - N
        if found :
            break
    return print(
    'Phi = {:.4f} deg Lamda = {:.4f} deg h = {:.4f} m'.format(degrees(phi),degrees(lamda),h)
    )
def vermeille(X,Y,Z):
    if X > 0 and Y > 0 :
        lamda = (atan(Y/X))
    elif (X < 0 and Y > 0) or (X < 0 and Y < 0):
        lamda = pi + (atan(Y/X))
    else :
        lamda = 2*pi - (atan(Y/X))
    p = (X**2+Y**2)/a**2
    q = (Z**2)*((1-esq)/a**2)
    r = (p+q-esq**2)/6
    u = r + 0.5*(sqrt(8*r**3 + esq**2*p*q)+sqrt(p*q*esq**2))**(2/3) + \
        0.5*(sqrt(8*r**3 + esq**2*p*q)-sqrt(p*q*esq**2))**(2/3)
    v = sqrt(u**2 + q*esq**2)
    w = ((u+v-q)/(2*v))*esq
    k = (u+v)/(sqrt(w**2 + u + v)+w)
    D = k*(sqrt(X**2+Y**2)/(k+esq))
    h = ((k+(esq)-1)/(k))*(sqrt(D**2+Z**2))
    phi = 2*atan(Z/(sqrt(D**2+Z**2)+D))
    return print(
    'Phi = {:.4f} deg Lamda = {:.4f} deg h = {:.4f} m'.format(degrees(phi),degrees(lamda),h)
    )

## Transform Coordinate
#Geodetic2Cartesian
Geodetic2Cartesian(p,l,h)
#Cartesian2Geodetic
Cartesian2Geodetic(x,y,z)
#Vermeille
vermeille(x,y,z)
