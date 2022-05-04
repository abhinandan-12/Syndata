import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

imported=np.genfromtxt('connections.csv', delimiter=",", dtype=str)
nodes=[]
for i in imported:
    for j in i:
        if j not in nodes:
            nodes.append(j)
nodes=sorted(nodes)
print("Nodes: ", nodes)
g=nx.Graph()
g.add_nodes_from(nodes)
g.add_edges_from(imported)
a = nx.to_pandas_adjacency(g, dtype=int)
print("Adjacency Matrix:")
print(a)
g = nx.from_pandas_adjacency(a)
nx.draw(g, with_labels=True)
for line in nx.generate_edgelist(g, data=False):
    test = []
    test.append(line)
    print(line)
'''    
    file2 = open('test.csv', 'a', newline='', delimiter)
    with file2:
        write = csv.writer(file2)
        write.writerows(line)
'''
np.savetxt("test.csv",
           test,
           delimiter=", ",
           fmt='% s')
plt.draw()
plt.savefig("graph.png", dpi=600)
plt.show()