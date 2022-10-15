import React  from "react";
const axios = require("axios").default;
export default function Table(){
    const onGenerate=()=>{
        axios.post('http://localhost:5000/generate/').then(res => console.log(res));
    };
    
    return (
        <div>
            <button onClick={onGenerate}>generte Solution</button>
        </div>
    )
}