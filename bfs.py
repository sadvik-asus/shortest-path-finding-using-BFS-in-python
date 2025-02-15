from collections import deque

def bfs(graph, start):
    # Create a queue to hold nodes to visit
    queue = deque([start])
    # Set to keep track of visited nodes to avoid revisiting them
    visited = set([start])
    
    print(f"Starting BFS from node: {start}")
    
    # Continue until the queue is empty
    while queue:
        # Pop the first node from the queue
        vertex = queue.popleft()
        print(f"Visiting node: {vertex}")
        
        # Process all adjacent nodes
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                # Mark the neighbor as visited and add it to the queue
                visited.add(neighbor)
                queue.append(neighbor)
                print(f"Queueing {neighbor}")

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Call the bfs function with the graph and starting node
bfs(graph, 'A')