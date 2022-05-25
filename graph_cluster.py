from sklearn.cluster import KMeans
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
X = np.loadtxt("embedding.emb", skiprows=1) # load the embedding of the nodes of the graph
g = nx.read_edgelist('edgelist.txt', nodetype=int)
G = nx.Graph()
G.add_nodes_from(sorted(g.nodes(data=True)))
G.add_edges_from(g.edges(data=True))
nodelist = nx.nodes(g)
nodelist = sorted(nodelist)
#print(X)
# sort the embedding based on node index in the first column in X
X=X[X[:,0].argsort()]
#print(X)
Z=X[0:X.shape[0],1:X.shape[1]] # remove the node index from X and save in Z
kmeans = KMeans(n_clusters=4, random_state=0).fit(Z) # apply kmeans on Z
labels=kmeans.labels_  # get the cluster labels of the nodes.
print(labels)
color_map = []
for node in labels:
    if node == 0:
        color_map.append('blue')
    elif node == 1:
        color_map.append('green')
    elif node == 2:
        color_map.append('red')
    elif node == 3:
        color_map.append('yellow')

nx.draw(G, node_color=color_map, width=0.3, with_labels=True)
print(color_map)
plt.show()