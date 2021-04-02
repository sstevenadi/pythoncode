def o1(a,b):
    return a+b

def o2(a,b):
    return a-b

def o3(a,b):
    return a*b

def o4(a,b):
    return float(a/b)

def main():
    a = int(input("A : "))
    b = int(input("B : "))
    print(o1(a,b))
    print(o2(a,b))
    print(o3(a,b))
    print(o4(a,b))

if __name__ == "__main__":
    main()