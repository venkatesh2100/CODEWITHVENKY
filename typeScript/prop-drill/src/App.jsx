import { useContext, useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import { CounterContext } from "./Context.jsx";

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <CounterContext.Provider value={{ count, setCount }}>
        <Count />
      </CounterContext.Provider>
    </>
  );
}

// Create Two Components which render Two Button + & - and count
function Count() {
  return (
    <>
      <Counter />
      <Button />
    </>
  );
}

//

function Counter() {
  const { count } = useContext(CounterContext);

  return (
    <>
      <p>Value: {count}</p>
    </>
  );
}

console.log("HI Bro");

console.log("name?");
console.log("hio");
function Button() {
  const { count, setCount } = useContext(CounterContext);

  return (
    <>
      <button onClick={() => setCount(count + 1)}>Increment</button>
      <button onClick={() => setCount(count - 1)}>Decrement</button>
    </>
  );
}

export default App;
