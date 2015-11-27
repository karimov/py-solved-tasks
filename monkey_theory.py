import random
import time

def generator(strlen):
    res = ''
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    for i in range(strlen):
        res += alphabet[random.randrange(len(alphabet))]
    return res

def score(goal,randomstr):
    numSum = 0
    for i in range(len(goal)):
        if goal[i] == randomstr[i]:
            numSum += 1
    return float(numSum) / float(len(goal))

def print_out(goal):
    best = 0
    newscore = score(goal, generator(len(goal)))
    newstr = generator(len(goal))
    while newscore < 1:
        if newscore > best:
            best = newscore
            print newscore, newstr
        newstr = generator(len(goal))
        newscore = score(goal, newstr)
     #   print newscore, newstr
