from collections import deque

"""
Write a function, has_path, that takes in a dictionary representing the adjacency list
of a directed acyclic graph and two nodes (src, dst). The function should return a boolean
indicating whether or not there exists a directed path between the source and destination nodes.
"""


# Recursive DFS
def has_path_recursive_dfs(graph, src, dst):
    if src == dst:
        return True

    for n in graph[src]:
        if has_path_recursive_dfs(graph, n, dst) is True:
            return True
    return False


# Iterative DFS
def has_path_iterative_dfs(graph, src, dst):
    stack = [src]
    while stack:
        cur = stack.pop()
        if cur == dst:
            return True
        for n in graph[cur]:
            stack.append(n)
    return False


# Iterative BFS
def has_path_bfs(graph, src, dst) -> bool:
    queue = deque([src])
    while queue:
        cur = queue.popleft()
        if cur == dst:
            return True
        for n in graph[cur]:
            queue.append(n)
    return False


# n = number of nodes
# e = number edges
# Time: O(e)
# Space: O(n)

graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

assert has_path_recursive_dfs(graph, 'f', 'k') is True
