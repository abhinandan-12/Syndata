import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

def header_import(name):
    global mat
    choice = str(input("Does csv file contain header and index (y/n): "))
    mat = pd.read_csv(str(name), header=None)
    if choice == 'y':
        mat = mat.iloc[1:, 1:]
    elif choice == 'n':
        pass

choice1=int(input("(1) Use static db or (2) Use random matrix: "))
if choice1==1:
    header_import('db_matrix.csv')
elif choice1==2:
    header_import('matrix_generated.csv')

#draw graph
g=nx.from_pandas_adjacency(mat)
nx.draw_random(g, with_labels=False, node_size=10, width=0.3)
plt.draw()
plt.savefig("matrix2graph.png", dpi=600)
plt.show()

#generate
print("Connections:")
for line in nx.generate_edgelist(g, delimiter=',', data=False):
    print(line)
nx.write_edgelist(g, 'connections_exported.csv', delimiter=',', data=False)
nx.write_edgelist(g, 'edgelist.txt')
