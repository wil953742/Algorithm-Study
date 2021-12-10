## Python Modules with JS

created by [wil953742](https://github.com/wil953742), [Nastro](https://github.com/Narastro)

### 1. Deque

Implemented with DLL(Double Linked List) <br/>
It takes O(1) time with push, pushleft, pop, popleft methods

- Define
  <br/>
  `const deque = new Deque()` or <br/>
  `const deque = new Deque([1,2,3,4,5])`

- valuable & method
  - deque.length: Return total length of deque
  - deque.push(value): push value in the list from **right**
  - deque.pushleft(value): push value in the list from **left**
  - deque.pop(): remove value from the right side of the list and return the value
  - deque.popleft(): remove value from the left side of the list and return the value
  - deque.isEmpty(): true when the length is 0, false otherwise
