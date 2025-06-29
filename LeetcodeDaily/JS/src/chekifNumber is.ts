

function check(s:string) {
 let val= s.match(/\d+/g)?.map(Number)||[];
 return val;
}

let Example= "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
console.log(check(Example))