using System; 


class Program
{
	public class Edge : IComparable<Edge> { 
		public int src, dest, weight; 

		public int CompareTo(Edge compareEdge) 
		{ 
			return this.weight - compareEdge.weight; 
		} 
	} 
 
	public class subset { 
		public int parent, rank; 
	}; 



	public int find(subset[] subsets, int i) 
	{ 
		 
		if (subsets[i].parent != i) 
			subsets[i].parent 
				= find(subsets, subsets[i].parent); 

		return subsets[i].parent; 
	} 

	public void Union(subset[] subsets, int x, int y) 
	{ 
		int xroot = find(subsets, x); 
		int yroot = find(subsets, y); 

		if (subsets[xroot].rank < subsets[yroot].rank) 
			subsets[xroot].parent = yroot; 
		else if (subsets[xroot].rank > subsets[yroot].rank) 
			subsets[yroot].parent = xroot; 


		else { 
			subsets[yroot].parent = xroot; 
			subsets[xroot].rank++; 
		} 
	} 


	public void Calculate_MST() 
	{ 

		Edge[] result = new Edge[V]; 

		int e = 0; 

		int i = 0; 
		for (i = 0; i < V; ++i) 
			result[i] = new Edge(); 

		Array.Sort(edge); 

		
		subset[] subsets = new subset[V]; 
		for (i = 0; i < V; ++i) 
			subsets[i] = new subset(); 

		for (int v = 0; v < V; ++v) { 
			subsets[v].parent = v; 
			subsets[v].rank = 0; 
		} 
		i = 0; 

		while (e < V - 1) { 

			Edge next_edge = new Edge(); 
			next_edge = edge[i++]; 

			int x = find(subsets, next_edge.src); 
			int y = find(subsets, next_edge.dest);  
	

			if (x != y) { 
				result[e++] = next_edge; 
				Union(subsets, x, y); 
			} 
		} 

		int minimumCost = 0; 
		for (i = 0; i < e; ++i) { 
			minimumCost += result[i].weight; 
		} 

		Console.WriteLine( minimumCost); 
	} 
    int V, E;
	Edge[] edge; 

	public static void Main(String[] args) 
	{ 
        var x = new Program();
        String VE = Console.ReadLine();

		x.V = int.Parse(VE.Split(' ')[0]); 
		x.E = int.Parse(VE.Split(' ')[1]);  


        x.edge = new Edge[x.E]; 
        
        for (int i = 0; i < x.E; ++i) 
            x.edge[i] = new Edge(); 

        for (int i = 0; i < x.E; i++)
        {
            string line = Console.ReadLine();
            var line_arr = line.Split(' ') ;
            x.edge[i].src = int.Parse(line_arr[0])-1; 
            x.edge[i].dest = int.Parse(line_arr[1])-1; 
            x.edge[i].weight = int.Parse(line_arr[2]); 
            
        }

		x.Calculate_MST(); 
	} 

}