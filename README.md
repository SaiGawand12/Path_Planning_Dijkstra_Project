# Shortest Path Finder

This project provides a Python implementation for finding all paths and the shortest path between two nodes in a weighted, undirected graph. The graph is represented as an adjacency list, and the solution finds the shortest path using a brute-force approach that explores all possible paths.

## Features

- **Find all paths**: The program recursively explores all possible paths between two nodes.
- **Find shortest path**: It identifies the shortest path based on the sum of edge weights.
- **Visualization**: The graph and the shortest path are visualized using `matplotlib` to represent the nodes and edges graphically.

## Requirements

Before running the project, you need to have Python installed on your machine. You also need the following libraries:

- `numpy`
- `matplotlib`

### Installing Dependencies

To install the required dependencies, follow these steps:

1. Clone or download the repository:

```bash
git clone https://github.com/SaiGawand12/Path_Planning_Dijkstra_Project.git
cd Path_Planning_Dijkstra_Project
```

2. Install the required Python libraries using `pip`:

```bash
pip install numpy matplotlib
```

## Running the Code

1. **Define the graph**: The graph is represented as an adjacency list, where the keys are node names, and the values are dictionaries with neighboring nodes as keys and edge weights as values. Example graph:

```python
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
```

2. **Modify the starting and ending nodes**: The program allows you to change the start and end nodes for the shortest path calculation. Modify the following lines in the code:

```python
start, end = 'A', 'D'
```

Set `start` and `end` to the desired nodes in your graph.

3. **Run the script**: Once you've set the graph and nodes, you can run the script. In your terminal, navigate to the directory where the script is located, and run:

```bash
python main.py
```

This will output the shortest path and its distance to the console, and also display a graphical representation of the graph with the shortest path highlighted.

Example output in the terminal:

```bash
Shortest path from A to D is ['A', 'B', 'C', 'D'] with distance 4.0
```

### Output

- **Console**: The shortest path and its distance will be printed in the console.
- **Graph**: A graphical visualization of the graph will be displayed with the shortest path highlighted.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request with improvements or fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### How to Run:

1. Clone or download the repository to your local machine.
2. Install dependencies with `pip` as described above.
3. Modify the `start` and `end` variables in the code to choose the nodes for your shortest path calculation.
4. Run the script using `python shortest_path_finder.py`.

This will execute the program, print the result to the console, and show a graph with the shortest path highlighted.

Let me know if you need further details!
