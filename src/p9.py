def node_path_existence(start, end):
    graph = {
        'A': ['B'],
        'B': ['A', 'C', 'D', 'E'],
        'C': ['F'],
        'D': ['G', 'E'],
        'E': ['F'],
        'F': ['B', 'G'],
        'G': []
    }

    # If start and end are the same, return immediately
    if start == end:
        return [True, [start]]

    visited = {node: False for node in graph} # Keep track of visited nodes
    previous_node = {node: None for node in graph} # Store previous node to build path
    queue = [start] # Queue for BFS
    visited[start] = True

    while queue:
        current_node = queue.pop(0) # Take first node in queue

        # Stop if we reached the end
        if current_node == end:
            break

        for neighbor in graph[current_node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                previous_node[neighbor] = current_node # Remember how we got here
                queue.append(neighbor) # Add neighbor to queue

    # No path found
    if not visited[end]:
        return [False, []]

    # Reconstruct path from end to start
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous_node[current]
    path.reverse()

    return [True, path]
