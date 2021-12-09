from collections import defaultdict


class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def topological_sort(self):
        indegree = [0]*self.V
        for i in self.graph:
            for j in self.graph[i]:
                indegree[j] +=1
        
        queue = []
        for i in range(self.V):
            if indegree[i]==0:
                queue.append(i)

        count =0
        top_order =[]
        while queue:
            u=queue.pop(0)
            top_order.append(u)
            for i in self.graph[u]:
                indegree[i]-=1
                if indegree[i]==0:
                    queue.append(i)
            count +=1 

        if count != self.V:
            print("There is a cycle")

        else:
            print(top_order)


g = Graph(7)
g.addEdge(2, 5)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
g.addEdge(0, 2)
print ("Following is a Topological Sort of the given graph")
g.topological_sort()


