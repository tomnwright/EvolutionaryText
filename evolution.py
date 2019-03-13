chars = 'abcdefghijklmnopqrstuvwxyz '
import random
test = 'Methinks it is a weasel'

def dist(a,b):
    n =  abs(chars.index(b)-chars.index(a))
    if n<=13:
        return n
    else:
        return 27-n
def t_dist(current, target):
    n = 0
    for e,i in enumerate(current):
        n += dist(i, target[e])
    return n

def mutate(c,lim):
    n = ""
    for i in c:
        index = (chars.index(i) + random.randint(lim*-1,lim))% 27
        n += chars[index]
    return n

def evolve(target,start=None):
    #input validation
    if not start:
        start = 'a' * len(target)
    if len(target) != len(start):
        raise Exception('[length] target != start')
    target, start = target.lower(), start.lower()

    c = start
    e= 0
    while c != target:
        e+=1
        best = mutate(c,5)
        best_d = t_dist(best,target)
        for i in range(500):
            n = mutate(c,1)
            n_d = t_dist(n,target)
            if n_d < best_d:
                best, best_d = n, n_d
        print('%s: %s' % (e,best)); c= best
        
evolve(test)
