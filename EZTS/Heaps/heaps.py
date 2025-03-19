## Implementing Heaps DATA structures.

class Min_heap:
  def __init__(self) -> None:
    self.heap = []

  def parent(self,index):
    return (index - 1)//2


  def left_child(self,index):
    return 2 * (index) +1


  def right_child(self,index):
    return 2 * (index) + 2

  def insert(self,value):
    self.heap.append(value)
    self.heapify_up(len(self.heap)-1)

  def extract_min(self): ## Take the root Element .. and Swap the last ele to root 
    if len(self.heap) == 0:
      return None
    if len(self.heap) == 1:
      return self.heap.pop()
    root = self.heap[0]
    self.heap[0] = self.heap.pop()
    self.heapify_down(0)
    return root


  def heapify_up(self,index):
    parent = self.parent(index)

    while index > 0 and self.heap[index] < self.heap[parent]:
      ## swaping the values
      self.heap[index] , self.heap[parent] = self.heap[parent] , self.heap[index]
      index = parent
      parent = self.parent(index)

  def heapify_down(self, index):
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify_down(smallest)

  def get_min(self):
    return self.heap[0] if self.heap else None

minheap = Min_heap()

minheap.insert(10)
minheap.insert(100)
minheap.insert(1000)
minheap.insert(2)
minheap.insert(120)

print(minheap.extract_min())