const recur = (order, list, idxList) => {
    if(idxList.length === 3) {
        let combination =  idxList.map(idx=> order[idx]).join("");
        list.push(combination);
        return true;
    }
    
    for(let i=idxList.length; i<order.length; i++) {
        if(i <= idxList[idxList.length-1]) {}
        else {
            idxList.push(i)
            recur(order, list, idxList);
            idxList.pop();
        }
    }
    return list;
}

let recu = recur("ABCDE", [], []);
console.log(recu);