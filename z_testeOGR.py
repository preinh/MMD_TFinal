import matplotlib as mp
import numpy as np

def makeGrid(Ox=0, Oy=0, dx=10, dy=10, nx=None, ny=None, Fx=90, Fy=180):

    nx = (Fx - Ox)/dx
    ny = (Fy - Oy)/dy
            
    for x in range(Ox, Fx, dx):
        for y in range(Oy, Fy, dy):
            print (x,y)
        
    for x in np.linspace(Ox, Fx, nx):
        for y in np.linspace(Oy, Fy, ny):
            print (x,y)    


def write_shape(fileName="tmp2.shp", layerName="layser"):
    
    import sys
    import string
    from osgeo import ogr
    
    driverName = "ESRI Shapefile"
    drv = ogr.GetDriverByName(driverName)
    
    if drv is None:
        print "%s driver not available.\n" % driverName
        sys.exit( 1 )

    ds = drv.CreateDataSource( fileName )
    if ds is None:
        print "Creation of output file failed.\n"
        sys.exit( 1 )
    
    lyr = ds.CreateLayer( layerName, None, ogr.wkbPoint )
    if lyr is None:
        print "Layer creation failed.\n"
        sys.exit( 1 )
    
    field_defn = ogr.FieldDefn( "Name", ogr.OFTString )
    field_defn.SetWidth( 32 )
    
    if lyr.CreateField ( field_defn ) != 0:
        print "Creating Name field failed.\n"
        sys.exit( 1 )

    print fileName
    
    # Expected format of user input: x y name
    linestring = raw_input()
    linelist = string.split(linestring)
    
    while len(linelist) == 3:
        x = float(linelist[0])
        y = float(linelist[1])
        name = linelist[2]
    
        feat = ogr.Feature( lyr.GetLayerDefn())
        feat.SetField( "Name",  name )
    
        pt = ogr.Geometry(ogr.wkbPoint)
        pt.SetPoint_2D(0, x, y)
    
        feat.SetGeometry(pt)
    
        if lyr.CreateFeature(feat) != 0:
            print "Failed to create feature in shapefile.\n"
            sys.exit( 1 )
    
        feat.Destroy()
    
        linestring = raw_input()
        linelist = string.split(linestring)
    
    ds = None


if __name__ == '__main__':
    #makeGrid(Ox=-95, Oy=-65, Fx=-20, Fy=25, dx=1, dy=1)
    write_shape()
    
