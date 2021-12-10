const Deque = require("./Deque");

const deque = new Deque();

deque.push(1);
deque.push(2);
deque.push(3);
deque.push(4);
console.log("len : ", deque.length);
deque.push(5);
deque.push(6);
console.log(deque.pop());
console.log(deque.pop());
console.log(deque.pop());
console.log(deque.pop());
console.log("len : ", deque.length);
console.log(deque.pop());
console.log(deque.pop());
console.log(deque.pop());

console.log("-------------------");

deque.push(1);
deque.push(2);
deque.push(3);
deque.pushleft(4);
console.log("len : ", deque.length);
deque.pushleft(5);
deque.pushleft(6);
console.log(deque.pop());
console.log(deque.pop());
console.log(deque.pop());
console.log(deque.pop());
console.log("len : ", deque.length);
console.log(deque.pop());
console.log(deque.pop());
console.log(deque.pop());

console.log("-------------------");

deque.push(1);
deque.push(2);
deque.push(3);
deque.pushleft(4);
console.log("len : ", deque.length);
deque.pushleft(5);
deque.pushleft(6);
console.log(deque.popleft());
console.log(deque.popleft());
console.log(deque.popleft());
console.log(deque.popleft());
console.log("len : ", deque.length);
console.log(deque.popleft());
console.log(deque.popleft());
console.log(deque.popleft());

console.log("-------------------");

const deque2 = new Deque([1, 2, 3]);
deque2.pushleft(4);
console.log("len : ", deque2.length);
deque2.pushleft(5);
deque2.pushleft(6);
console.log(deque2.popleft());
console.log(deque2.popleft());
console.log(deque2.popleft());
console.log(deque2.popleft());
console.log("len : ", deque2.length);
console.log(deque2.popleft());
console.log(deque2.popleft());
console.log(deque2.popleft());
