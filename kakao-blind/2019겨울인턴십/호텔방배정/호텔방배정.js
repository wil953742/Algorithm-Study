const solution = (k, room_number) => {
  const rooms = [];

  for(let i=0; i<k+1; i++) {
    rooms.push(false);
  }

  const answer = room_number.map((num) => {
    if(!rooms[num]) {
      rooms[num] = true;
      return num;
    }
    
    for(let i=num+1; i<k+1; i++) {
      if(!rooms[i]) {
        rooms[i] = true;
        return i;
      }
    }
  })

  return answer;
};

const sol = solution(10, [1, 3, 4, 1, 3, 1]);
console.log(sol); //[1,3,4,2,5,6]
