import random

#Graph class which defines the functions and structures of the graph
class Graph:
    def __init__(self, num_nodes): #Start initialization
        self.num_nodes = num_nodes # Total number of Nodes
        self.graph = {} # Initializing graph as a dictionary
    
    #Dictionary is key value pair (key, value)
        
    def add_edge(self, u, v): # Adding edges (u: starting vertex, v: ending vertex)
        if u in self.graph: #First check if u already exists in the dictionary or not
            self.graph[u].append(v) #append the ending node to the key value pair of the graph start node u
        else: #Next case
            self.graph[u] = [v] #create a new key value pair of the starting node and ending node
    
    def remove_edge(self, u, v): #Remove edges between two nodes (u: starting vertex, v: ending vertex)
        if u in self.graph: #First check if u is a part of the adjacency list or not
            if v in self.graph[u]: # Then check if v is a part of the key value pair that is it is connected to u or not
                self.graph[u].remove(v) #Remove the edge between u and v

    def has_edge(self, u, v): #Check whether edges exist between two nodes
        result = False #By default assume no edge exists between two nodes
        if u in self.graph: #First check if the starting node is present or not in the adjacency list
            if v in self.graph[u]: #Then check if an edge exists between the starting node and the ending node
                result = True #Set result as true if it exists
        return result #return true or false

    def get_spanning_tree(self, start): # Get spanning tree of the graph from the start node
        spanning_tree = Graph(self.num_nodes) #Get total number of nodes of the tree from the self.num_nodes function
        stack = [] #Initialize an empty stack
        visited = [False]*self.num_nodes #Set visited array like you would do in dfs

        visited[start] = True #Set start node as visited true in the visited array
        stack.append(start) #Append the start node to the stack
        while stack: #Keep executing until the stack is empty
            node = stack[len(stack)-1] #Pop the last element of the stack
            unvisited_nodes = [] #Initialize unvisited array
            for next_node in self.graph[node]: #Get all the unvisted nodes from the graph adjacency list from the last popped element of the stack
                if not visited[next_node]: #Check if the node that was connected to the node popped from the stack was visited or not
                    unvisited_nodes.append(next_node) #Append all the unvisited nodes to the unvisited nodes array
            if unvisited_nodes: #If any elements exists in the unvisited array
                next_node = random.choice(unvisited_nodes) #select a random node using random.choice function from the unvisited nodes array
                stack.append(next_node) #append the randomly selected node to the stack
                visited[next_node] = True #Set the randomly selected node as visited true in the visited array
                spanning_tree.add_edge(node, next_node) #Add an edge between the popped node at the start of the function and the randomly selected node
                spanning_tree.add_edge(next_node, node) #Add an edge between the randomly selected node and the popped node at the start of the function
            else: #If no elements in the unvisited nodes
                stack.pop() #Pop the stack

        return spanning_tree #Return spanning tree to the function
    
    def get_solution_maze(self, start_node):
        visited = [False] * self.num_nodes
        ending_node = self.num_nodes - 1
        print(ending_node)
        print(start_node)
        queue = []
        queue.append(start_node)
        visited[start_node] = True
        paths_found = []
        while queue:
            s = queue.pop(0)
            paths_found.append(s)
            if s == ending_node:
                break
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        return paths_found
    
class Maze:
    def __init__(self, size): #Initialize of the maze with the given size
        self.size = size #Setting self.size to size
        self.nodes = [] #Defining an empty nodes array
        self.graph_one = Graph(size*size) #Define the size of the graph as a square instead of a rectangle4
        self.graph_two = Graph(size*size) #Second Graph to store the removed edges

        # label the nodes from 0 to (N*N)-1
        #This function creates a 2D array of nodes for the graph
        for i in range(0, self.size): #Start array loop from 0 to the size of the graph that was defined
            self.nodes.append([]) #Initialize an empty list and append it to the nodes array to create a 2D array
            for j in range(0, self.size): #Inner loop 
                self.nodes[i].append(i*self.size + j) #Appends a new node to the inner loop of the array

        # each node in the graph is connected to UP, DOWN, LEFT, RIGHT (if they exist)
        for i in range(0, self.size): #Outer loop to loop through the first node
            for j in range(0, self.size): #Inner loop to loop through the adjacency nodes
                node = self.nodes[i][j] #Add the self.nodes every node connected to the node to a node variable
                if i > 0: #If the current node is not on the top row, the function adds an edge between the current node and the node directly above it. Similarly, if the current node is not on the bottom row, the function adds an edge between the current node and the node directly below it.
                    up = self.nodes[i-1][j]
                    self.graph_one.add_edge(node, up)
                if i < self.size-1: #If the current node is not on the leftmost column, the function adds an edge between the current node and the node directly to the left. Similarly, if the current node is not on the rightmost column, the function adds an edge between the current node and the node directly to the right.
                    down = self.nodes[i+1][j]
                    self.graph_one.add_edge(node, down)
                if j > 0: #The edges are added to the graph using the self.graph.add_edge() function, which was previously defined.
                    left = self.nodes[i][j-1]
                    self.graph_one.add_edge(node, left)
                if j < self.size-1:
                    right = self.nodes[i][j+1]
                    self.graph_one.add_edge(node, right) #After the function completes execution, the self.graph adjacency list will represent a grid graph of size self.size with edges connecting adjacent nodes.
    
    def generate_maze(self): #Use all above functions to execute and return a new maze
        paths = []
        spanning_tree = self.graph_one.get_spanning_tree(0) #Call the spanning tree function to start from node 0
        for i in range(0, self.graph_one.num_nodes): #Loop through the keys first
            for j in range(0, self.graph_one.num_nodes): #Then loop through the values of the keys first
                if spanning_tree.has_edge(i, j): #Check if an edge exists between the two 
                    self.graph_one.remove_edge(i, j) #Remove that edge if node exists
                    self.graph_two.add_edge(i, j) #Add the removed edges to the second graph
        paths = Graph.get_solution_maze(self.graph_two, 0)
        print("Solution for this maze is: ", paths)
                    
    def print(self): #Print the end result that is the maze
        result = ' '+('_ ' * (self.size-1))+'_\n' #Top Line or the result string which will contain the maze
        for i in range(self.size): #First loop through the keys
            result+='|' #Set as starting result
            for j in range(self.size): #Then loop through the values
                node = self.nodes[i][j]
                # check the floor (bottom wall)
                if i < self.size-1 and self.graph_one.has_edge(node, self.nodes[i+1][j]):
                    result+='_'
                elif (i == self.size-1):
                    result+='_'
                else:
                    result+=' '

                # check the right wall
                if j < self.size-1 and self.graph_one.has_edge(node, self.nodes[i][j+1]):
                    result+='|'
                elif i < self.size-1 and j < self.size-1:
                    result+=' '
                elif i == self.size-1 and j < self.size-1:
                    result+='_'
            result+='|\n'
        print(result)
    
    def printing(self):
        print(self.graph_two)
        print(self.graph_one)

maze = Maze(5)
maze.generate_maze()
maze.print()
#paths = maze.get_solution(0)
#print(paths)
#print(maze.printing())