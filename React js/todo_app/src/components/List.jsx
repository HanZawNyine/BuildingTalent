import React,{useState} from 'react'

function List(props) {
    const [toto, setToto] = useState("");
    return (
        <div>
            <input type='text' value={toto} onChange={(e) => setToto(e.target.value)}/>
            <button onClick={(toto)=>props.addTodo(toto)}>add</button>
        </div>
    )
}

export default List
