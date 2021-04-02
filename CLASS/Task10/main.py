class Node:
    
    def __init__(self, data=None):
        self.data = data # current data
        self.next = None # next data

class SLL:
    
    def __init__(self):
        self.head = None # first data / current data
    
    def insert(self,new):
        newNode = Node(new) # new data
        if self.head is None : # if the list is empty add the data as the head
            self.head = newNode
            return
        last = self.head
        while(last.next): # to put the data at the end of the list
            last = last.next
        last.next = newNode # new data become the last

    def listp(self):
        printdata = self.head
        while printdata is not None:
            print (printdata.data) # print current data
            printdata = printdata.next # change current data to next data

    def sum(self):
        temp = self.head
        sum1 = 0
        while temp:
            sum1 = sum1+temp.data
            temp = temp.next
        print ('Total',sum1)

def main():
    a = SLL()
    a.insert(2)
    a.insert(2)
    a.insert(2)
    a.insert(2)
    a.sum()
    a.listp()

if __name__ == "__main__":
    main()