const s = "carbar";
const t = "carbar";
const hashMap = new Map();

for (let c of s) {
  if (hashMap.has(c)) {
    hashMap.set(c, hashMap.get(c) + 1);
  } else {
    hashMap.set(c, 1);
  }
}


console.log(isAnagram(hashMap,t))
console.log(hashMap);
