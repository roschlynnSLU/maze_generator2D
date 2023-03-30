public class Maze{
    private int size;
    private int[][] nodes;
    private Graph graph; // represents the walls
    private Graph spanningTree; // represents the paths between nodes

    public Maze(int size){
        this.size = size;
        this.nodes = new int[size][];
        // label nodes from 0 to N*N-1
        for (int i = 0; i < size; i++){
            this.nodes[i] = new int[size];
            for (int j = 0; j < size; j++){
                this.nodes[i][j] = i * size + j;
            }
        }
        // create a graph object with each node connected to UP, DOWN, LEFT, RIGHT (if they exist)
        this.graph = new Graph(size*size);
        for (int i = 0; i < size; i++){
            for (int j = 0; j < size; j++){
                int node = this.nodes[i][j];
                if (i > 0){
                    int up = this.nodes[i-1][j];
                    this.graph.addEdge(node, up);
                }
                if (i < size-1){
                    int down = this.nodes[i+1][j];
                    this.graph.addEdge(node, down);
                }
                if (j > 0){
                    int left = this.nodes[i][j-1];
                    this.graph.addEdge(node, left);
                }
                if (j < size-1){
                    int right = this.nodes[i][j+1];
                    this.graph.addEdge(node, right);
                }
            }
        }
    }

    public void generateMaze(){
        this.spanningTree = graph.getSpanningTree(0, this.size*this.size-1);
        // remove edges that are in the spanningTree from graph
        for (int i = 0; i < this.graph.getNumNodes(); i++){
            for (int j = 0; j < this.graph.getNumNodes(); j++){
                if (this.spanningTree.hasEdge(i,j)){
                    this.graph.removeEdge(i,j);
                }
            }
        }
    }

    public void print(){
        String result = " "+"__".repeat(this.size-1)+"_";
        result+='\n';
        
        for (int i = 0; i < this.size; i++){
            result+="|";
            for (int j = 0; j < this.size; j++){
                int node = this.nodes[i][j];
                // check the floor
                if (i < this.size-1 && this.graph.hasEdge(node, this.nodes[i+1][j])){
                    result+="_";
                }
                else if (i == this.size-1){
                    result+="_";
                }
                else{
                    result+=" ";
                }
                // check the right wall
                if (j < this.size-1 && this.graph.hasEdge(node, this.nodes[i][j+1])){
                    result+="|";
                }
                else if (j < this.size-1 && i < this.size-1){
                    result+=" ";
                }
                else if (i == this.size-1 && j < this.size-1){
                    result+="_";
                }
            }
            result+="|\n";
        }
        System.out.println(result);
    }
    public static void main(String[] args){
        System.out.println("Welcome to 2D Maze");
        Maze maze = new Maze(30);
        maze.generateMaze();
        maze.print();
    }
}