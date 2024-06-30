import React, { useState } from "react";

export default function Body() {
  const [name, setName] = useState("HI Venkatesh");
  const [num,setNum]=useState();//use state is used to re render the components

  function renderName() {
    setName("Hi Sai");
  }

 function renderNum(){
  setNum(Math.random());
 }
// *we should prevent the unnecessary re render --By using Sperate components 
  return (
    <div>
      <button onClick={renderName } >CLick Me</button>
      <h1>{name}</h1> 
      <h2>{name}</h2>
      <button onClick={renderNum}>Number~~~</button>
      
      <p>Hihihihihilorem</p>
      <p>Hihihihihilorem</p>
      <p>Hihihihihilorem</p>
      <p>Hihihihihilorem</p>
      <p>Hihihihihilorem</p>
      <p>Hihihihihilorem</p>
      <p>Hihihihihilorem</p>
      <p>Hihihihihilorem</p>
      <p>lfkfdfkdjffkdf</p>
    </div>
  );
}
