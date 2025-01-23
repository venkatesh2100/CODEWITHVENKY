import React, { useRef, useState } from "react";

// Create a component that tracks and displays the number of times it has been rendered. Use useRef to create a variable that persists across renders without causing additional renders when it changes.

export default function Assignment2() {
  const [renderdemo, setRender] = useState(0);
  const renderCount = useRef(0);

  const handleReRender = () => {
    // Update the render count using useRef
    renderCount.current++;
    setRender(Math.random());
    // Update the state to force re-render
    // setRender(render + 1);
  };

  return (
    <div>
      <p>This component has rendered {renderdemo} times.</p>
      <button onClick={handleReRender}>Force Re-render</button>
      <button></button>
    </div>
  );
}

//! Assingment One code
// import React, { useEffect, useRef, useState } from 'react';

// // Create a component with a text input field and a button. When the component mounts or the button is clicked, automatically focus the text input field using useRef.
// export default function Assignment1() {
//   const inputRef = useRef(null);
//   const [divs, setDivs] = useState([]);

//     setTimeout(() => {
//       if (inputRef.current) {
//         inputRef.current.focus();
//       }
//     }, 1000); // 1 second delay

//     let interval;
//     setTimeout(() => {
//       interval = setInterval(() => {
//         setDivs((prevDivs) => {
//           if (prevDivs.length >= 5) {
//             clearInterval(interval);
//             return prevDivs;
//           }
//           return [...prevDivs, <div key={prevDivs.length}><p>Hello</p></div>];
//         });
//       }, 2000); // 2 seconds delay
//     }, 1000); // 1 second delay before starting to add divs
//   }, []);

//   const handleButtonClick = () => {
//     if (inputRef.current) {
//       inputRef.current.focus();
//     }
//   };

//   return (
//     <div>
//       <input type="text" ref={inputRef} placeholder="Enter text here" />
//       <button onClick={handleButtonClick}>Focus Input</button>
//       {divs}
//     </div>
//   );
// }

////! This code useses Divref to Override the DOM element
// import { useCallback, useEffect, useRef, useState } from 'react'

// function App() {
//   const divRef = useRef();

//   useEffect(() => {
//     setTimeout(() => {
//       // divRef.current.innerHTML = "10"
//       console.log(divRef.current);
//       document.getElementById('container').innerHTML=10;
//     }, 5000);
//   }, [])

//   const incomeTax = 20000;

//   return (
//     <div>
//         {/* hi there, your income tax returns are <div ref={divRef}>{incomeTax}</div> */}
//         hi there, your income tax returns are <div id='container' ref={divRef}>{incomeTax}</div>

//     </div>
//   )
// }

// export default App

////! useMemo Code
// import { useEffect, useMemo, useState } from 'react'

// function App() {
//   const [exchange1Data, setExchange1Data] = useState({});
//   const [exchange2Data, setExchange2Data] = useState({});
//   const [bankData, setBankData] = useState({});

//   useEffect(() => {
//     // Some operation to get the data
//     setExchange1Data({
//       returns: 100
//     });
//   }, [])

//   useEffect(() => {
//     // Some operation to get the data
//     setExchange2Data({
//       returns: 100
//     });
//   }, [])

//   useEffect(() => {
//     // Some operation to get the data
//     setTimeout(() => {
//       setBankData({
//         income: 100
//       });
//     },3000)
//   }, [])
//   console.log("Before")
//   //? we need to Memoize this equation mean skip this function or calculation for the next time(useMemo)
//   const cryptoReturns = useMemo(() => {
//     console.log("hi")
//     return exchange1Data.returns + exchange2Data.returns;
//   }, [exchange1Data, exchange2Data])
//   console.log("AFter")
// // const cryptoReturns =exchange1Data.returns + exchange2Data.returns;
//   const incomeTax = (cryptoReturns + bankData.income) * 0.3

//   return (
//     <div>
//       hi there, your income tax returns are {incomeTax}
//     </div>
//   )
// }

// export default App

//!useEffect code
// import { useEffect, useState } from 'react'

// function App() {
//   const [exchangeData, setExchangeData] = useState({});
//   const [bankData, setBankData] = useState({});
//   console.log("Hi re-render")

//   useEffect(() => {
//     setTimeout(() => {
//       setBankData({ income: 100 });
//     }, 2000);

//     setTimeout(() => {
//       setExchangeData({
//         returns: 100
//       });
//     }, 1000);
//   }
//   , [])

//   // fetch("https://google.com", async (res) => {
//   //   const json = await res.json();
//   //   setBankData({income:100});
//   //   // Assume it is { income: 100 }
//   // });

//   const incomeTa = (bankData.income + exchangeData.returns) * 0.3;

//   return (
//     <div>
//       hi there, your income tax returns are {incomeTa}
//     </div>
//   )
// }

// export default App
