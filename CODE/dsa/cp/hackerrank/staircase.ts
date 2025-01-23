function staircase(n: number): void {
  // Write your code here

  /* #
    ##
   ###
  ####
 #####
######*/
  var space: number = n - 1;
  var star: number = 1;
  for (let i = 0; i < n; i++) {
    let line: string = "";
    for (let i = 0; i < space; i++) {
      line += " ";
    }
    for (let i = 0; i < star; i++) {
      line += "#";
    }
    space--;
    star++;
    console.log(line);
  }
}

function staircase2(n:number):void{
  for(let i=1;i<=n;i++){
let space:string=' '.repeat(n-i);
let star:string='#'.repeat(i);
console.log(space+star);

  
  }
``
}