function containsDuplicate(nums: number[]): boolean {
  let hashMap = new Map<number, number>();

//?Find the Number of occurance of the num
  for (let num of nums) {
      if (hashMap.has(num)) {
          hashMap.set(num, hashMap.get(num) + 1);
      } else {
          hashMap.set(num, 1);
      }
  }
  //?above code in single line => hashMap.set(num,hashMap.has(num)?(hahsMap.get(num)+1):+1);

//?And then check if any num is occured > 1
  for(let [num,count] of hashMap){
      if(count>1){
          return true;
      }
  }
  return false;

/**
 * single line code HEHEHHE using SET contains unique values
 * return nums.lenght!==Set(nums).size
 */

};