function removeElement(nums: number[], val: number): number {
  let j = 0;
  let i = 0;
  while (i < nums.length) {
    if (nums[i] !== val) {
      nums[j] = nums[i];
      j++;
    }
    i++;
  }
  return j;
}
