class minHeap():
    def __init__(self,capacity):
        self.capacity = capacity
        self.storage = [0]*capacity
        self.size = 0

    def getParentIndex(self,index):
        return (index-1)//2

    def getRightChildIndex(self,index):
        return 2*index+2
 
    def getLeftChildIndex(self,index):
        return 2*index+1

    def hasParent(self,index):
        return self.getParentIndex(index) >= 0

    def hasLeftChild(self,index):
        return self.getLeftChildIndex(index) < self.size
   
    def hasRightChild(self,index):
        return self.getRightChildIndex(index) < self.size
  
    def parent(self,index):
        return self.storage[self.getParentIndex(index)]
        
    def leftChild(self,index):
        return self.storage[self.getLeftChildIndex(index)]

    def rightChild(self,index):
        return self.storage[self.getRightChildIndex(index)]

    def isFull(self):
        return self.size==self.capacity

    def swap(self,index1,index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp


    def heapifyUp(self,index):
        if (self.hasParent(index)) and self.parent(index)>self.storage[index]:
            self.swap(self.getParentIndex(index),index)
            self.heapifyUp(self.getParentIndex(index))

    def insert(self,data):
        if(self.isFull()):
            raise("Heap is Full")
        self.storage[self.size] = data
        self.size += 1
        self.heapifyUp(self.size-1)



array = [30,10,8,5,20,15]
heap = minHeap(len(array))
for i in array:
    heap.insert(i)

print(heap.storage)



