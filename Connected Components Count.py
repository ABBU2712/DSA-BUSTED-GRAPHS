#Write a function, connected_components_count, that takes in the adjacency list of an undirected graph. The function should return the number of connected components within the graph.


def connected_components_count(graph):
  visited = set()
  count=0
  for i in graph:
    if explore(graph,i,visited) == True:
      count += 1
  return count
def explore(graph,current,visited):
  if current in visited:
    return False
  visited.add(current)
  for i in graph[current]:
    explore(graph,i,visited)
  return True