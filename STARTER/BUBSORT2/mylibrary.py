import time

def descen(a):
    for c in range (len(a)):
        for j in range (1,len(a)):
            if a[j-1] < a[j]:
                a[j],a[j-1] = a[j-1],a[j]
        
        print("Iterasi ke-",c+1)
        for i in range(len(a)):
            print("%d" %a[i])
        print("----------")

    return a

def main ():
    a = [93,76,1,34,81,41,30,51,96,100]
    print (descen(a))

# if __name__ == "__main__":
#     main()

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))