import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

choice=int(input("(1) Use static db or (2) Use random data: "))
if choice==1:
    imported=np.genfromtxt('db_connections.csv', delimiter=",", dtype=int)
elif choice==2:
    imported=np.genfromtxt('connections_generated.csv', delimiter=",", dtype=int)
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
nx.draw_networkx(g, with_labels=False, node_size=10, width=0.3)
plt.draw()
plt.savefig("list2graph.png", dpi=1200)
plt.show()                                                                                                                                                                                                                                                                                                       
save_choice=str(input("Save with headers and index (y/n): "))
if save_choice=='y':
    mat.to_csv("matrix_exported.csv", header=True, index=True)
elif save_choice=='n':
    mat.to_csv("matrix_exported.csv", header=False, index=False)
