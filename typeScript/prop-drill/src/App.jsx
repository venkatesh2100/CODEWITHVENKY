import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
function App() {

const [count, setCount] = useState(0)
  return (
    <>
    <Count count={count}/>
    <Button setCount={setCount} count={count}/>
    </>
  )
}

//?Create Two Components which render Two Button + & - and count
//?Create a Counter component in the Count
function Count({count}){
  return(
    <>
    <Counter count={count}/>
    </>
  )
}
function Counter({count}){
  return(
    <>
    {count}</>
  )
}
function Button({setCount ,count}){
  return(
    <>
    <button onClick={()=>setCount(count+1)}>Increment</button>
    <button onClick={()=>setCount(count-1)}>Decrement</button>
    </>
  )
}

export default App
