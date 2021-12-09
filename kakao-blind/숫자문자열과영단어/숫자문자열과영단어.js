const words = {
  zero: "0",
  one: "1",
  two: "2",
  three: "3",
  four: "4",
  five: "5",
  six: "6",
  seven: "7",
  eight: "8",
  nine: "9",
};

function solution(s) {
  let answer = s;

  Object.keys(words).forEach((word) => {
    let init;
    while (true) {
      init = answer;
      answer = answer.replace(word, words[word]);

      if (init === answer) {
        break;
      }
    }
  });

  return parseInt(answer);
}

const solution2 = (s) => {
  s = s
    .replace(/zero/g, 0)
    .replace(/one/g, 1)
    .replace(/two/g, 2)
    .replace(/three/g, 3)
    .replace(/four/g, 4)
    .replace(/five/g, 5)
    .replace(/six/g, 6)
    .replace(/seven/g, 7)
    .replace(/eight/g, 8)
    .replace(/nine/g, 9);

  return parseInt(s);
};

const sol = solution2("1zerotwozero3");
console.log(sol); //234567
