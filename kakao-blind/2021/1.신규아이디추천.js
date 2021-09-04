const step1 = id => id.toLowerCase()
const step2 = id => id.match(/[a-zA-Z0-9-_.]/g).join("");
const step3 = id => id.replace(/\.{2,}/g, '.');
const step4 = id => {
    id = id[0] === '.' ? id.slice(1) : id;
    id = id[id.length-1] === '.' ? id.slice(0,-1) : id
    return id;
}

const step5 = id => id.length === 0 ? 'a' : id;
const step6 = id => {
    id = id.length >= 16 ? id.slice(0, 15) : id;
    return step4(id);
}
const step7 = id => {
    let len = id.length;
    if(len <= 2) {
        id += id[len-1].repeat(3-len);
    }
    return id;
};

function solution(new_id) {
    let new_id1 = step1(new_id);
    let new_id2 = step2(new_id1);
    let new_id3 = step3(new_id2);
    let new_id4 = step4(new_id3);
    let new_id5 = step5(new_id4);
    let new_id6 = step6(new_id5);
    let new_id7 = step7(new_id6);

    return new_id7
}