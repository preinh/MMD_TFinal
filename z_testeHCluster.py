import matplotlib as mp
from hcluster import pdist, linkage, dendrogram
import numpy as np
from numpy.random import rand

X = rand(10,100)
X[0:5,:] *= 2
Y = pdist(X)
Z = linkage(Y)
dendrogram(Z, no_plot=False )

mp.pylab.draw()
mp.pylab.show()
mp.pylab.clf()

X=np.loadtxt("iris2.txt", usecols=(0,1,2,3,4), skiprows=1, delimiter=',')
Y=pdist(X, 'seuclidean')

Z=linkage(Y, 'single')
dendrogram(Z, color_threshold=0)

mp.pylab.draw()
mp.pylab.show()
mp.pylab.clf()

Z=linkage(X, 'centroid')
dendrogram(Z, color_threshold=1.8)

mp.pylab.draw()
mp.pylab.show()
mp.pylab.clf()

mp.pylab.title('Sir Ronald Fisher\'s Iris Data Set')
mp.pylab.xlabel('Flower Specimen Number')
mp.pylab.ylabel('Distance')
mp.pylab.legend(('Iris Setosa', 'Iris Virginica', 'Iris Versicolour'))

Z=linkage(Y, 'complete')
dendrogram(Z, color_threshold=2.3)

mp.pylab.draw()
mp.pylab.show()
mp.pylab.clf()

dendrogram(Z, color_threshold=0, truncate_mode='level', p=3, show_contracted=True, orientation='left')

mp.pylab.draw()
mp.pylab.show()
mp.pylab.clf()