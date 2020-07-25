class Pool:
    """
    class for handling pool of usable characters
    """
    
    def __init__(self, chars):
        self.chars = chars
    def __iter__(self):
        return self.chars.__iter__()
    def __getitem__(self, key):
        return self.chars.__getitem__(key)


    def GetIndex(self, target):
        if target not in self.chars:
            raise Exception("Invalid Character.")

        return self.chars.index(target)
    
    def GetChar(self, index):

        i = index % len(self.chars)
        return self.chars[i]

    def MoveChar(self, current, direction):
        """
        Get the next base character in some direction
        """

        if current not in self.chars:
            raise Exception("Invalid Current Character.")

        i = self.GetIndex(current)

        return self.GetChar(i + direction)


    def CharDistance01 (self, _from, _to):
        """
        Determines the shortest distance in index between two chars 
        Normalized between 0 (closest) and 1
        """

        iF = self.GetIndex(_from)
        iT = self.GetIndex(_to)

        dist = abs(iF - iT) / len(self.chars)

        #ensure shortest distance
        if dist > 0.5:
            dist = 1 - dist

        return dist

    def TextDistance(self, _from, _to):
        """
        Determines overall distance between two pieces of text
        Calculates normalized distance for each letter
        """

        result = 0

        for i in range(len(_from)):
            
            a = _from[i]
            b = _to[i]

            result += self.CharDistance01(a,b)
            
        return result


def printIf(value, condition, **kwargs):
    if condition:
        print(value, **kwargs)