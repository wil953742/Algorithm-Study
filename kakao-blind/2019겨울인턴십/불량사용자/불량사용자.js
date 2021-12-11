const stringToRegex = (s) => {
  return `/^${s.split("\*").join("\w")}$/`;
};

const solution = (user_id, banned_id) => {
  let answer = 0;

  console.log("frodoc".match(/(fr\wd\w)(\W|^)/g));

  return answer;
};

const sol = solution(
  ["frodo", "fradi", "crodo", "abc123", "frodoc"],
  ["fr*d*", "*rodo", "******", "******"]
);
console.log(sol); //3
