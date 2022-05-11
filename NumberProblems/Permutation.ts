function Permutation(n:number, r: number) {
    
    function Fact(n: number): number {
        if (n <= 1) {
            return n;
        }
        const val = n * Fact(n - 1);
        
        return val;
    }

    return Fact(n) / (Fact(n - r));
}

// HACK: Permutation FORMULA
// ( n ! ) / ( n - r )!
// n = 5, r = 2
// ( 5 * 4 ) / ( 2 * 1 )