

class Solution {

  add = (a: number, b: number): number => {
    return a + b;
  }

  solve = () => {
    return this.add(10, 15);
  }

}

const calc = new Solution();
console.log(calc.solve());
