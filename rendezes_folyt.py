import subprocess



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
                

        
    def bubble_Sort_inc(self):


        for x in self.t:
            

            m = len(x.adat)
            
            for i in range(m):
                
                for j in range(0 , m - 1):
                    
                    if x.adat[j] > x.adat[j + 1]:
                        d = x.adat[j]
                        x.adat[j] = x.adat[j + 1]
                        x.adat[j + 1] = d
                    
                
            for i in range(len(x.adat)):
                try:
                    k = int(x.adat[i])
                    print("%d"  %k , end=" ")
                except:
                    print("%s"  %x.adat[i] , end=" ")




    def bubble_Sort_dec(self):

            for x in self.t:

                m = len(x.adat)
                
                for i in range(m):
                    
                    for j in range(0 , m - 1):
                        
                        if x.adat[j] < x.adat[j + 1]:
                            d = x.adat[j]
                            x.adat[j] = x.adat[j + 1]
                            x.adat[j + 1] = d
                        
                    
                for i in range(len(x.adat)):
                    try:
                        k = int(x.adat[i])
                        print("%d"  %k , end=" ")
                    except:
                        print("%s"  %x.adat[i] , end=" ")
    

    
    def Shell_Sort_inc(self):
        b = [5, 3, 1]
 
 
        for x in self.t:
            a = x.adat
            n = len(a)
            
            for k in range(0, 3):
                lepes = b[k]
                for j in range(lepes, n):
                    i = j - lepes
                    kulcs = a[j]
                    while i >= 0 and a[i] > kulcs:
                        a[i+lepes] = a[i]
                        i = i - lepes
                    a[i+lepes] = kulcs
            

            try:
                for i in a:
                    i = int(i)
                    print(i , end = " ")
            except:
                for i in a:
                    i = str(i)
                    print(i , end = " ")
                
        
    def Shell_Sort_dec(self):
        b = [5, 3, 1]
 
 
        for x in self.t:
            a = x.adat
            n = len(a)
            
            for k in range(0, 3):
                lepes = b[k]
                for j in range(lepes, n):
                    i = j - lepes
                    kulcs = a[j]
                    while i >= 0 and a[i] < kulcs:
                        a[i+lepes] = a[i]
                        i = i - lepes
                    a[i+lepes] = kulcs
            

            try:
                for i in a:
                    i = int(i)
                    print(i , end = " ")
            except:
                for i in a:
                    i = int(i)
                    print(i , end = " ")
                

        
f = Feladat("ki.txt")


def Kiiras():
    
    valasz_1 = input("Buborék vagy shell rendezés(b/s): ")
    valasz_2 = input("Csökkenő vagy növekvő(cs/n): ")
    
    if valasz_1 == "b" or valasz_1 == "s" and valasz_2 == "cs" or valasz_2 == "n":
        
        if valasz_1 == "b" and valasz_2 == "n":
            f.bubble_Sort_inc()
        elif valasz_1 == "b" and valasz_2 == "cs":
            f.bubble_Sort_dec()
        elif valasz_1 == "s" and valasz_2 == "n":
            f.Shell_Sort_inc()
        elif valasz_1 == "s" and valasz_2 == "cs":
            f.Shell_Sort_dec()
            
            
        new = input("\nÚj hozzáadása(i/n): ")
        if new == "i":
            add = input("Új: ")
            with open("ki.txt" , "a" , encoding = "utf-8") as ff:
                ff.write(";" + add)
            
            subprocess.run(["python" , "rendezes_folyt.py"])

            
        else:
            pass
            
    else:
        print("ERROR")
        
        
Kiiras()