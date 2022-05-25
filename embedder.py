import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph();
G=nx.read_edgelist("edgelist.txt")

nx.draw(G,with_labels = False,node_size=10);

from node2vec import Node2Vec
# Generate walks
node2vec = Node2Vec(G, dimensions=2, walk_length=50, num_walks=10,workers=4)
# Learn embeddings
model = node2vec.fit(window=10, min_count=1)
#model.wv.most_similar('1')
model.wv.save_word2vec_format("embedding.emb")
plt.draw()
plt.show()