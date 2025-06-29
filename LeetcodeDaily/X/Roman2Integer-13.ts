function romanToInt(s: string): number {

//?Set the Hashmao values
  let hashMap=new Map();
  hashMap.set('I',1);
  hashMap.set('V',5);
  hashMap.set('X',10);
  hashMap.set('L',50);
  hashMap.set('C',100);
  hashMap.set('D',500);
  hashMap.set('M',1000);
let ans=0;

  for(let i=0;i<s.length;i++){

    //? IV => 5 -1 = 4
      if(i<s.length-1 && hashMap.get(s.charAt(i))<hashMap.get(s.charAt(i+1))){
        ans-=hashMap.get(s.charAt(i));
      }else{//?VI 5 + 1 = 6
        ans+=hashMap.get(s.charAt(i);)
      }
  }

  return ans;

};