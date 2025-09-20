class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

noNodes = "No nodes in the list "   
class Linkedlist:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode
        newNode.prev = current
    
    def prepend(self,data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            return 
        self.head.prev = newNode
        newNode.next = self.head
        self.head = newNode
    
    def display_forward(self):
        if not self.head:
            return print(noNodes)
        
        current = self.head
        while current:
            print(current.data,end=" -> ")
            current = current.next
        print("None")
            
    def display_backward(self):
        if not self.head:
            return print(noNodes)
        
        current = self.head
        while current.next:
            current = current.next
        
        while current:
            print(current.data,end=" -> ")
            current = current.prev
        print("None")

    def insertByIndex(self,value,index):
        newNode = Node(value)
        # if the list is empty
        if not self.head and index == 0:
            self.head = newNode
            return
        
        # 0 meand the head
        if index == 0:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            return 
        
        # carefull with negative index
        if index < 0:
            return print("invalid index")
        
        # find the right index before one step behind
        current = self.head
        count = 0
        while current and count < index -1:
            current = current.next
            count += 1

        # index error or invalid if count not equal index
        if count != index:
            return print("invalid index")
        
        # last point link the newnode with prev with next
        if current.next:
            current.next.prev = newNode
        newNode.next = current.next
        current.next = newNode
        newNode.prev = current
    
    def delete(self,value):
        if not self.head:
            return print(noNodes)
        
        if self.head.data == value:
            if self.head.next:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None
            return

        current = self.head
        while current:
            if current.data == value:
                if current.next:
                    current.next.prev = current.prev
                current.prev.next = current.next
                return
            current = current.next

    def update_node(self,newdata,name):
        current = self.head
        while current:
            if current.data == name:
                current.data = newdata
                return True
            current = current.next
        return False
        
    def search(self,data):
        if not self.head:
            return False
        current = self.head
        while current :
            if current.data == data:
                return True
            current = current.next
        return False

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
    
    def get_length(self):
        if not self.head:
            return 0
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next
        
        return length


    def swap_nodes(self,data1,data2):
        if not self.head :
            return False
        
        node1 = self.head
        node2 = self.head
        while node1 and node1.data != data1:
            node1 = node1.next
        while node2 and node2.data != data2:
            node2 = node2.next
        
        if not node2 or not node1:
            return 
        
        if node1.next:
            node1.next.prev = node2

        if node1.prev:
            node1.prev.next = node2
        else:
            self.head = node2
        
        if node2.next:
            node2.next.prev = node1
        
        if node2.prev:
            node2.prev.next = node1
        else:
            self.head = node1
        
        node1.next, node2.next = node2.next, node1.next
        node1.prev, node2.prev = node2.prev, node1.prev
        
        


        



younes = Linkedlist()
younes.append(10)
younes.append(30)
younes.append(20)
younes.append(50)
younes.append(60)




younes.delete(99)