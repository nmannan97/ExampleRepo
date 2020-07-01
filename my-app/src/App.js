import React from 'react';
import logo from './logo.svg';
import './App.css';
import Button from './Button'

var counter = 0;
function increment(){
  counter = counter+1;
  console.log("function entered")
};
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        
        <button onClick = {increment()}> click me! </button>
        <p> 
          {console.log("starting")}
          the button has been clicked {counter} times {console.log(counter)}
        </p>
      </header>
    </div>
  );
}

export default App;
//<Button/>