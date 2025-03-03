import React, { useState } from "react";
//creating a div TODO
const Todo = ({ key,title, desc }) => (
  <div>
    <h1>{key}</h1>
    <h2>{title}</h2>
    <p>{desc}</p>
  </div>
);

export default function Header() {
  const [todos, setTodos] = useState([
    {
      id: 1,
      title: "I wanna go to gym",
      desc: "Daily morning 6:00 am to 8:00 am",
    },
    {
      id: 2,
      title: "I wanna read books",
      desc: "Every evening from 7:00 pm to 8:00 pm",
    },
    {
      id: 3,
      title: "I wanna learn coding",
      desc: "Daily from 9:00 am to 11:00 am",
    },
  ]);

  function addTodo() {
    setTodos([
      ...todos,
      {
        id: todos.length + 1,
        title: `New Todo ${todos.length + 1}`,
        desc: `Description for todo ${todos.length + 1}`,
      },
    ]);
  }

  return (
    <div>
      <h1>ToDOs</h1>
      <button onClick={addTodo}>Add Todo</button>

      {todos.map((todo) => (
        <Todo key={todo.id} title={todo.title} desc={todo.desc} />
      ))}
    </div>
  );
}
