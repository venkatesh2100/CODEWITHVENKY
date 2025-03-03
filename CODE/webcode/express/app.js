const express = require('express');
const app = express();
const port = 3000;

// Middleware to log request time
app.use((req, res, next) => {
  console.log('Time: ', Date.now());
  next();
});

// Route for the home page
app.get('/', (req, res) => {
  res.send('BRO CODE');
});

app.put('/code',(req,res)=>{
  res.send("Hello meow")
})
app.delete('/',(req,res)=>{
  res.send('This code is Deleted')
})
// Start the server
app.listen(port, () => {
  console.log(`App is Working on ${port}`);
});
