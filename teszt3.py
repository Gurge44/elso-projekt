


t = [11 , 15 , 25 , 41 , 58 , 3 , 92 , 42]
# t = ["alma" , "barack"]

m = len(t)

for i in range(m):
    
    mi = m * i
    for j in range(0 , m - 1):
        
        if t[j] > t[j + 1]:
            d = t[j]
            t[j] = t[j + 1]
            t[j + 1] = d
            
            
for i in range(len(t)):
    print("%s" %t[i] , end=" ")