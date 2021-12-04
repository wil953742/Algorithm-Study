import heapq

heap = [ 3, 5, 12, 45, 2, 6, 22, 13]

heapq.heapify(heap)
print(heap)

heapq.heappush(heap, 1)
print(heap)

top = heapq.heappop(heap)
print(top)
print(heap)