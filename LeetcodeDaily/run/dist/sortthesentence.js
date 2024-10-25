"use strict";
function check1(s) {
    let res = '';
    let val = s.split(' ');
    val.sort((a, b) => {
        let num1 = parseInt(a.slice(-1));
        let num2 = parseInt(b.slice(-1));
        return num1 - num2;
    });
    for (let c of val) {
        c = c.slice(0, -1);
        res = res.concat(c, ' ');
    }
    return res;
}
let Example2 = "is2 sentence4 This1 a3";
console.log(check1(Example2));
