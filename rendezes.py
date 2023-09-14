

class Adat:
    def __init__(self , sor):
            resz = sor.split(";")
            self.adat = resz

class Feladat:
    def __init__(self , allomany):
        self.t = []
        with open(allomany , encoding="utf-8") as f:
            for x in f:
                self.t.append(Adat(x))
                
    def Novekvo(self):
        n = self.t
        n.sort()
        print(n)
                
    def Csokkeno(self):
        cs = self.t
        cs.sort(reverse=True)
        print(cs)
        
    def bubble_Sort(self):

        for i in range(5 , 1 , -1):
            
            for j in range(0 , i-1):
                
                if self.adat[j] > self.adat[j + 1]:
                    d = self.adat[j]
                    self.adat[j] = self.adat[j + 1]
                    self.adat[j + 1] = d
                
                
        print(self.adat)
    
        
    
        
        
f = Feladat("ki.txt")


def Kiiras(self):
    valasz = input("Csökkenő vagy növekvő(cs/n):")
    if valasz == "cs":
        f.Csokkeno()
    elif valasz == "n":
        f.Novekvo()
    else:
        print("ERROR")
        
        
Kiiras
        