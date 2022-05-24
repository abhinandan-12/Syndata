import matplotlib.pyplot as plt
import networkx as nx
from sklearn.cluster import KMeans
import numpy as np
from scipy.spatial.distance import cdist

choice=int(input("(1) Use static db or (2) Use random data: "))
if choice==1:
    imported=np.genfromtxt('db_connections.csv', delimiter=",", dtype=int)
elif choice==2:
    imported=np.genfromtxt('connections_generated.csv', delimiter=",", dtype=int)
#extract nodes
nodes=[]
for i in imported:
    for j in i:
        if j not in nodes:
            nodes.append(j)
nodes=sorted(nodes)
print("Nodes: ", nodes)
#plot graph and matrix
g=nx.Graph()
g.add_nodes_from(nodes)
g.add_edges_from(imported)
kmeans = KMeans().fit_predict(imported)
plt1 = plt.figure(1)
nx.draw_random(g, with_labels=False, node_size=20, width=0.3)
xaxis = []
yaxis = []
for x in imported:
    xaxis.append(x[0])
    yaxis.append(x[1])
'''
plt1 = plt.figure(1)
plt.scatter(xaxis, yaxis, s=50, c=kmeans)
plt.draw()
'''
distortions = []
inertias = []
mapping1 = {}
mapping2 = {}
K = range(1, 10)

for k in K:
    # Building and fitting the model
    kmeanModel = KMeans(n_clusters=k).fit(imported)
    kmeanModel.fit(imported)

    distortions.append(sum(np.min(cdist(imported, kmeanModel.cluster_centers_,
                                        'euclidean'), axis=1)) / imported.shape[0])
    inertias.append(kmeanModel.inertia_)

    mapping1[k] = sum(np.min(cdist(imported, kmeanModel.cluster_centers_,
                                   'euclidean'), axis=1)) / imported.shape[0]
    mapping2[k] = kmeanModel.inertia_
#print("Optimal number of clusters", mapping2.index(max(mapping2))+2)
plt2 = plt.figure(2)
plt.plot(K, distortions, 'bx-')
plt.xlabel('Values of K')
plt.ylabel('Distortion')
plt.title('The Elbow Method using Distortion')
plt.show()