


a = [5, 4, 7, 3, 1]

def bubble_Sort():

    for i in range(5 , 1 , -1):
        
        for j in range(0 , i-1):
            
            if a[j] > a[j + 1]:
                d = a[j]
                a[j] = a[j + 1]
                a[j + 1] = d
                
                
    print(a)
    
bubble_Sort()