interface Value1 {
  name: string;
  age: number;

}

function returnAge(user1: Value1, user2: Value1) {
  return user1.age + user2.age;
}

const result = returnAge(
  {
    name: "venkatesh",
    age: 90
  },
  {
    name: "venkatesh",
    age: 90
  }
);

console.log(result); // Output: 180
