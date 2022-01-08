import React,{useState} from 'react'

const Hook = () => {
    const [state, setState] = useState([])
    const [item, setItem] = useState()
    function handleChange(e) {
        setItem(e.target.value)       
    }
    function handleCLick() {
        console.log(item)
        setState([...state,{key:state.length,value:item}])
    }

    return (
        <div>
            <h1>Hello</h1>
            <input type="text" value={state.value} onChange={(e)=>handleChange(e)}/>
            <button onClick={handleCLick}> on Click</button>
            <ul>
                {state.map((item) => (
                    <li key={item.key}>{ item.value}</li>
                ))}
            </ul>
        </div>
    )
}

export default Hook