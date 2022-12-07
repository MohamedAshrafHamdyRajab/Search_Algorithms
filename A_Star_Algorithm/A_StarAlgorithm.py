# this project is implementation of the A star search algorithm

# the graph information
graph = {
    's' : [('a' , 1) , ('b' , 4)],
    'a' : [('b' , 2) , ('c' , 5) , ('g' , 12)],
    'b' : [('c' , 2)],
    'c' : [('g' , 3)] 
}

# the heuristic table
heuristicTable = {
    's' : 7,
    'a' : 6,
    'b' : 4,
    'c' : 2,
    'g' : 0
}

# function to calculate the full cost of the A star search (nodesDistance + heuristicCost)
def pathFullCost(path) :
    nodesDistance = 0
    for (lastNode , cost) in path :
        # calculate the distance between nodes 
        nodesDistance += cost
        lastNode = path[-1][0]
        # calculate the heuristic value of the last node
        heuristicCost = heuristicTable[lastNode]
        # calculate the full cost of the A star search
        fullCost = nodesDistance + heuristicCost
    return fullCost , lastNode

# function to implement the A star search on the graph 
def AStarSearch(graph , startNode , goal) :
    visitedList = []
    queueList = [[(startNode , 0)]]
    while queueList :
        queueList.sort(key = pathFullCost)
        path = queueList.pop(0)
        lastNode = path[-1][0]
        if lastNode in visitedList :
            continue
        visitedList.append(lastNode)
        if lastNode == goal :
            return path
        else :
            adjacentNodes = graph.get(lastNode , [])
            for (nextNode , cost) in adjacentNodes :
                newPath = path.copy()
                newPath.append((nextNode , cost))
                queueList.append(newPath)

# displaying the results of the A star search
AStar = AStarSearch(graph , 's' , 'g')
print(f'\n the A star search of the graph is : {AStar} \n')
print(f'cost of the A star search is : ', pathFullCost(AStar)[0])