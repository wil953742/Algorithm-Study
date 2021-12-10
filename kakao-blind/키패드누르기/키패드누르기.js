const keyboard = {
  1: [0, 3],
  2: [1, 3],
  3: [2, 3],
  4: [0, 2],
  5: [1, 2],
  6: [2, 2],
  7: [0, 1],
  8: [1, 1],
  9: [2, 1],
  "*": [0, 0],
  0: [1, 0],
  "#": [2, 0],
};

const calcDistance = (coor1, coor2) =>
  Math.abs(coor1[0] - coor2[0]) + Math.abs(coor1[1] - coor2[1]);

function solution(numbers, hand) {
  let answer = "";
  let [leftThumb, rightThumb] = [keyboard["*"], keyboard["#"]];

  numbers.forEach((num) => {
    key = keyboard[String(num)];

    if (num === 0 || num % 3 === 2) {
      [leftDistance, rightDistance] = [
        calcDistance(key, leftThumb),
        calcDistance(key, rightThumb),
      ];

      if (leftDistance > rightDistance) {
        answer += "R";
        rightThumb = key;
      } else if (rightDistance > leftDistance) {
        answer += "L";
        leftThumb = key;
      } else {
        if (hand === "right") {
          answer += "R";
          rightThumb = key;
        } else {
          answer += "L";
          leftThumb = key;
        }
      }
    } else if (num % 3 === 1) {
      answer += "L";
      leftThumb = key;
    } else {
      answer += "R";
      rightThumb = key;
    }
  });

  return answer;
}

const sol1 = solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right");
console.log(sol1);
