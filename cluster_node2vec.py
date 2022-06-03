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
loop = int(input("Graph output loop: "))
cluster_choice = int(input("(1) Agglomerative\n(2) Birch\n(3) Bisecting KMeans\n(4) KMeans\n(5) Mini Batch KMeans\n(6) Spectral\nEnter clustering method: "))
output_choice = str(input("Dump graphs to file (y/n): "))
for i in range(0,loop):

    # sort the embedding based on node index in the first column in X
    X=X[X[:,0].argsort()]

    Z=X[0:X.shape[0],1:X.shape[1]] # remove the node index from X and save in Z

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

    nx.draw(G, node_color=labels, font_size=6, cmap=plt.cm.rainbow, width=0.3, with_labels=True, node_size=[d[k]*50 for k in d])
    print("Nodes:\n",nodelist)

    #graph dump
    if cluster_choice == 1:
        plt.savefig("Node2vec/Agglomerative/ag{}.png".format(i))
    elif cluster_choice == 2:
        plt.savefig("Node2vec/Birch/br{}.png".format(i))
    elif cluster_choice == 3:
        plt.savefig("Node2vec/BisectingKMeans/bskm{}.png".format(i))
    elif cluster_choice == 4:
        plt.savefig("Node2vec/KMeans/km{}.png".format(i))
    elif cluster_choice == 5:
        plt.savefig("Node2vec/MiniBatchKMeans/mbkm{}.png".format(i))
    elif cluster_choice == 6:
        plt.savefig("Node2vec/Spectral/spt{}.png".format(i))

    plt.show()
    plt.close()