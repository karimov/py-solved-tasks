from stack import Stack
import re

def tagParse(pList):
    index = 0
    result = ""
    for index in range(len(pList)):
        if pList[index] == '<':
            while pList[index] != '>' and index < len(pList):
                result += pList[index]
                index += 1
            else:
                if pList[index] == '>':
                    result += pList[index]
    return result

def tagsCheck(htmldoc):
    otagstack = Stack()
    htmltags = tagParse(htmldoc).split('>')
    htmltags.remove('')
    balanced = True
    pos = 0
    while pos < len(htmltags) and balanced:
        tags = htmltags[pos]
        if tags in "<html<head<title<body<h1":
            otagstack.push(tags)
        if tags in "</html</head</title</body</h1":
            top = otagstack.pop()
            if not matChes(top, tags):
                balanced = False
        pos += 1
    if balanced and otagstack.is_empty():
        return True
    return False

def matChes(top, bottom):
    oList = ["<html", "<head", "<title", "<body", "<h1"]
    cList = ["</html", "</head", "</title", "</body", "</h1"]
    return oList.index(top) == cList.index(bottom)
