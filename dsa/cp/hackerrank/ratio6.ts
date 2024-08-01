function plusMinus(arr: number[]): void {
  // Write your code here
  const arrsize: number = arr.length;
  var p: number = 0;
  var n: number = 0;
  var z: number = 0;
  //? Find Total postive negitive and Zeros  and find ratio
  for (let i = 0; i < arrsize; i++) {
    if (arr[i] > 0) {
      p++;
    } else if (arr[i] < 0) {
      n++;
    } else {
      z++;
    }
  }
  console.log(p/arrsize);
  console.log(n/arrsize);
  console.log(z/arrsize);
}
