from collections import deque

# Creating a deque with initial values
dq = deque([1, 2, 3, 4, 5])
print(dq)  # deque([1, 2, 3, 4, 5])

dq = deque([1, 2, 3])
dq.append(4)  # Add to right
dq.appendleft(0)  # Add to left
print(dq)  # deque([0, 1, 2, 3, 4])

dq.pop()  # Removes 4 (from the right)
dq.popleft()  # Removes 0 (from the left)
print(dq)  # deque([1, 2, 3])

from collections import deque  # Import deque for efficient queue operations

def bfs(graph, start):
    """
    Performs Breadth-First Search (BFS) on a graph starting from a given node.

    Parameters:
    - graph: Dictionary representing the adjacency list of the graph.
    - start: The node from which BFS traversal begins.

    Output:
    - Prints nodes in the order they are visited.
    """

    # Initialize a queue with the starting node
    queue = deque([start])  # `deque` provides O(1) time complexity for popping from the left
    visited = set([start])  # Use a set to keep track of visited nodes to avoid cycles

    while queue:  # Continue until the queue is empty
        node = queue.popleft()  # Remove and process the leftmost node (FIFO behavior)
        print(node, end=" ")  # Print the node (order of traversal)

        # Iterate through all the adjacent nodes (neighbors)
        for neighbor in graph[node]:
            if neighbor not in visited:  # If the neighbor hasn't been visited
                queue.append(neighbor)  # Add the neighbor to the queue for future processing
                visited.add(neighbor)  # Mark the neighbor as visited to avoid re-processing

# Example graph represented as an adjacency list (Undirected Tree-like Graph)
graph = {
    1: [2, 3],  # Node 1 is connected to Nodes 2 and 3
    2: [4, 5],  # Node 2 is connected to Nodes 4 and 5
    3: [6, 7],  # Node 3 is connected to Nodes 6 and 7
    4: [],      # Leaf node (No outgoing edges)
    5: [],      # Leaf node (No outgoing edges)
    6: [],      # Leaf node (No outgoing edges)
    7: []       # Leaf node (No outgoing edges)
}

# Call BFS starting from node 1
bfs(graph, 1)
# Expected Output: 1 2 3 4 5 6 7
