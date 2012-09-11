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
        
        
        bsb_shp="/Users/pirchiner/Documents/ws_indigo/MMD_TFinal/resources/gis_data/bsb_br.shp"
        bsb_grass="test_in_ogr"
        grass.run_command("v.in.ogr", 
                          dsn=bsb_shp, 
                          output=bsb_grass,
                          #layer="1",
                          type="point",
                          overwrite=True)

        faults_shp="/Users/pirchiner/Documents/ws_indigo/MMD_TFinal/resources/gis_data/faults_semNE.shp"
        faults_grass="faults_semNE_grass"
        grass.run_command("v.in.ogr", 
                          dsn=faults_shp,
                          output=faults_grass,
                          #layer="1",
                          type="line",
                          overwrite=True)
        
        distances_grass = "tmp_distances3"
        grass.run_command("v.distance",
                          _from=bsb_grass, 
                          to=faults_grass, 
                          output=distances_grass+"_raw", 
                          overwrite=True, 
                          upload="cat", 
                          column="cat")

        grass.run_command("v.category", 
                          input=distances_grass+"_raw", 
                          output=distances_grass,
                          #layer=1, 
                          type="line", 
                          op="add",
                          overwrite=True)

        grass.run_command("v.db.addtable", 
                          map=distances_grass,
                          #table=distances_grass+"_table",
                          column="dist DOUBLE",
                          #layer=1,
                          overwrite=True)
#        grass.run_command("v.db.connect", 
#                          driver="sqlite",
#                          map=distances_grass,
#                          )
        print "bla"
        grass.run_command("v.to.db", 
                          map=distances_grass, 
                          option="length", 
                          column="dist",
                          #layer=1,
                          overwrite=True)

        grass.run_command("v.univar", 
                          map=distances_grass, 
                          column="dist")


if __name__ == '__main__':
    app = grass_app()
    app.run_app()