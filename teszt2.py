

a = [ 5, 3, 6, 2, 1, 9 ]
b = [5, 3, 1]
 
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
 
print(a)