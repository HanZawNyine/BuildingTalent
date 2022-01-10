import react, { useState } from 'react';
import './App.css';
import List from './components/List'

function App() {
  const [Todo, setTodo] = useState("")
  function addTodo(e) {
    // setTodo([...Todo,e])
    console.log(e)
  }
  return (
    <div className="App">
      <List setTodo={addTodo}/>
    </div>
  );
}

export default App;
