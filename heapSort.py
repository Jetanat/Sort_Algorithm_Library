import numpy as np 

# This function return an index of the index_i's parent
def parent(index_i):
    return np.int64(np.floor((index_i - 1)*0.5))

# This function return an index of the index_i's left child
def left(index_i):
    return np.int64(index_i * 2 + 1)
 
# This function return an index of the index_i's right child
def right(index_i):
    return np.int64(index_i * 2 + 2)

# This function is a comparing function
def comp_bool(a,b):
    if a > b:
        return True
    else:
        return False


# This function return a right condition of Max Heap starting from index_i down to its leaves
def maxHeapify(heap, index_i, func = comp_bool):
    # count 0 as a one
    heap_size = len(heap)

    l = left(index_i)
    r = right(index_i)
    
    if l <= (heap_size - 1) and comp_bool(heap[l], heap[index_i]):
        largest = l
    else:
        largest = index_i
    
    if r <= (heap_size - 1) and comp_bool(heap[r], heap[largest]):
        largest = r
    
    if largest != index_i:
        swap = heap[index_i]
        heap[index_i] = heap[largest]
        heap[largest] = swap
        maxHeapify(heap, largest)

# This function build a heap
def buildMaxHeap(heap, heap_size):

    max_rng = np.int64(np.floor(heap_size/2))
    min_rng = 0
    for index_i in range(max_rng, min_rng-1, -1):
        maxHeapify(heap, index_i)

# This function build a heapsort
def heapSort(array, array_size):
    buildMaxHeap(array, array_size)
    for index_i in range(array_size-1, 0, -1):
        swap = array[0]
        array[0] = array[index_i]
        array[index_i] = swap

        array_size = array_size - 1
        maxHeapify(array[0:array_size], 0)


heap = np.arange(150)
np.random.shuffle(heap)
print(heap)
print('=='*15)
heapSort(heap, len(heap))
print(heap)
