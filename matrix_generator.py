import networkx as nx

def header_save(name):
    choice = str(input("Save header and index (y/n): "))
    if choice == "y":
        mat.to_csv(str(name), header=True, index=True)
    elif choice == "n":
        mat.to_csv(str(name), header=False, index=False)

nodes = int(input("Enter number of nodes: "))
edges = int(input("Enter number of edges: "))
G = nx.dense_gnm_random_graph(nodes, edges)
mat=nx.to_pandas_adjacency(G, dtype=int)
print(mat)

choice1=int(input("(1) Generate random or (2) Dump to static db : "))
if choice1==1:
    header_save('matrix_generated.csv')
elif choice1==2:
    header_save('db_matrix.csv')

