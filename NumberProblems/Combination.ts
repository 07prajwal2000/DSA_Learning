function Combination(n:number, r: number): number {
    let row = 1;
    let col = 1;

    for (let i = 1; i <= r; i++) {
        row *= n;
        n--;
    }
    for (let i = 1; i <= r; i++) {
        col *= i;
    }
    return (row / col);
}

// HACK: Combination FORMULA
// n = 5, r = 2
// { n * (n - 1) * ... * (n - r) } / { r * (r - 8) * ... * (r - 0) }
// ( 5 * 4 ) / ( 2 * 1 )