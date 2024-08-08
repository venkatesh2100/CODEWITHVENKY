// function removeElement(nums: number[], val: number): number {
//   let j = 0;
//   let i = 0;
//   while (i < nums.length) {
//     if (nums[i] !== val) {
//       nums[j] = nums[i];
//       j++;
//     }
//     i++;
//   }
//   return j;
// }


function removeElement(nums:number[],val:number):number{
  let k=0;
  for(let i of nums){
    if(val!==i){
      nums[k++];
    }
  }

  return k;
}