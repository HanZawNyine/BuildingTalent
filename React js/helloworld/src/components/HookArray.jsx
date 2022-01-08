import React, { useState } from 'react'

function HookArray() {
    const [todos, setTodos] = useState([{text: 'Learn Hooks' }]);
    function handleOrangeClick() {
        setTodos({key:todos.length, text: 'orange' });
        console.log(todos)
    }
    return (
        <div>
            <h1>Hello</h1>
            <input/>
            <button onClick={handleOrangeClick}>Click</button>            
           
        </div>
    )
}

export default HookArray
