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

function remove(nums: number[], val: number): number {
  let k = 0;

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== val) {
      nums[k] = nums[i];
      k++;
    }
  }
  return k;
}
