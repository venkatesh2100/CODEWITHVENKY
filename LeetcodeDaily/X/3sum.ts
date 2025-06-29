function threeSum(nums: number[]): number[][] {
  const arr: string[];
  for (let i = 1; i < nums.length; i++) {
    for (let j = 2; j < nums.length; j++) {
      for (let m = 3; m < nums.length; m++) {
        if (nums[i] + nums[j] + nums[m] == 1) {
          if (i != j && j != m && m != i) {
            arr.push[(nums[i], nums[j], nums[m])];
          }
        }
      }
    }
  }
  return arr;
}
