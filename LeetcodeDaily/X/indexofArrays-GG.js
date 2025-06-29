class Solution {
  // Function to find a continuous sub-array which adds up to a given number.
  subarraySum(arr, n, s) {
    // your code here
    let current_max = 0;
    let start_element = 0;
    //sliding window
    if (n === 1) {
      if (arr[0] === s) {
        return [1, 1];
      } else {
        return -1;
      }
    }
    for (let i = 0; i < n; i++) {
      current_max += arr[i];
      while (current_max > s && start_element <= i) {
        current_max -= arr[start_element];
        start_element++;
      }
      if (current_max == s) {
        return [start_element + 1, i + 1];
      }
    }

    return -1;
  }
}
const sol = new Solution();

console.log(sol.subarraySum([0], 1, 1));

