# synthetic classification dataset
from numpy import unique
from numpy import where
import numpy
from sklearn.datasets import make_classification
from sklearn.cluster import AgglomerativeClustering
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
model = AgglomerativeClustering(n_clusters=2)
# fit model and predict clusters
yhat = model.fit_predict(imported)
# retrieve unique clusters
clusters = unique(yhat)
# create scatter plot for samples from each cluster
for cluster in clusters:
	# get row indexes for samples with this cluster
	row_ix = where(yhat == cluster)
	# create scatter of these samples
	pyplot.scatter(imported[row_ix, 0], imported[row_ix, 1])
# show the plot
pyplot.show()
'''