# this project is implementation of the breadth first search by reading the graph from text file
# without write the graph on the form of dictionary

# graph = {
# '5': ['3', '7'],
# '3': ['2', '4'],
# '7': ['8'],
# '2': [],
# '4': ['8'],
# '8': []
# }

# declaration of the function
visitedList = [] 
queueList = []
def bfs(visitedList , graph , startNode) :
    visitedList.append(startNode)
    queueList.append(startNode)
    while queueList :
        queueMember = queueList.pop(0)
        print(queueMember , end = "  ")
        for neighbour in graph[queueMember]:
            if neighbour not in visitedList:
                visitedList.append(neighbour)
                queueList.append(neighbour)

# reading the text file
graph = {}
file = open("graphText.txt")
for item in file :
    line = item.strip().split(",")
    arr = []
    for char in range (len(line)) :
        arr.append(line[char])
        graph[line[0]] = arr
print(f"this is graph :  \n {graph} \n")        
file.close()

# displaying the results of the breadth first search
print("the breadth first search of the input graph is :")
bfs(visitedList , graph , '5')