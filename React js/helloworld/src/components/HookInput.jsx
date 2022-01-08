import React, { useState } from 'react'
 
function HookInput() {
    const [count, setCount] = useState([{key:0,text:0}]);
    return (
      <div>
            <p>You clicked {count.key} {count.text} times</p>
            <input/>
            <button onClick={(envent) =>setCount([...count,{key:count.length,text:10}])}>
         Click me
            </button>
            <ul>

            </ul>
     </div>
    );

}

export default HookInput
