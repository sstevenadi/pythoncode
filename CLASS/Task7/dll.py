class Node:

    def __init__ (self, data):
        self.data = data # the data
        self.next = None # next data
        self.prev = None # prev data

class DLL:

    def __init__ (self):
        self.head = None # first data

    def revlist (self):
        temp = None
        current = self.head
 
        # the point is this code swap the data
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
 
        # check if the head and tail is just 1
        if temp is not None:
            self.head = temp.prev
    
    def add(self, new): # add from front
        newNode = Node(new) # the new data
        newNode.next = self.head # make the next data as the head ?
        if self.head is not None: # if the first data is not empty
            self.head.prev = newNode # link the new data to the head as the prev
        self.head = newNode # make the data to the first data

    def plist(self, head):
        while(head is not None):
            print (head.data)
            head = head.next

    def addM(self,before,new):
        if before is None:
            print ("There is no data at all")
            return
        newNode = Node(data=new) # the data
        newNode.next = before.next # to link the before data to new data
        before.next = newNode # link the data in before to the new data
        newNode.prev = before # link the new data to data in before
        if newNode.next is not None: # link the new data to the next data
            newNode.next.prev = newNode
    
    def deleteNode(self,head_ref, del_):
 
    # base case 
        if (head_ref == None or del_ == None):
            return
 
    # If node to be deleted is head node 
        if (head_ref == del_):
            head_ref = del_.next
 
    # Change next only if node to be deleted is NOT 
    # the last node 
        if (del_.next != None):
            del_.next.prev = del_.prev
 
    # Change prev only if node to be deleted is NOT 
    # the first node 
        if (del_.prev != None):
            del_.prev.next = del_.next
         
        return head_ref
 
# Function to delete the node at the given position
# in the doubly linked list 
    def delete(self, position):     
        if(position < 1):
            print("\nposition should be >= 1.")
        elif (position == 1 and self.head != None):
            nodeToDelete = self.head
            self.head = self.head.next
            nodeToDelete = None
            if (self.head != None):
                self.head.prev = None
        else:    
            temp = self.head
            for i in range(1, position-1):
                if(temp != None):
                    temp = temp.next   
        if(temp != None and temp.next != None):
            nodeToDelete = temp.next
            temp.next = temp.next.next
            nodeToDelete = None 
        else:
            print("\nThe node is already null.")


# dll = DLL()
# dll.add(2)
# dll.add(4)
# dll.add(8)
# dll.add(10)
# dll.addM(dll.head,11)
# dll.pop_at(3)

# dll.plist(dll.head)

# dll.revlist()

# dll.plist(dll.head)

