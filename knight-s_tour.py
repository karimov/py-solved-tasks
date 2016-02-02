
'''
 Building the knight's tour graph
 '''
import graph

def knightGraph(boardSize):
    ktGraph = graph.Graph()
    for row in range(boardSize):
        for col in range(boardSize):
            nodeId = posToNodeId(row, col, boardSize)
            newPositions = genLegalMoves(row, col, boardSize)
            for e in newPositions:
                nid = posToNodeId(e[0], e[1], boardSize)
                ktGraph.addEdge(nodeId, nid)

    return ktGraph

def posToNodeId(row, column, boardSize):
    return (row * boardSize) + column

def genLegalMoves(x, y, boardSize):
    newPositions = []
    moveOffsets = [(-1,-2),(-1,2),(-2,-1),(-2,1),
                    (1,-2),(1,2),(2,-1),(2,1)]

    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX, boardSize) and legalCoord(newY, boardSize):
            newPositions.append((newX, newY))

    return newPositions

def legalCoord(x, boardSize):
    if x >= 0 and x < boardSize:
        return True
    else:
        return False

'''
 Implementing Knight's Tour
 '''

def knightTour(n, path, u, limits):
    u.setColor('grey')
    path.append(u)
    if n < limit:
