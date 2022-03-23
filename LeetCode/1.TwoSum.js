function TwoSum(target, nums) {
    obj = {}

    for (let i = 0; i < nums.length; i++) {
        let diff = target - nums[i];

        if(diff in obj)
        {
            return [i, obj[diff]];
        }
        obj[nums[i]] = i;
    }
}

console.log(TwoSum(6, [3, 2, 4]));