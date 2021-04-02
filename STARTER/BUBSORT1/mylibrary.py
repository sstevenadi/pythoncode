def ascen(a):
    for c in range (len(a)):
        for j in range (1,len(a)):
            if a[j-1] > a[j]:
                a[j],a[j-1] = a[j-1],a[j]               
    return a

a = [13, 12, 21, 14, 16, 10, 9, 3, 8, 5]

ascen(a)