class Node(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Graph(dict):
    def get_node_at(self, x, y):
        for node in self:
            if node.x == x and node.y == y:
                return node
    def set_neighbours(self):
        pass

graph = Graph()
for x in range(21):
    for y in range(18):
        graph[Node(x,y)] = []

graph.set_neighbours()
mynode = graph.get_node_at(6,6)
print(mynode)
