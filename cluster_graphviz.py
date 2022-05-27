from sklearn.cluster import KMeans
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import csv

coords=[]
positions=[]
with open('embedding.emb', 'r') as file:
    reader=csv.reader(file, delimiter=",")
    for row in reader:
        for i in row:
            a=i.replace("(", "").replace(")", "")
            coords.append(float(a))
        coords.pop(0)
        positions.append(coords)
        coords=[]

Z=np.array(positions)

g = nx.read_edgelist('edgelist.txt', nodetype=int)
with open("optimal_clusters.txt",'r') as file:
    clusters=int(file.read())
print("Number of clusters= ", clusters)
G = nx.Graph()
G.add_nodes_from(sorted(g.nodes(data=True)))
G.add_edges_from(g.edges(data=True))
nodelist = sorted(nx.nodes(g))

kmeans = KMeans(n_clusters=clusters).fit(Z) # apply kmeans on Z
labels=kmeans.labels_  # get the cluster labels of the nodes.
print("Clusters:\n",labels)

nx.draw(G, node_color=labels, cmap=plt.cm.prism, width=0.3, with_labels=True)
#print("Colour maps:\n",color_map)
print("Nodes:\n",nodelist)
plt.show()
plt.close()

