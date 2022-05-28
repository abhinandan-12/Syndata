import networkx as nx
import matplotlib.pyplot as plt
import json

G=nx.Graph()
g=nx.read_edgelist("edgelist.txt")
G.add_nodes_from(sorted(g.nodes(data=True)))
G.add_edges_from(g.edges(data=True))
pos = nx.nx_pydot.graphviz_layout(G, prog='neato')
nx.draw(G, pos, width=0.2, node_size=8)
pos = {int(k):tuple(float(i) for i in v) for k,v in pos.items()}
new_pos = dict(sorted(pos.items()))
print(new_pos)

with open('embedding.emb', 'w') as f:
    for key in new_pos.keys():
        f.write("%s,%s\n"%(key,new_pos[key]))

json.dump(new_pos, open("positions.pkl",'w'))

plt.draw()
plt.show()