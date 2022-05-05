import networkx as nx

nodes = int(input("Enter number of nodes: "))
edges = int(input("Enter number of edges: "))
G = nx.dense_gnm_random_graph(nodes, edges)
mat=nx.to_pandas_adjacency(G, dtype=int)
print(mat)

choice=str(input("Save header and index (y/n): "))
if choice=="y":
    mat.to_csv('matrix_generated.csv', header=True, index=True)
elif choice=="n":
    mat.to_csv('matrix_generated.csv', header=False, index=False)
