function maxSubArray(nums: number[]): number {
  //?Add the array and comapare with res value.
let res=Number.MIN_SAFE_INTEGER-1;

  let subArr=0;
  for(let num of nums){
    subArr+=num;

    if(subArr>res){
      res=subArr;
    }
    if(subArr<0){
      subArr=0;
    }
  }
  return res;
};