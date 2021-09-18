function InfoObj(info) {
    [this.language, this.group, this.career, this.soulFood, this.score] = info.trim().split(" ")
}

const check = (infoObj, language, group, career, soulFood, score) => {
    if(language !== '-' && language !== infoObj.language) {
        return false;
    }

    if(group !== '-' && group !== infoObj.group) {
        return false;
    }

    if(career !== '-' && career !== infoObj.career) {
        return false;
    }

    if(soulFood !== '-' && soulFood !== infoObj.soulFood) {
        return false;
    }

    if(parseInt(score) > parseInt(infoObj.score)) {
        return false;
    }

    return true;
}

const search = (query, infoObjList) => {
    let count = 0;
    let queryRegex = /(cpp|java|python|-) and (backend|frontend|-) and (junior|senior|-) and (chicken|pizza|-) ([\d]+)/; 
    let [, language, group, career, soulFood, score] = query.match(queryRegex);
    for(let infoObj of infoObjList) {
        let checkRes = check(infoObj, language, group, career, soulFood, score)
        if(checkRes) {
            count += 1;
        }
    }
    return count;
}

function solution(info, query) {
    let infoObjList = info.map(each => new InfoObj(each));
    let answer = query.map(each => search(each, infoObjList))
    return answer;
}

let infoElement = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"];
let queryElement = ["- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"];
let sol = solution(infoElement, queryElement)//[1]

console.log(sol);