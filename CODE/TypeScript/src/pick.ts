interface User {
  name: string;
  age: number;
  email?: string;
  pass: string;
}

// Correct usage of Pick
type updateUser = Pick<User, 'name' | 'pass' | 'age'>;


type updateUserOptional=Partial<updateUser>
const displayUser = (user: updateUserOptional) => {
  // Use backticks for string interpolation
  console.log(`Name: ${user.name}, Age: ${user.age}`);
}

// Example usage:
const user: updateUserOptional = {
  name: "venkatesh",
  age: 25
};

displayUser(user); // Output: Name: venkatesh, Age: 25
