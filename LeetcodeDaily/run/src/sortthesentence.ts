



//?sort the string in number format
function check1(s:string) {
  let res:string='';
  let val= s.split(' ');
//?sort the array by  Number
 val.sort((a,b)=>{
  let num1=parseInt(a.slice(-1));
  let num2=parseInt(b.slice(-1));
  return num1-num2;
 })


  //?remove the last word.
  for(let c of val){
    c=c.slice(0,-1);
    res=res.concat(c,' ');
  }
  return res;
 }

let Example2= "is2 sentence4 This1 a3"
 console.log(check1(Example2))