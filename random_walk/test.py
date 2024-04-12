import random
import networkx as nx

def generate_connected_graph(n):
    # Create an empty graph
    G = nx.Graph()

    # Add nodes to the graph
    G.add_nodes_from(range(1, n + 1))

    # Add edges to create a connected graph
    for i in range(1, n):
        # Choose a random node from the already existing nodes
        random_node = random.randint(1, i)
        # Connect the newly added node to a randomly chosen existing node
        G.add_edge(i + 1, random_node)

    # Check if the graph is fully connected
    if nx.is_connected(G):
        return G
    else:
        # If not fully connected, add edges until it's connected
        components = list(nx.connected_components(G))
        while len(components) > 1:
            # Randomly choose nodes from different components
            node1 = random.choice(components[0])
            node2 = random.choice(components[1])
            # Add an edge between them
            G.add_edge(node1, node2)
            # Update connected components
            components = list(nx.connected_components(G))
        return G

# Example usage:
n = 10
random_connected_graph = generate_connected_graph(n)
print("Nodes of the graph:", random_connected_graph.nodes())
print("Edges of the graph:", random_connected_graph.edges())
