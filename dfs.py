
def dfs(graph,state):
    print(state)
    output.add(state)
    for x in graph[state]:
        if x not in output:
            dfs(graph,x)

graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':[],
    'F':['G'],
    'G':[],
    }      
output=set()
dfs(graph,'A')     
