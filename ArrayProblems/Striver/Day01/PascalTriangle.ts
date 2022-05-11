function generatePascalTriangle(numRows: number): number[][] {
    const result: number[][] = [];
    let pre: number[] = [];

    for (let i = 0; i < numRows; i++) {
        const arr: number[] = [];
        for (let j = 0; j <= i; j++) {
            if (j === 0 || j === i) {
                arr.push(1);
            }
            else
                arr.push(pre[j - 1] + pre[j]);
        }

        pre = arr;
        result.push(arr);
    }

    return result;
}

console.log(generatePascalTriangle(5));