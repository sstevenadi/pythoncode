class Node:

    def __init__ (self, data):
        self.data = data # the data
        self.next = None # next data
        self.prev = None # prev data

class DLL:

    def __init__ (self):
        self.head = None # first data

    def add(self, new): # add from front
        newNode = Node(new) # the new data
        newNode.next = self.head # make the next data as the head ?
        if self.head is not None: # if the first data is not empty
            self.head.prev = newNode # link the new data to the head as the prev
        self.head = newNode # make the data to the first data
    
    def plist(self, head):
        while(head is not None):
            if (head is not None):
                print (head.data, end=" ")
                head = head.next

def main():
    a = DLL()

    a.add(10)
    a.add(13)
    a.add(17)
    a.add(90)
    a.add(30)

    a.plist(a.head)

if __name__ == "__main__":
    main()