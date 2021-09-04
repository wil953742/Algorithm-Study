const stringSort = (string) => string.split("").sort().join('');

const getCombination = (order, list, idxList, courseNum) => {
    if(order.length < courseNum) return false;
    if(idxList.length === courseNum) {
        let combination =  idxList.map(idx=> order[idx]).join("");
        list.push(stringSort(combination));
        return true;
    }
    for(let i=idxList.length; i<order.length; i++) {
        if(i <= idxList[idxList.length-1]) {}
        else {
            idxList.push(i)
            getCombination(order, list, idxList, courseNum);
            idxList.pop();
        }
    }
    return list;
}

const getCombinationList = (orders, courseNum) => {
    let combinationList = [];
    orders.forEach(each => {
        let combination = getCombination(each, [], [], courseNum);
        if(combination) {
            combinationList.push(...combination);
        }
    });
    return combinationList;
}

const getMostOrderedList = (statistic, courseNum) => {
    let mostOrderedMenu = 0;
    let mostOrderedList = [];
    
    if(Object.keys(statistic).length === 0) return false;

    mostOrderedMenu = Object.keys(statistic).reduce((accu, curr) => {
        return statistic[accu] < statistic[curr] ? curr : accu;
    })

    mostOrderedList.push(mostOrderedMenu);
    if(statistic[mostOrderedMenu] < 2) return false;

    Object.keys(statistic).forEach(key => {
        if(statistic[mostOrderedMenu] === statistic[key] && mostOrderedMenu !== key) mostOrderedList.push(key)
    })

    return mostOrderedList;
}

function solution(orders, course) {
    let answer = [];
    while(course.length > 0) {
        let courseNum = course.shift();
        let combination = getCombinationList(orders, courseNum);
        let statistic = {};        
        combination.forEach(each => Object.keys(statistic).includes(each) ? statistic[each]+=1 : statistic[each]=1)
        let mostOrderedList = getMostOrderedList(statistic, courseNum)
        if(mostOrderedList) answer.push(...mostOrderedList);
    }
    return answer.sort();
}

let orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"];
let orders2 = ["XYZ", "XWY", "WXA"]
let course = [2,3,4];
let sol = solution(orders2, course);
//["AC", "ACDE", "BCFG", "CDE"];
console.log(sol);
