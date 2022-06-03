import sklearn.cluster as sk
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import csv
import json

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
print(Z)

pos = {int(k):tuple(int(i) for i in v) for k,v in json.load(open('positions.pkl')).items()}

g = nx.read_edgelist('edgelist.txt', nodetype=int)
with open("optimal_clusters.txt",'r') as file:
    clusters=int(file.read())
print("Number of clusters= ", clusters)
G = nx.Graph()
G.add_nodes_from(sorted(g.nodes(data=True)))
G.add_edges_from(g.edges(data=True))
print(G.nodes)
nodelist = sorted(nx.nodes(g))
d = dict(G.degree)
loop = int(input("Graph output loop: "))
for i in range(0,loop):
    #cluster = sk.KMeans(n_clusters=clusters).fit(Z)
    #cluster = sk.AgglomerativeClustering(n_clusters=clusters).fit(Z)
    #cluster = sk.MiniBatchKMeans(n_clusters=clusters).fit(Z)
    #cluster = sk.Birch(n_clusters=clusters).fit(Z)
    #cluster = sk.SpectralClustering(n_clusters=clusters).fit(Z)
    cluster = sk.BisectingKMeans(n_clusters=clusters).fit(Z)

    labels=cluster.labels_  # get the cluster labels of the nodes.
    print("Clusters:\n",labels)

    nx.draw(G, pos, node_color=labels, font_size=6, node_size=[d[k]*50 for k in d], cmap=plt.cm.rainbow, width=0.3, with_labels=True)
    #print("Colour maps:\n",color_map)
    print("Nodes:\n",nodelist)
    #comment out next line to skip file output
    #plt.savefig("Graphviz/BisectingKMeans/bskm{}.png".format(i))
    plt.show()
    plt.close()

