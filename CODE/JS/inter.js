const date = new Date();
console.log(date)
const arr = Array.of(100.2)
console.log(arr)
arr.push(200);

arr.forEach((a) => {
  console.log(a)
})
arr.push(100)
arr.unshift(100)
console.log(arr)
let res = arr.filter((a) => a === 100)
console.log(res)

//TIP: objects Usecase

class Car {

  constructor(model, color, price) {
    this.model = model;
    this.price = price;
    this.color = color;
  }

}
const myCar = new Car("Brezza VXI", "Arctic white", "9L")
console.log(myCar)


//TIP: promises and Asyncs

const myPromise = new Promise((resolve, reject) => {
  setTimeout(() => {
    console.log("Promise Success");
    resolve("Operation completed successfully!"); // You forgot this
  }, 2000);
});

const resolvedPromise = Promise.resolve("Instant");
const rejectPromise = Promise.reject("Error Promise Rejected");

// Handle myPromise
myPromise
  .then((result) => {
    console.log(result); // This will now log: "Operation completed successfully!"
  })
  .catch((error) => {
    console.error(error);
  })
  .finally(() => {
    console.log("myPromise resolved");
  });

// Handle the other promises too
resolvedPromise
  .then((result) => {
    console.log("Resolved:", result); // "Instant"
  });

rejectPromise
  .catch((error) => {
    console.error("Caught:", error); // "Error Promise Rejected"
  });

//HACK: Classs and functions 

class Person {
  name;

  constructor(name) {
    this.name = name;
  }

  Saymyname() {
    console.log(`Your name is${this.name}`)
  }
}

const Hey = new Person('Heisienbeg');
Hey.Saymyname()

console.log(0.1 + 0.2)
