const relax = () => {};

const disX = (x, n) => {
    let dis = [];
    for(let i=0; i<n; i++) {
        dis.push(Infinity);
    }
    dis[x] = 0;
    return dis;
}

function solution(n, s, a, b, fares) {
    var answer = 0;
    
    let matrix = [];
    for(let y=0; y<n; y++) {
        let row = [];
        for(let x=0; x<n; x++) {
            row.push(0);
        }
        matrix.push(row);   
    }

    for(let ele of fares) {
        let x = ele[0]-1;
        let y = ele[1]-1;
        matrix[x][y] = ele[2];
        matrix[y][x] = ele[2];
    }
    
    let disA = disX(a, n);
    let disB = disX(b, n);
    
    for(let i=0; i<n; i++){
        if(matrix[a-1][i] > 0) {
            
        }
    }
    
    console.log(disA);
    console.log(disB);
    return matrix;
}

let fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
let sol = solution(6, 4, 6, 2, fares);
console.log(sol);