class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = node()


    def append(self,data):
        new_node = node(data)
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node

    def length(self):
        curr = self.head
        total = 0
        while curr.next != None:
            total += 1
            curr = curr.next

        return total


    def display(self):
        elem = []
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
            elem.append(curr_node.data)
        print(elem)

    def extract_i(self,index):
        if index>=self.length():
            print("index out of range")
            return None
        cur_pos = 0
        cur_node = self.head
        while True:
            cur_node=cur_node.next
            if cur_pos == index:
                 return cur_node.data
            cur_pos += 1

    def erase(self,index):
        if index>=self.length():
            print("out of Index Rage, Erase")
            return

        curr_pos = 0
        curr_node = self.head
        while True:
            last_node = curr_node
            curr_node = curr_node.next
            if curr_pos==index:
                last_node.next = curr_node.next
                return
            curr_pos += 1

lst = LinkedList()
lst.append(1)
lst.append(2)
lst.append(3)

lst.display()
print("linked list position 2 is %d" %lst.extract_i(2))
lst.erase(1)
lst.display()
