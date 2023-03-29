class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.graph = {}
        
    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]
    
    def remove_edge(self, u, v):
        if u in self.graph:
            if v in self.graph[u]:
                self.graph[u].remove(v)

    def has_edge(self, u, v):
        result = False
        if u in self.graph:
            if v in self.graph[u]:
                result = True
        return result

class Maze:
    def __init__(self, size):
        self.size = size
        self.nodes = []
        self.graph = Graph(size*size)

        # label the nodes from 0 to (N*N)-1
        for i in range(0, self.size):
            self.nodes.append([])
            for j in range(0, self.size):
                self.nodes[i].append(i*self.size + j)

        # each node in the graph is connected to UP, DOWN, LEFT, RIGHT (if they exist)
        for i in range(0, self.size):
            for j in range(0, self.size):
                node = self.nodes[i][j]
                if i > 0:
                    up = self.nodes[i-1][j]
                    self.graph.add_edge(node, up)
                if i < self.size-1:
                    down = self.nodes[i+1][j]
                    self.graph.add_edge(node, down)
                if j > 0:
                    left = self.nodes[i][j-1]
                    self.graph.add_edge(node, left)
                if j < self.size-1:
                    right = self.nodes[i][j+1]
                    self.graph.add_edge(node, right)
                    
    def print(self):
        result = ''
        for i in range(self.size):
            for j in range(self.size):
                node = self.nodes[i][j]
                # check the floor (bottom wall)
                if i < self.size-1 and self.graph.has_edge(node, self.nodes[i+1][j]):
                    result+='_'
                else:
                    result+=' '

                # check the right wall
                if j < self.size-1 and self.graph.has_edge(node, self.nodes[i][j+1]):
                    result+='|'
                else:
                    result+=' '
            result+='\n'
        print(result)


maze = Maze(5)
maze.print()
print("Welcome to 2D maze")