class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.graph = {}
        
class Maze:
    def __init__(self, size):
        self.size = size
        self.nodes = []
        self.graph = Graph(size*size)

maze = Maze(5)
print("Welcome to 2D maze")