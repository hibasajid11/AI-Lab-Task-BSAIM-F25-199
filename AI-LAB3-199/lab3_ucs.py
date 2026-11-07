# Lab 3: UCS and Search implementation
import heapq

graph_weighted = {
    'A': [('B', 1), ('C', 10)],
    'B': [('E', 1)],
    'C': [('G', 2)],
    'E': [('G', 1)],
    'G': []
}

def uniform_cost_search(start, goal):
    pq = [(0, start, [start])]
    visited = set()
    while pq:
        cost, node, path = heapq.heappop(pq)
        if node == goal:
            return cost, path
        if node in visited:
            continue
        visited.add(node)
        for neighbor, weight in graph_weighted.get(node, []):
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))
                
print("UCS Result:", uniform_cost_search('A', 'G'))