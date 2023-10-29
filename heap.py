
    
class HeapMin:
    def __init__(self):
        self.heap = []

    def push(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)

        return root

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        smallest = index

        if (left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]):
            smallest = left_child

        if (right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]):
            smallest = right_child

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)
heap = HeapMin()
heap.push(4)
heap.push(10)
heap.push(3)
heap.push(5)
heap.push(1)
print("힙에서 팝된 값:", heap.pop())
# 가장 작은 값인 1이 출력됩니다.

class HeapMax:
    def __init__(self):
        self.heap = []

    def push(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) -1)

    def pop(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_up(0)

        return root

    def _heapify_up(self, index):
        parent = (index -1) // 2
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        largest = index

        if (left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]):
            largest = left_child

        if (right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]):
            largest = right_child

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

heap_max = HeapMax()
heap_max.push(4)
heap_max.push(10)
heap_max.push(3)
heap_max.push(5)
heap_max.push(1)
heap_max.push(23)
heap_max.push(-3)
print("힙에서 팝된 값:", heap_max.pop())