"""
-----------------------------------------
Text evolution - a demonstration of Richard Dawkin's Weasel program.
-----------------------------------------

https://en.wikipedia.org/wiki/Weasel_program

Do you see yonder cloud that's almost in shape of a camel?
By the mass, and 'tis like a camel, indeed.
Methinks it is like a weasel.
"""

import string, random
from tools import Pool
from tools import printIf

class Evolver:
    """
    Evolves a start string to a target string through random mutation.
    Start and target must be of same length (currently).
    """
    
    def __init__(self, base, target, start = None):
        self.base = base

        self.target = target
        self.start  = start

        if start == None:
            self.start = 'a' * len(target)

    def mutate(self, target, limit, prob):

        """
        Copies the letters of a target string, and may mutate each based on given probability

        Arguments:
        target -- string to be mutated
        limit  -- max mutation distance for each letter (in either direction)
        prob   -- probability of mutation for each letter
        """

        result = ''

        for char in target:
            
            randomMut = random.randint(0,1000)
            if randomMut > (prob * 1000):
                result += char
                continue

            movement = random.randint(-limit, limit)
            result += self.base.MoveChar(char, movement)
        
        return result

    def evolve(self, mutations = 10, mLim = 10, mProb = 0.1, genLim = 50000, printing = False):
        """
        Evolves the start string towards the target string
        (mutates working text a given number of times for each generation,
        and chooses the best if better than current)

        Returns number of generations after which target was reached 

        Keyword arguments:
        mutations -- number of mutations per generation
        mLim      -- value passed to limit in mutate()
        mProb     -- value passed to prob in mutate()
        genLim    -- limit on the number of generations
        printing  -- whether each generation is printed to console
        """

        generation = 0
        
        current = self.start
        currentDist =  self.base.TextDistance(current, self.target)
        
        while current != self.target and generation < genLim:
            #mutate
            best = currentDist
            besttext = current

            original = current

            for i in range(mutations):

                mutation = self.mutate(original, mLim, mProb)

                dist = self.base.TextDistance(mutation, self.target)

                if dist < best :
                    best = dist
                    besttext = mutation
                    current = mutation

        
            generation += 1
            currentDist =  self.base.TextDistance(current, self.target)

            printIf(f"Generation {generation}: {current}, distance {currentDist}", printing)
            
        
        print(f"FINISHED, {generation} generations")
        return generation

                


if __name__ == '__main__':

    pool = Pool(string.ascii_letters + ' ')
    evolver = Evolver(pool, 'Methinks it is like a weasel')

    evolver.evolve(printing = True)
    
