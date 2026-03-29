import requests
import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations

# Sample users (you can change these)
sample_users = ["FluffyPal0", "HeyFang", "VipRascal", "MatchTheMatrix", "HypeStratex"]

# Headers (no token needed for public data)
headers = {
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "InterestGraph"
}

def get_starred_repos(username):
    url = f"https://api.github.com/users/{username}/starred?per_page=100"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return [repo["full_name"] for repo in response.json()]
    else:
        print(f"Error for {username}: {response.status_code}")
        return []

# Fetch data
user_repos = {user: get_starred_repos(user) for user in sample_users}

# Create graph
G = nx.Graph()

# Add nodes
for user in user_repos:
    G.add_node(user)

# Add edges based on common starred repos
edge_labels = {}

for user1, user2 in combinations(user_repos.keys(), 2):
    common = set(user_repos[user1]) & set(user_repos[user2])

    if common:
        G.add_edge(user1, user2)
        edge_labels[(user1, user2)] = "\n".join(list(common)[:2])

# Draw graph
plt.figure(figsize=(10, 7))
pos = nx.spring_layout(G, k=1)

nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

plt.title("GitHub Interest Graph")
plt.show()
