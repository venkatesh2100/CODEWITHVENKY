import React from 'react'
import { useCallback } from 'react';
import { memo, useState } from 'react'

export default function App() {
  const [count, setCount] = useState(0);
  //Now usecallback
  const  onclic=useCallback(()=>{
    console.log("HIHI");
  },[])
  return (
    <div>
      <ButtonComponent onClick={onclic}/>
      <button onClick={() => setCount(count + 1)}>couter {count}</button></div>
  )

}

const ButtonComponent = memo(() => {
  console.log("child is render")
  return (
    <div><button>Button is clicked</button></div>
  )

})