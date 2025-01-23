function subarraySum(arr, n, sum) {
  // To store the result
  let res = [];

  // Flag to indicate if the subarray is found
  let flag = false;

  for (let i = 0; i < n; i++) {
    // Initialize the current sum
    let currentSum = arr[i];

    // Check if the single element is the sum
    if (currentSum === sum) {
      res.push(i + 1);
      res.push(i + 1);
      flag = true;
      break;
    } else {
      // Try all subarrays starting with 'i'
      for (let j = i + 1; j < n; j++) {
        currentSum += arr[j];

        if (currentSum === sum) {
          res.push(i + 1);
          res.push(j + 1);
          flag = true;
          break;
        }
      }
      if (flag) break;
    }
  }
  if (flag) return res;
  return [-1]; // If no subarray is found
}

// Driver Code
let arr = [15, 2, 4, 8, 9, 5, 10, 23];
let n = arr.length;
let sum = 23;
let result = subarraySum(arr, n, sum);
for (let i of result) console.log(i);
