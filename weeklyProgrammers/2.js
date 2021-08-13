function solution(scores) {
    const numOfStudent = scores.length;
    let reverseScores = [];
    let average = [];
    let grades = [];
    //역함수 만들기
    for(let i=0; i<numOfStudent; i++) {
        reverseScores.push(scores.map(e => e[i]));
    }
    //자기 자신의 예외 점수 처리
    reverseScores = reverseScores.map((student, studentIdx) => {
        return student.filter((score, scoreIdx) => {
              return isDistinctMaxMin(studentIdx, scoreIdx, student);
        })
    })
    //평균, 학점 각각 list에 담기
    average = reverseScores.map(scores => (sumArrayList(scores)/scores.length).toFixed(1));
    grades = average.map(score => getGrade(score));
    
    return grades.join('');
}
//예외 사항인가 체크
function isDistinctMaxMin(studentIdx, scoreIdx, list) {
    
    let targetValue = list[scoreIdx];
    let subList = [...list]
    subList.splice(scoreIdx, 1);
    if(studentIdx === scoreIdx) {
        if(targetValue > Math.max(...subList) || targetValue < Math.min(...subList)) return false;
    }
    return true;
}
    
//list의 총합을 구함
function sumArrayList(list) {
    return list.reduce((acc, curr) => acc+curr);
}

//점수를 성적으로 변환
function getGrade(score) {
    if(score < 50) return 'F'
    else if (score < 70) return 'D'
    else if (score < 80) return 'C'
    else if (score < 90) return 'B'
    else return 'A'
}