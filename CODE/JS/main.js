

const arr = ['1', '2', '3']
//print the list of Arrays
for (let i = 0; i < arr.length; i++) {
  console.log(arr[i]);
}

console.log(eval(3 + 5))
a = eval(100 * 20)
console.log(a)

// alert("Hello")
//case Sensitive

function BlockScope() {
  {

    let a = 100;
    var b = 200;

    console.log(a, b);
  }

  console.log(a, b);
}

// console.log(b)
BlockScope();

let x;
x = 99;
console.log(typeof (x))

console.log("42" + 7)
num = 100.50
console.log(parseInt(num))
console.log(parseFloat(num))

//Arrow Function 
const check = (x) => {
  return x == 100 ? "Good" : `Bad Guy ${x}`;
}

ans = check(10)
console.log(ans)
//try catch block
try {
  throw "Error";
} catch (err) {
  console.log(err)
}


//basic For loops 
const fruits = ["apple", "orange", "grape"]

for (f in fruits) {
  console.log(fruits[f])
}
for (f of fruits) {
  console.log(f)
}

//Basic factorialiorail Function 
let memo = []
function factorial(x, memo) {
  if (x === 1n | x === 0n) {
    return 1n;
  } else if (memo[x]) {
    return memo[x]
  }
  else {
    memo[x] = factorial(x - 1n, memo) * x;
    return memo[x];
  }
}

console.time('factorial')
console.log(factorial(1000n, memo))
console.timeEnd('factorial')
