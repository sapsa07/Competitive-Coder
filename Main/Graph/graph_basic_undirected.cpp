// Basic graph Implementation in an undirected graph
#include <bits/stdc++.h>

#define ll long long

using namespace std;

// To add an edge in an undirected graph. 
void addEdge(vector<int> adj[], int u, int v) 
{ 
    adj[u].push_back(v); 
    adj[v].push_back(u); 
} 
  
// To print the adjacency list representation of graph 
void printGraph(vector<int> adj[], int V) 
{ 
    for (int v = 0; v < V; ++v) 
    { 
        cout << "\n Adjacency list of vertex "<< v << "\n head ";

        for (auto x : adj[v]) 
           cout << "-> " << x; 
        cout << endl; 
    } 
} 

int main()
{
    // ...
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int V = 5;
    vector<int> adj[V];

    addEdge(adj, 0, 1); 
    addEdge(adj, 0, 4); 
    addEdge(adj, 1, 2); 
    addEdge(adj, 1, 3); 
    addEdge(adj, 1, 4); 
    addEdge(adj, 2, 3); 
    addEdge(adj, 3, 4); 

    //Print
    printGraph(adj, V);
    
    return 0;
}

// O(|V|+|E|)