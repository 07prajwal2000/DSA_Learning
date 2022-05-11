function ArrayRotation(arr:number[], step: number): number[] {
    const temp = new Array(arr.length);
    for (let i = 0; i < arr.length; i++) {
        const idx = (step + i) % arr.length;
        temp[idx] = arr[i];
    }
    for (let i = 0; i < arr.length; i++) {
        arr[i] = temp[i];
    }
    return arr;
}

console.log(ArrayRotation([2, 3, 4, 5, 6], 3));