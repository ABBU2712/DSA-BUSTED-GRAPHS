#Write a function, undirected_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). The function should return a boolean indicating whether or not there exists a path between node_A and node_B.

def undirected_path(edges, node_A, node_B):
  graph = buildgraph(edges)
  return haspath(graph, node_A, node_B, set())
def haspath(graph,src,des,visited):
  if src == des:
    return True
  if src in visited:
    return False
  visited.add(src)
  for i in graph[src]:
    if haspath(graph,i,des,visited) == True:
      return True
  return False    
def buildgraph(edges):
  graph = {}
  for edge in edges:
    a,b=edge
    if a not in graph:
      graph[a]=[]
    if b not in graph:
      graph[b]=[]
    graph[a].append(b)
    graph[b].append(a)
  return graph
      
    