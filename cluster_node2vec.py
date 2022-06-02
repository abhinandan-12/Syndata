import sklearn.cluster as sk
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

X = np.loadtxt("embedding.emb", skiprows=1) # load the embedding of the nodes of the graph
g = nx.read_edgelist('edgelist.txt', nodetype=int)
with open("optimal_clusters.txt",'r') as file:
    clusters=int(file.read())
print("Number of clusters= ", clusters)
G = nx.Graph()
G.add_nodes_from(sorted(g.nodes(data=True)))
G.add_edges_from(g.edges(data=True))
nodelist = sorted(nx.nodes(g))
d=dict(G.degree)

# sort the embedding based on node index in the first column in X
X=X[X[:,0].argsort()]

Z=X[0:X.shape[0],1:X.shape[1]] # remove the node index from X and save in Z

cluster = sk.KMeans(n_clusters=clusters).fit(Z)
#cluster = sk.AgglomerativeClustering(n_clusters=clusters).fit(Z)
#cluster = sk.MiniBatchKMeans(n_clusters=clusters).fit(Z)
#cluster = sk.Birch(n_clusters=clusters).fit(Z)
#cluster = sk.SpectralClustering(n_clusters=clusters).fit(Z)
#cluster = sk.BisectingKMeans(n_clusters=clusters).fit(Z)

labels=cluster.labels_  # get the cluster labels of the nodes.
print("Clusters:\n",labels)

nx.draw(G, node_color=labels, font_size=6, cmap=plt.cm.rainbow, width=0.3, with_labels=True, node_size=[d[k]*50 for k in d])
#print("Colour maps:\n",color_map)
print("Nodes:\n",nodelist)
plt.show()
plt.close()