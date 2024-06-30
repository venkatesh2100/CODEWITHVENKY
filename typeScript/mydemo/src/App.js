import Header from "./components/header";
import Body from "./components/body";
import { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [todos, setTodos] = useState([]);
  const [error, setError] = useState(null);
  const [effectCount,setEffectCount]=useState(0);

  function sqaure(num){
    var ans=num*num;
    console.log(ans)
    return ans;
  }

sqaure(9483);
  useEffect(() => {
    if(effectCount < 2){
    axios.get("https://sum-server.100xdevs.com/todos")
      .then(function (response) {
        setTodos(response.data.todos);
      }).finally(()=>{
        setEffectCount(prevcount => prevcount+1)
      }).catch(function(error){
        console.error("Error",error);
        setError(error.message);
      })}
  }, [effectCount]);

  return (
    <div className="App">
      {error && <p style={{ color: 'red' }}>Error: {error}</p>}
      {todos.map((todo) => (
        <Todo key={todo.id} title={todo.title} desc={todo.description} />
      ))}
    </div>
  );
}

function Todo({ title, desc }) {
  return (
    <div>
      <h1>{title}</h1>
      <h2>{desc}</h2>
    </div>
  );
}

export default App;
