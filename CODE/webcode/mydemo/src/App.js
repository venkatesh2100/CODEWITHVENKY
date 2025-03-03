import Header from "./components/header";
import Body from "./components/body";
import { useEffect, useMemo, useState } from "react";
import axios from "axios";

function App() {
  const [todos, setTodos] = useState([]);
  const [error, setError] = useState(null);
  const [effectCount,setEffectCount]=useState(0);
  const [state ,setState]= useState("red");
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
  
 const expensiveValue=useMemo(()=>{
  
  let result=0;
  for(let i=0;i<10000000;i++){
    result+=i;
  }
  return result+num;
 },[num])

  return (
    <div className="App" >
      <button onClick={()=>setState("blue")}>1</button>
      <button onClick={()=>setState("orange")}>2</button>
      <button>3</button>
      <button>4</button>
      <input type="box"></input>
      <button>Counter</button>
      <p>Hi this is color {state}</p>
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
