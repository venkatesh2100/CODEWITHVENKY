"use strict";
function check(s) {
    var _a;
    let val = ((_a = s.match(/\d+/g)) === null || _a === void 0 ? void 0 : _a.map(Number)) || [];
    return val;
}
let Example = "1 box has 3 blue 4 red 6 green and 12 yellow marbles";
console.log(check(Example));
