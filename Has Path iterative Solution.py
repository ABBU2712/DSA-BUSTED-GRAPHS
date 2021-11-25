def haspath(graph,src,des):
    queue=[]
    queue.append(src)
    while queue:
        current=queue.pop(0)
        if current == des:
            return True
        for i in graph[current]:
            graph.append(i)
    return False
