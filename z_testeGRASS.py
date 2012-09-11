import os
import sys

#http://www.kyngchaos.com/software/grass
#http://grass.osgeo.org/wiki/GRASS_Python_Scripting_Library
#http://code.google.com/p/postgis-grass-r-py/wiki/0003_01_PythonForGrassGis

# env setup
gisbase = os.environ['GISBASE'] = "/Applications/GRASS/GRASS-7.0.app/Contents/MacOS/"
     
gisdbase = os.path.join(os.environ['HOME'], "Desktop/gisData/grassData")
location = "southAmerica"
mapset   = "southAmerica_mapset"

sys.path.append(os.path.join(os.environ['GISBASE'], "etc", "python"))

import grass.script as grass
import grass.script.setup as gsetup


class grass_app(object):
    def __init__(self):
        gsetup.init(gisbase,
                    gisdbase, location, mapset)


    def run_app(self):
        print grass.gisenv()
         
        grass.message('Raster maps:')
        for rast in grass.list_strings(type = 'rast'):
            print rast
            
        grass.message('Vector maps:')
        for v in grass.list_strings(type = 'vect'):
            print v
            
        r = grass.read_command("g.region", flags='p' )
        print r

if __name__ == '__main__':
    app = grass_app()
    app.run_app()