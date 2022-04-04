function RotateArray(nums, k) {
    let temp = new Array(nums.length)
    for (let i = 0; i < nums.length; i++) {
        const idx = ( i + k ) % nums.length;
        temp[idx] = nums[i];
    }
    for (let i = 0; i < nums.length; i++) {
        nums[i] = temp[i]
    }
}

let arr = [1,2,3,4,5,6,7]
RotateArray(arr, 2)
console.log(arr);