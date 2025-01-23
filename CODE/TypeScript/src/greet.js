
//Interface whioh is used to pass the values
interface User {
  firstname: string;
  lastname: string;
  age: number;
  email?:string
}

function isLegal(user: User): boolean {
  return user.age > 18;
}

const person1 = isLegal({
  firstname: "kjfdk",
  lastname: "kfjkldkf",
  age: 20,
  email:"lfdklfkd"
});

function Greet(user: User, isAdult: boolean): void {
  if (isAdult) {
    console.log(`Hi ${user.firstname}, you are an adult.`);
  } else {
    console.log(`Hi ${user.firstname}, you are not an adult.`);
  }
}

// Call the Greet function
Greet({
  firstname: "kjfdk",
  lastname: "kfjkldkf",
  age: 20,
}, person1);
