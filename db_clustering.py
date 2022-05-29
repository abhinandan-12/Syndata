from numpy import unique
from numpy import where
import numpy
from sklearn.datasets import make_classification
#from sklearn.cluster import AgglomerativeClustering
import sklearn.cluster as skc
from matplotlib import pyplot
# define dataset
#X, y = make_classification(n_samples=1000, n_features=2, n_informative=2, n_redundant=0, n_clusters_per_class=1, random_state=4)
imported=numpy.genfromtxt('db_connections.csv', delimiter=",", dtype=int)
#extract nodes
nodes=[]
for i in imported:
    for j in i:
        if j not in nodes:
            nodes.append(j)
nodes=sorted(nodes)
print("Nodes: ", nodes)
#visualising data on a scatter plot
listx = []
listy = []
for k in imported:
    listx.append(k[0])
    listy.append(k[1])
#pyplot.scatter(listx, listy)
#pyplot.show()

#CLUSTERINGS
#model = skc.AgglomerativeClustering(n_clusters=2)
#model = skc.Birch(threshold=0.01, n_clusters=2)
#model = skc.DBSCAN(eps=0.30, min_samples=9)
#model = skc.KMeans(n_clusters=2)
#model = skc.MiniBatchKMeans(n_clusters=2)
#model = skc.MeanShift()
model = skc.OPTICS(eps=0.8, min_samples=10)
#model = skc.SpectralClustering(n_clusters=2)


yhat = model.fit_predict(imported)

clusters = unique(yhat)

for cluster in clusters:
	row_ix = where(yhat == cluster)
	pyplot.scatter(imported[row_ix, 0], imported[row_ix, 1])

pyplot.show()
