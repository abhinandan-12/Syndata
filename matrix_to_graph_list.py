import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

#import matrix
choice=str(input("Does csv file contain header and index (y/n): "))
mat=pd.read_csv("matrix_generated.csv", header=None)
if choice=='y':
    mat= mat.iloc[1:, 1:]
elif choice=='n':
    pass

#draw graph
g=nx.from_pandas_adjacency(mat)
nx.draw(g, with_labels=True)
plt.draw()
plt.savefig("matrix2graph.png", dpi=600)
plt.show()

#generate
print("Connections:")
for line in nx.generate_edgelist(g, delimiter=',', data=False):
    print(line)
nx.write_edgelist(g, 'connections_exported.csv', delimiter=',', data=False)
