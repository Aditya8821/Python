def tower(n,source,destination,auxilliary):
    if n==1:
        print("Move Disk 1 form source",source,"to destination",destination)
    tower(n-1,source,destination,auxilliary)
    print("Move disk ",n,"from source",source,"to destination",destination)
    tower(n-1,auxilliary,destination,source)
n=4
tower(n,"A","B","C")
