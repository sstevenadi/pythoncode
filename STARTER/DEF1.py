def compare(x,y):
    if x > y :
        return y
    else :
        return x

def compare2(a,b,c):
    return compare(compare(a,b),c)

def main():
    x = int(input("A : "))
    y = int(input("B : "))
    z = int(input("C : "))
    print(compare2(x,y,z))
    
if __name__ == '__main__':
    main()