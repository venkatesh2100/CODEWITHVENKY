//HACK: simple loging of data
const x = 10;
console.log(10);

console.log([29, 399, 299, 20]);

//TODO:: Now convert Array to Unit8Arr
const arr = new Uint8Array([10, 240, 2999, 256]);
console.log(arr);

function AssciitoByte(val) {
  res = [];

  for (let i = 0; i < val.length; i++) {
    res.push(str.charCodeAt(i));
  }
  return res;
}

str = "HEllO";
console.log(str);
console.log(AssciitoByte(str));
