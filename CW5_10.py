from geographiclib.geodesic import Geodesic
from math import sin,cos,atan,radians,degrees,sqrt,pi
#WGS84
geod = Geodesic.WGS84
aWGS84 = geod.a 
fWGS84 = geod.f 
#ID1975
aID = 6377276.345
fID = 1/300.8017

def dms2dd(dms):
    d,m,s = dms.split(':')
    dd = float(d)+float(m)/60 +float(s)/3600
    return dd
# GNSS610279 WGS84
phiWGS84_610279 = '14:5:50.85995'
LamdaWGS84_610279 = '101:10:17.15426'
hWGS84_610279 = -23.052
phi1 = dms2dd(phiWGS84_610279)
lamda1 = dms2dd(LamdaWGS84_610279)
h1 = hWGS84_610279
# GNSS610279 ID1975
phiID_610279 = '14:5:44.94096'
LamdaID75_610279 = '101:10:29.25525'
hID1975_610279 = -3.888
phi2 = dms2dd(phiID_610279)
lamda2 = dms2dd(LamdaID75_610279)
h2 = hID1975_610279
# GNSS610280 WGS84
phiWGS84_610280 = '14:5:39.47155'
LamdaWGS84_610280 = '101:10:17.30072'
hWGS84_610280 = -21.963
phi3 = dms2dd(phiWGS84_610280)
lamda3 = dms2dd(LamdaWGS84_610280)
h3 = hWGS84_610280
# GNSS610280 ID1975
phiID75_610280 = '14:5:33.55165'
LamdaID75_610280 = '101:10:29.40156'
hID1975_610280 = -2.789
phi4 = dms2dd(phiID75_610280)
lamda4 = dms2dd(LamdaID75_610280)
h4 = hID1975_610280
def Geodetic2Cartesian(phi,lamda,h,a,f):
    esq = f*(2-f)
    N = a / sqrt(1-esq*(sin(radians(phi))**2))
    X = (N+h)*cos(radians(phi))*cos(radians(lamda))
    Y = (N+h)*cos(radians(phi))*sin(radians(lamda))
    Z = ((1-esq)*N + h )*sin(radians(phi))
    return X,Y,Z
def vermeille(X,Y,Z,a,f):
    esq = f*(2-f)
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
    return phi,lamda,h

dx,dy,dz = 204.4798 , 837.8940 , 294.7765
Xi,Yi,Zi = Geodetic2Cartesian(phi2,lamda2,h2,aID,fID)
# Shift origin
Xt = Xi + dx
Yt = Yi + dy
Zt = Zi + dz
PHI, LAMDA , H = vermeille(Xt,Yt,Zt,aWGS84,fWGS84)
print('GNSS-610279 กรมชล')
print('Latitude = {:.4f} deg Longitude = {:.4f} deg Geodetic Height = {:.3f} m'.format(phi1,lamda1,h1))
print('GNSS-610279 ที่คำนวณได้')
print('Latitude = {:.4f} deg Longitude = {:.4f} deg Geodetic Height = {:.3f} m'.format(degrees(PHI),degrees(LAMDA),H))
Xi,Yi,Zi = Geodetic2Cartesian(phi4,lamda4,h4,aID,fID)
# Shift origin
Xt = Xi + dx
Yt = Yi + dy
Zt = Zi + dz
PHI, LAMDA , H = vermeille(Xt,Yt,Zt,aWGS84,fWGS84)
print('GNSS-610280 กรมชล')
print('Latitude = {:.4f} deg Longitude = {:.4f} deg Geodetic Height = {:.3f} m'.format(phi3,lamda3,h3))
print('GNSS-610280 ที่คำนวณได้')
print('Latitude = {:.4f} deg Longitude = {:.4f} deg Geodetic Height = {:.3f} m'.format(degrees(PHI),degrees(LAMDA),H))
