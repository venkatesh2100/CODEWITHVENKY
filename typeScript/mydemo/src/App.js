// import logo from './logo.svg';
import Header from "./components/header";
import Body from "./components/body";
function App() {


  const currentDate=new Date();
  return (
    <div className="App">
      <Header/>
      <h1>Hello world!</h1>
      <h2>The time Now is {currentDate.toLocaleTimeString()}</h2>
      <h2>Time in hrs {currentDate.getHours()} hrs</h2>
      <h2>Today day is {currentDate.toDateString()}</h2>
      <Body/>
    </div>
  );
}

export default App;
