const x: number = 10000;
console.log(x);

function Greeting(name: string):object {
  console.log("Hello", { name });
  return {
    name
  }
}
//Good Boy 
const val=Greeting("Vnek");
console.log(val)
function Sum(a:number ,b:number){
  console.log(a+b);
}
Sum(102,330);

function runAfter1s( fun: () => void){
  setTimeout(fun,1000);
}
const sumfun=()=>Sum(29392392,9239239);
runAfter1s(sumfun);