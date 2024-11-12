import numpy as np
import matplotlib.pyplot as plt

def find_all_paths(graph, start, end, path=[], distances=[], all_paths=[]):
    path = path + [start]
    if len(distances) == 0:
        distances = [0]  # Initialize distance for the starting node
    
    # If we've reached the end node, save this path and its total distance
    if start == end:
        all_paths.append((path, sum(distances)))
        print(f"Path: {path} | Distance: {sum(distances)}")
        return

    # Explore neighbors recursively
    for neighbor, weight in graph[start].items():
        if neighbor not in path:  # Avoid cycles
            find_all_paths(graph, neighbor, end, path, distances + [weight], all_paths)

def shortest_path_from_all_paths(graph, start, end):
    all_paths = []
    find_all_paths(graph, start, end, all_paths=all_paths)
    
    # Select the path with the minimum distance
    if not all_paths:
        return None, float('inf')
    
    shortest_path, min_distance = min(all_paths, key=lambda x: x[1])
    return shortest_path, min_distance

# Example graph as adjacency list
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Run to find all paths and shortest path
start, end = 'A', 'D'
path, distance = shortest_path_from_all_paths(graph, start, end)

print(f"\nShortest path from {start} to {end} is {path} with distance {distance}")

# Visualization
positions = {'A': (0, 0), 'B': (1, 1), 'C': (1, -1), 'D': (2, 0)}
plt.figure()
for node, pos in positions.items():
    plt.scatter(*pos, label=node, s=100)
    plt.text(pos[0], pos[1], f' {node}', ha='right')

# Plot edges
for node, neighbors in graph.items():
    for neighbor, weight in neighbors.items():
        x_values = [positions[node][0], positions[neighbor][0]]
        y_values = [positions[node][1], positions[neighbor][1]]
        plt.plot(x_values, y_values, 'gray', linestyle='--', alpha=0.5)

# Highlight the shortest path
for i in range(len(path) - 1):
    start, end = path[i], path[i + 1]
    x_values = [positions[start][0], positions[end][0]]
    y_values = [positions[start][1], positions[end][1]]
    plt.plot(x_values, y_values, 'blue')

plt.legend()
plt.title("Graph Representation with Shortest Path")
plt.show()
