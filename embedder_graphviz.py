import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
g=nx.read_edgelist("edgelist.txt")
G.add_nodes_from(sorted(g.nodes(data=True)))
G.add_edges_from(g.edges(data=True))
pos = nx.nx_pydot.graphviz_layout(G, prog='neato')
nx.draw(G, pos, width=0.2, node_size=8)
with open('embedding.emb', 'w') as f:
    for key in pos.keys():
        f.write("%s,%s\n"%(key,pos[key]))
plt.draw()
plt.show()