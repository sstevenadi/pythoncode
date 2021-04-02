import time

def insertsort (a):
    b = len(a)
    temp = 0
    for i in range (1,b):
        temp=a[i]
        j=i-1
        while j>=0 and temp < a[j]:
            a[j+1] = a[j]
            j = j-1
        a[j+1] = temp
        print (a)
    return a

a = [1, 10, 5, 17, 9, 8, 35, 54, 5]
A = [3, 4, 2, 1, 5]

# insertsort(A)

# def main ():
#   a = [93,76,1,34,81,41,30,51,96,100]
#     print (insertsort(A))

# if __name__ == "__main__":
#     main()

start_time = time.time()
insertsort(A)
print("--- %s seconds ---" % (time.time() - start_time))