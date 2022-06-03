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

pos = {int(k):tuple(int(i) for i in v) for k,v in json.load(open('positions.pkl')).items()}

g = nx.read_edgelist('edgelist.txt', nodetype=int)
with open("optimal_clusters.txt",'r') as file:
    clusters=int(file.read())
print("Number of clusters= ", clusters)
G = nx.Graph()
G.add_nodes_from(sorted(g.nodes(data=True)))
G.add_edges_from(g.edges(data=True))
nodelist = sorted(nx.nodes(g))
d = dict(G.degree)
loop = int(input("Graph output loop: "))
cluster_choice = int(input("(1) Agglomerative\n(2) Birch\n(3) Bisecting KMeans\n(4) KMeans\n(5) Mini Batch KMeans\n(6) Spectral\nEnter clustering method: "))
for i in range(0,loop):
    if cluster_choice == 1:
        cluster = sk.AgglomerativeClustering(n_clusters=clusters).fit(Z)
    elif cluster_choice == 2:
        cluster = sk.Birch(n_clusters=clusters).fit(Z)
    elif cluster_choice == 3:
        cluster = sk.BisectingKMeans(n_clusters=clusters).fit(Z)
    elif cluster_choice == 4:
        cluster = sk.KMeans(n_clusters=clusters).fit(Z)
    elif cluster_choice == 5:
        cluster = sk.MiniBatchKMeans(n_clusters=clusters).fit(Z)
    elif cluster_choice == 6:
        cluster = sk.SpectralClustering(n_clusters=clusters).fit(Z)
    else:
        print("Wrong option! Run again")


    labels=cluster.labels_  # get the cluster labels of the nodes.
    print("Clusters:\n",labels)

    nx.draw(G, pos, node_color=labels, font_size=6, node_size=[d[k]*50 for k in d], cmap=plt.cm.rainbow, width=0.3, with_labels=True)
    print("Nodes:\n",nodelist)

    # graph dump
    if cluster_choice == 1:
        plt.savefig("Graphviz/Agglomerative/ag{}.png".format(i))
    elif cluster_choice == 2:
        plt.savefig("Graphviz/Birch/br{}.png".format(i))
    elif cluster_choice == 3:
        plt.savefig("Graphviz/BisectingKMeans/bskm{}.png".format(i))
    elif cluster_choice == 4:
        plt.savefig("Graphviz/KMeans/km{}.png".format(i))
    elif cluster_choice == 5:
        plt.savefig("Graphviz/MiniBatchKMeans/mbkm{}.png".format(i))
    elif cluster_choice == 6:
        plt.savefig("Graphviz/Spectral/spt{}.png".format(i))

    plt.show()
    plt.close()

