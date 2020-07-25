import time

class Writer:
    def __init__(self):

        self.filename = f"test{time.time()}.txt"
    
    def write(self, x, y, z):
        with open(self.filename, "a") as file:
            file.write(f"({x}, {y}, {z})\n")
    
    def close(self):
        self.file.close()

class Reader:
    def __init__(self, filename):
        self.filename = filename
    def getdata(self):
        xd,yd,zd = [],[],[]

        with open(self.filename, "r") as file:
            for line in file:
                l = line.strip("()\n")
                x,y,z = (float(i) for i in l.split(","))
                y,z = int(y),int(z)
                
                xd.append(x)
                yd.append(y)
                zd.append(z)

        return xd,yd,zd

if __name__ == '__main__':
    reader = Reader("test1595704038.9444854.txt")
    reader.getdata()