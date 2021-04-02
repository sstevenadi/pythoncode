from dll import DLL

def main():
    
    dll = DLL()
    dll.add(1)
    dll.add(2)
    dll.add(3)
    dll.add(6)

    dll.addM(dll.head,4)
    dll.addM(dll.head,5)

    dll.plist(dll.head)

    print ("---------------------")

    dll.delete(2) # delete at index 1
    dll.delete(3) # delete at index 2

    dll.plist(dll.head)

if __name__ == "__main__":
    main()