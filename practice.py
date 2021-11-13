import heapq

heap = [4, 5, 1, 2, 12, 9]
max_heap = [(-num, num) for num in heap]
print(max_heap)

heapq.heapify(max_heap)
print(max_heap)
