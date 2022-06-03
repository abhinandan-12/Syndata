import matplotlib.pyplot as plt
import networkx as nx
from sklearn.cluster import KMeans
import numpy as np
from yellowbrick.cluster import KElbowVisualizer

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
plt1 = plt.figure(1)
nx.draw_random(g, with_labels=False, node_size=20, width=0.3)
xaxis = []
yaxis = []
for x in imported:
    xaxis.append(x[0])
    yaxis.append(x[1])

visualizer = KElbowVisualizer(KMeans(), k=(2,10))

visualizer.fit(imported)
visualizer.show()
elbowval = visualizer.elbow_value_
print("Optimal number of Clusters:", elbowval)
with open('optimal_clusters.txt', 'w') as file:
    file.write(str(elbowval))