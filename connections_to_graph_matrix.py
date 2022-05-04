import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

imported=np.genfromtxt('connections_generated.csv', delimiter=",", dtype=str)
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
mat=nx.to_pandas_adjacency(g, dtype=int)
print("Adjacency Matrix:")
print(mat)
mat.to_csv("matrix_exported.csv", header=True, index=True)
nx.draw(g, with_labels=True)
plt.draw()
plt.savefig("list2graph.png", dpi=600)
plt.show()                                                                                                                                                                                                                                                                                                       

