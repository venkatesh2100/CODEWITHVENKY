//?Creeate a promise that execute when value is correct and error

let mypromise = new Promise(function (myvalue, myerror) {
  let success = false;  // Corrected 'ture' to 'true'
  if (success) {
    myvalue("Print the value");
  } else {
    myerror("Got an Error Baboi");
  }
});

mypromise.then((message) => {
  console.log(message);
}).catch((error) => {
  console.log(error);
});


// let mypromisecode=new Promise((myvalue,myReject)=>{
//   let sucess=true;


//   if(sucess){
//     myvalue("Print the the code follow in the function");
//   }else{
//     myReject("print the rejected code for the following funtion");
//   }
// })

// mypromisecode=then((message)=>{
//   console.log(message);
// }).catch((error)=>{
//   console.log(error);
// })