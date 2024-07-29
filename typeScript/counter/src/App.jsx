import React, { useEffect } from 'react'
import { useCallback } from 'react';
import { memo, useState } from 'react'
import DataFectch from './customHooks/Datafetch';
export default function App() {

  const [render,setRender]=useState(true);
  useEffect(()=>{
    setTimeout(()=>{
    setRender(false)
    },5000)
  },[]);
  return (
    <>
    <DataFectch/>
      {render?<SetUse />:<div></div>}
    </>)
}

//* create a useEfect to render flase

function ClickButton() {

  const [count, setCount] = useState(0);
  const onclic = useCallback(() => {
    console.log("HIHI");
  }, [])
  return (
    //Now usecallback
    <div>
      <ButtonComponent onClick={onclic} />
      <button onClick={() => setCount(count + 1)}>couter {count}</button>
    </div>
  )
}
//* Create a useEffect use Button by using setTimeout
function SetUse() {
  const [count, setCount] = useState(0);
  console.log("out")
  useEffect(() => {
    setTimeout(() => {
      setCount((count) => count + 1);
    }, 1000)
    console.log("IN")
  }, [])
  return (
    <h1>Number of render is {count}</h1>
  )
}
function UseEffectButton() {
  console.error("outside the return")
  useEffect(() => {
    return (
      console.error("Inside the return ")
    )
  }, [])
  return (
    <div>Inside the component</div>
  )
}

const ButtonComponent = memo(() => {
  console.log("child is render")
  return (
    <div><button>Button is clicked</button></div>
  )

})