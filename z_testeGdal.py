import numpy as np
import matplotlib as mpl
from matplotlib import pylab 
from osgeo import gdal


def print_dataset_info(dataset=None):
    
    print 'Driver: ', dataset.GetDriver().ShortName,'/', \
          dataset.GetDriver().LongName
    print 'Size is ',dataset.RasterXSize,'x',dataset.RasterYSize, \
          'x',dataset.RasterCount
    print 'Projection is ',dataset.GetProjection()
    
    geotransform = dataset.GetGeoTransform()
    if not geotransform is None:
        print 'Origin = (',geotransform[0], ',',geotransform[3],')'
        print 'Pixel Size = (',geotransform[1], ',',geotransform[5],')'


def plot_dataset():
    
    #topo2 = topo[topo > -32000]
    #fair = fair[fair > -32000]
    #boug = boug[boug > -32000]
    #isos = isos[isos > -32000]
    
    #mpl.pylab.imshow(topo, interpolation='nearest', vmin=-8000, cmap=mpl.pylab.cm.gist_earth)
    mpl.pylab.imshow(topo, interpolation='nearest', vmin=-8500, cmap=mpl.pyplot.cm.gist_earth)
    mpl.pylab.title("Topografia")
    mpl.pylab.colorbar()
    mpl.pylab.show()
    mpl.pylab.clf()
    
    mpl.pylab.imshow(fair, interpolation='nearest', vmin=-140, cmap=mpl.pylab.cm.gist_rainbow)
    mpl.pylab.title("Anomalia Ar-Livre")
    mpl.pylab.colorbar()
    mpl.pylab.show()
    mpl.pylab.clf()
    
    mpl.pylab.imshow(boug, interpolation='nearest', cmap=mpl.pylab.cm.gist_rainbow)
    mpl.pylab.title("Anomalia Bouger")
    mpl.pylab.colorbar()
    mpl.pylab.show()
    mpl.pylab.clf()
    
    mpl.pylab.imshow(isos, interpolation='nearest', vmin=-80, vmax=80, cmap=mpl.pylab.cm.gist_rainbow)
    mpl.pylab.title("Anomalia Isostatica")
    mpl.pylab.colorbar()
    mpl.pylab.show()
    mpl.pylab.clf()



def colormap_plot():
    
    import numpy as np
    import matplotlib.pyplot as plt
    
    a = np.linspace(0, 1, 256).reshape(1,-1)
    a = np.vstack((a,a))
    
    # Get a list of the colormaps in matplotlib.  Ignore the ones that end with
    # '_r' because these are simply reversed versions of ones that don't end
    # with '_r'
    maps = sorted(m for m in plt.cm.datad if not m.endswith("_r"))
    nmaps = len(maps) + 1
    
    fig = plt.figure(figsize=(5,10))
    fig.subplots_adjust(top=0.99, bottom=0.01, left=0.2, right=0.99)
    for i,m in enumerate(maps):
        ax = plt.subplot(nmaps, 1, i+1)
        plt.axis("off")
        plt.imshow(a, aspect='auto', cmap=plt.get_cmap(m), origin='lower')
        pos = list(ax.get_position().bounds)
        fig.text(pos[0] - 0.01, pos[1], m, fontsize=10, horizontalalignment='right')
    
    plt.show()


gdal_dataset = gdal.Open("datasets/southAmerica_topo_fa_bg_iso.tif")

print_dataset_info(gdal_dataset)

#print gdal_dataset.RasterCount

band_topo = gdal_dataset.GetRasterBand(1)
band_fair = gdal_dataset.GetRasterBand(2)
band_boug = gdal_dataset.GetRasterBand(3)
band_isos = gdal_dataset.GetRasterBand(4)


band_topo.ComputeBandStats()


topo = band_topo.ReadAsArray()
fair = band_fair.ReadAsArray()
boug = band_boug.ReadAsArray()
isos = band_isos.ReadAsArray()

plot_dataset()


