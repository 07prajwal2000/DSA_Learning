function SetZeroMatrix(matrix:number[][]) {
    const row = matrix.length;
    const column = matrix[0].length;
    const dummyRow: number[] = new Array(row).fill(-1);
    const dummyCol: number[] = new Array(column).fill(-1);
    for (let i = 0; i < row; i++) {
        for (let j = 0; j < column; j++) {
            if (matrix[i][j] === 0) {
                dummyRow[i] = 0;
                dummyCol[j] = 0;
            }
        }
    }

    for (let i = 0; i < row; i++) {
        for (let j = 0; j < column; j++) {
            if (dummyCol[j] === 0 || dummyRow[i] === 0) {
                matrix[i][j] = 0;
            }
        }
    }
    
}

function SetZeroMatrix_BruteForce(matrix:number[][]) {
    const row = matrix.length;
    const column = matrix[0].length;
    for (let i = 0; i < row; i++) {
        for (let j = 0; j < column; j++) {
            if (matrix[i][j] === 0) {
                let idx = 0;
                while (idx < row) {
                    if (matrix[idx][j] !== 0) {
                        matrix[idx][j] = null;
                    }
                    idx++;
                }
                idx = 0;
                while (idx < column) {
                    if (matrix[i][idx] !== 0) {
                        matrix[i][idx] = null;
                    }
                    idx++;
                }
            }
        }
    }

    for (let i = 0; i < row; i++) {
        for (let j = 0; j < column; j++) {
            if (matrix[i][j] === null) {
                matrix[i][j] = 0;
            }
        }
    }
}

const matrix = [
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]
];
for (let i = 0; i < matrix.length; i++) console.log(matrix[i]);
console.log("\n\n");

SetZeroMatrix_BruteForce(matrix);

console.log("\n\n");
for (let i = 0; i < matrix.length; i++) console.log(matrix[i]);