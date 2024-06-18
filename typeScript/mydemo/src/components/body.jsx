import React, { useState } from "react";

export default function Body() {
  const [name, setName] = useState("HI Venkatesh");//use state is used to re render the components

  function renderName() {
    setName("Hi Sai");
  }

  return (
    <div>
      <button onClick={renderName}>CLick Me</button>
      <h1>{name}</h1>
      <h2>{name}</h2>
    </div>
  );
}
