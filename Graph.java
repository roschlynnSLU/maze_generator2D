import java.util.ArrayList;

public class Graph{
    private int numNodes;
    ArrayList<ArrayList<Integer>> graph;

    public Graph(int numNodes){
        this.numNodes = numNodes;
        this.graph = new ArrayList<ArrayList<Integer>>();
        for (int i = 0; i < numNodes; i++)
        {
            this.graph.add(new ArrayList<Integer>());
        }
    }

    public void addEdge(int u, int v){
        boolean skip = false;
        for (Integer node: this.graph.get(u)){
            if (node == v){
                skip = true;
            }
        }
        if (!skip){
            this.graph.get(u).add(v);
        }
    }

    public void removeEdge(int u, int v){
        if (this.graph.get(u).contains(v)){
            for (int i = 0; i < this.graph.get(u).size(); i++)
            {
                if (this.graph.get(u).get(i) == v){
                    this.graph.get(u).remove(i);
                }
            }
        }
    }

    public boolean hasEdge(int u, int v){
        return this.graph.get(u).contains(v);
    }

    
}