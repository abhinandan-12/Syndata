from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import networkx as nx
import sklearn.cluster as skc
import numpy as np

choice=int(input("(1) Use static db or (2) Use random data: "))
if choice==1:
    imported=np.genfromtxt('db_connections.csv', delimiter=",", dtype=int)
elif choice==2:
    imported=np.genfromtxt('connections_exported.csv', delimiter=",", dtype=int)
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
kmeans = skc.KMeans().fit_predict(imported)
plt1 = plt.figure(1)
xaxis = []
yaxis = []
for x in imported:
    xaxis.append(x[0])
    yaxis.append(x[1])

sil = []
# Number of clusters in range 2-10
K = range(2, 10) # 2, 3, 4, 5
for n in K:
    algorithm = skc.KMeans(n_clusters = n)
    algorithm.fit(imported)
    labels = algorithm.labels_
    sil.append(silhouette_score(imported, labels, metric = 'euclidean'))
print("Optimal number of clusters", sil.index(max(sil))+2) #loop starts with 2
with open('optimal_clusters.txt', 'w') as file:
    file.write(str(sil.index(max(sil))+2))
plt2 = plt.figure(2)
plt.plot(K, sil, 'bx-')
plt.xlabel('Values of K')
plt.ylabel('Silhoutte')
plt.title('The Silhoutte Method for optimal K')
plt.show()