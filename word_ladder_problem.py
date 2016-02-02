
import graph

def buildGraph(wordFile):
    d = {}
    g = graph.Graph()
    wline = open(wordFile, 'r')
    # Create buckets of words that differ by one letter
    for line in wline:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)

    return g

'''
 Implementing Breadth First Search
 '''
import queue
import graph

def bfs(g.start):
    start.setDistance(0)
    start.setPredecessor(None)
    vertQueue = queue.Queue()
    vertQueue.enqueue(start)
    while vertQueue.size() > 0:
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if nbr.getColor() == 'white':
                nbr.setColor('grey')
                nbr.setDistance(nbr.getDistance() + 1)
                nbr.setPredecessor(currentVert)
                vertQueue.enqueue(nbr)
            currentVert.setColor('black')

# traverse

def traverse(y):
    x = y
    while x.getPredecessor():
        print(x.getId())
        x = x.getPredecessor()
    print(x.getId())

