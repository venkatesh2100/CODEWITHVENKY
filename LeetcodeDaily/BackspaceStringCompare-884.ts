function backspaceCompare(s: string, t: string): boolean {
  //?compare both
  return compare(s) === compare(t);
};
//?function using stack to => array of char && if # appears pop from the stack

function compare(text:string):string{
  let res:string[]=[];

  for(let c of text){
      if(c==='#'){
          res.pop();
      }else{
          res.push(c);
      }
  }
  //?join and return the string
  return res.join('');

}