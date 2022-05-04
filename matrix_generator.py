import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

nodes = int(input("Enter number of nodes: "))
edges = int(input("Enter number of edges: "))
G = nx.dense_gnm_random_graph(nodes, edges)
mat=nx.to_pandas_adjacency(G, dtype=int)
print(mat)
A = nx.to_numpy_array(G, dtype=int)

nx.draw(G, with_labels=True)
plt.draw()
plt.show()
choice=str(input("Save header and index (y/n): "))
if choice=="y":
    mat.to_csv('matrix.csv')
elif choice=="n":
    mat.to_csv('matrix.csv', header=False, index=False)
