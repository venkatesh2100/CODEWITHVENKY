import axios from 'axios';
import React, { useEffect, useState } from 'react'

function DataFectch() {
  const [todos, setTodos] = useState([]);
//? A good Examole of usecase of UseEffect Lovely
  useEffect(() => {
    axios.get("https://sum-server.100xdevs.com/todos").then(res => setTodos(res.data.todos))
  },[])
  return (
    <>{todos.map(todo => <Track todo={todo} />)}</>

  )
}


function Track({ todo }) {
  return (
    <div>{todo.title}
      <br />
      {todo.description}</div>
  )
}

export default DataFectch;