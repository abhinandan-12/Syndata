from sklearn.cluster import KMeans
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

# sort the embedding based on node index in the first column in X
X=X[X[:,0].argsort()]

Z=X[0:X.shape[0],1:X.shape[1]] # remove the node index from X and save in Z

kmeans = KMeans(n_clusters=clusters).fit(Z) # apply kmeans on Z
labels=kmeans.labels_  # get the cluster labels of the nodes.
print("Clusters:\n",labels)

nx.draw(G, node_color=labels, cmap=plt.cm.prism, width=0.3, with_labels=True)
#print("Colour maps:\n",color_map)
print("Nodes:\n",nodelist)
plt.show()
plt.close()