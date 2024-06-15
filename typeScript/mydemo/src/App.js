// import logo from './logo.svg';
import './App.css';

function App() {


  const currentDate=new Date();
  return (
    <div className="App">
      <h1>Hello world!</h1>
      <h2>The time Now is {currentDate.toLocaleTimeString()}</h2>
      <h2>Time in hrs {currentDate.getHours()} hrs</h2>
      <h2>Today day is {currentDate.toDateString()}</h2>
    </div>
  );
}

export default App;
