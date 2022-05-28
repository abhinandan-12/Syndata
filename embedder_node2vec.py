import networkx as nx
import matplotlib.pyplot as plt
from node2vec import Node2Vec

G=nx.Graph()
g=nx.read_edgelist("edgelist.txt")
G.add_nodes_from(sorted(g.nodes(data=True)))
G.add_edges_from(g.edges(data=True))
nx.draw(G,with_labels = False,node_size=10)
# Generate walks
node2vec = Node2Vec(G, dimensions=2, walk_length=100, num_walks=200, workers=4)
# Learn embeddings
model = node2vec.fit(window=10, min_count=1, batch_words=4)
model.wv.save_word2vec_format("embedding.emb")
print("Done")
