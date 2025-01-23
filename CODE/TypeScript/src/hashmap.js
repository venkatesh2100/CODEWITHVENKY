let hashmap=new Map();

hashmap.set("1","venky");
hashmap.set("2","love");
hashmap.set("3","code");

hashmap.set("4",{"value":"29","code":"19"});

const res=hashmap.get("1");
console.log(res)
console.log(hashmap.get("4"));
console.log(hashmap.size)