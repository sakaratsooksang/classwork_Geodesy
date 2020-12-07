# เปลี่ยนพิกัดก่อน ข้อนี้ควรทำในคอมเพราะต้อง write file
# edit for macos.
# CW_5_4_GeoidIsoKML : plot isoline of spectified geoid model
#
#
import os
import subprocess as sp
import numpy as np
import matplotlib.pyplot as plt

###########################################################################
def GeoidEval( x,y ):
    CMD  = '/usr/local/Cellar/geographiclib/1.50.1/bin/GeoidEval -n tgm2017-1 --input-string "{lat} {lng}" '.\
           format( lng=x, lat=y )
    res = sp.run( CMD, shell=True,  capture_output=True )
    undul = float( res.stdout.decode('utf-8') )
    #print( x,y, undul )
    return undul

##########################################################################
# e.g. Korat
ymin, xmin, ymax, xmax = 14.033783, 100.874236, 15.790706, 103.049529 
NUM = 20
xp = np.linspace( xmin, xmax, num=NUM, endpoint=True )
yp = np.linspace( ymin, ymax, num=NUM, endpoint=True )
X,Y = np.meshgrid(xp, yp)
#Z = f( X, Y )
vfunc = np.vectorize( GeoidEval )
Z = vfunc( X,Y )

##########################################################################
with open('GeoidGrid.xyz', 'w') as f:
    for x,y,z in zip( X.ravel(),Y.ravel(),Z.ravel() ):
        #print( x,y,z) 
        f.write(f'{x} {y} {z}\r\n')

##########################################################################
CMD_TRANS = 'gdal_translate -ot Float32 GeoidGrid.xyz GeoidGrid.tif'
res = sp.run( CMD_TRANS, shell=True,  capture_output=True )
print( res )

##########################################################################
CMD_CONTO = 'gdal_contour -a Undulation -3d -f KML -i 0.5  GeoidGrid.tif GeoidGrid.kml'
res = sp.run( CMD_CONTO, shell=True,  capture_output=True )
print( res )

#import pdb; pdb.set_trace()
