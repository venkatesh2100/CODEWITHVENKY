function birthdayCakeCandles(candles) {
  // Write your code here
  let maxvalue=new Map();
  let val=0;
  let max=0;
  for(const number of candles ){
    // maxvalue=(maxvalue[number]|| 0)+1;
    maxvalue.set(number,(maxvalue.get(number)||0)+1);
      if(number>val){
          // maxvalue.set("max",maxvalue.get(number));
          val=number;
          // max=maxvalue.get(number);
      }else if(number===val){

          max=maxvalue.get(number);
      }
  }
  return  max;
  // return maxvalue.get("max");
  // return maxvalue.size;
}
const candles=[3,2,1,3]
console.log(birthdayCakeCandles(candles))