import React  from "react";
const axios = require("axios").default;
export default function Table(){
    const onGenerate=()=>{
        axios.post('http://localhost:5000/generate/').then(res => console.log(res.data));
    };
    
    return (
        <div>
            <button onClick={onGenerate}>Generate Solution</button>
        </div>
    )
}