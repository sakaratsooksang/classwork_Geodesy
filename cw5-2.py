#cw5-2
# Tampa General Hospital Brandon Healthplex Heliport
# 27.929372 -82.336981 11.2776 m(37ft)

import matplotlib.pyplot as plt
import numpy as np
from geographiclib.geodesic import Geodesic
from math import sin,cos,atan,radians,degrees,sqrt,pi
geod = Geodesic.WGS84
a = geod.a 
f = geod.f 
esq =f*(2-f)
b = sqrt(a**2-esq*a**2)

phi = 27.929372
ga = 9.7803267715
gb = 9.8321863685

def Somiglia(phi) :
    normg = (
        (a*ga*cos(radians(phi))**2+b*gb*sin(radians(phi))**2)/sqrt((cos(radians(phi))**2)*a**2+(sin(radians(phi))**2)*b**2)
    )
    return print('Normal Gravity by Somiglia = {:.5f} m/s^2'.format(normg))

def Moritz(phi) :
    k = ((b*gb)/(a*ga))-1
    normg = (
        ga*( ( 1+k*sin(radians(phi))**2 ) / sqrt(1-esq*(sin(radians(phi)))**2) )
    )
    return print('Normal Gravity by Moritz = {:.5f} m/s^2'.format(normg))
    
Somiglia(phi)
Moritz(phi)
