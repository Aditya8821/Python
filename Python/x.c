struct Graph{
    int V;
    int E;
    int **Adj;
};
struct Graph *Adjmatrixofgraph(){
    int i,u,v;
    struct Graph *G=(struct node*)malloc(sizeof(struct Graph));
    if(!G){
        printf("\nMemory Error");
        return;
    }
    scanf("Number of Vertices: %d, Number of Edges: %d",&G->V,&G->E);
    G->Adj=malloc(sizeof(int)*(G->V*G->V));
    for(u=0;u<G->V;u++){
        for(v=0;v<G->V;v++){
            G->Adj[u][v]=0;
        }
    }
    for(i=0;i<G->E;i++){
        scanf("Connecting nodes: %d %d",&u,&v);
        G->Adj[u][v]=1;
        G->Adj[v][u]=1;
    }
    return G;
}