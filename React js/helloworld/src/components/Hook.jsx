import React,{useState} from 'react'

const Hook = () => {
    const [state, setState] = useState([])
    const [item, setItem] = useState()
    function handleChange(e) {
        setItem(e.target.value)       
    }
    function handleCLick() {
        // console.log(item)
        setState([...state, { key: state.length, value: item }])
        setItem('')
    }

    return (
        <div>
            <h1>To Do App</h1>            
            <div class="mb-3">
                <input className={'form-control'} type="text" value={item} onChange={(e)=>handleChange(e)}/>
            </div>
            <button type="submit" className={'btn btn-primary'} onClick={handleCLick}>Click</button>
            <div className={'mt-3 container'}>
                <table class="table">
                <thead>
                    <th scope='col'>#</th>
                    <th>To Do</th>
                </thead>
                <tbody>
                    {state.map((item) => (
                        <tr>
                            <th scope='row' key={item.key}>{item.key + 1}</th>
                            <td key={item.key}>{item.value}</td>
                        </tr>
                ))}
                </tbody>
            </table>
            </div>
            
        </div>
    )
}

export default Hook