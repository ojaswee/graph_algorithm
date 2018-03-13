'''
We can do BFS/DFS 2 ways via adjacency list or vertices matrix
Here I am trying to solve DFS via vertices matrix.
'''
graphx =[[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0],
        [0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0],
        [0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

def dfs_adjacency_mat(G, start, goal,count):
    visited=[False]*len(G[0])
    stack=[]
    stack.append(start)
    goal = goal -1
    while len(stack)!=0:
        v=stack.pop()
        if visited[v]==False:
            visited[v]=True
            count +=1
            print(v+1),
            for w in range(len(G[0])):
                if G[v][w]!=0:
                    stack.append(w)
                elif v == goal:
                    # print(v)
                    while len(stack)!=0:
                        stack.pop()
                    return count 
                    break
    return count

# def bfs_adjacency_mat(G, start, goal,count):
#     print G

#Entry point for program execution
count = dfs_adjacency_mat(graphx, 0, 10,0)
print " "
print "Total nodes visited:",count