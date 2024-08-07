type NumberArr=number[];

 
functio maxElement(arr:NumberArr){
  var max:number=0
  for(let i=0;i<arr.length;i++){
    if(arr[i]>max){
      max=arr[i];
    }
  }
  console.log(max);
}
const arr:number[]=[23,32,34,23,4,656,7,68];
maxElement(arr);
