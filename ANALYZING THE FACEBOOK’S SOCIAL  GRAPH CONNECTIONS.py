import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

url = "http://snap.stanford.edu/data/facebook_combined.txt.gz"
data = pd.read_csv(url, compression='gzip', sep=' ', names=['n1', 'n2'])

G = nx.from_pandas_edgelist(data, 'n1', 'n2')

print("Nodes:", G.number_of_nodes())
print("Edges:", G.number_of_edges())

plt.figure(figsize=(10, 6))
nx.draw(G, node_size=5, edge_color='gray', with_labels=False)
plt.title("Facebook Social Graph")
plt.show()
