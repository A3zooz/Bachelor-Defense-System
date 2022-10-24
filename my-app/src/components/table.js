    import React, { Component,useState,table, useEffect } from 'react'
    import LoadingScreen from "react-loading-screen";
    import spinner from'./download.gif'
    import ReactDOM from 'react-dom'
    import Timetable from 'react-scheduler-table'
    const axios = require("axios").default;
    export default function Table(){
        const [data, setData] = useState();
        const [isLoding, setIsLoding] = useState(false);
        const [showButton, setShowButton] = useState(true);
        const [downButton, setdownButton] = useState(false);
        const onGenerate=(event)=>{
            setIsLoding(true)
            setShowButton(false)
            setdownButton(true)
            return axios.post('http://localhost:5000/generate/').then((res) => {
                console.log("HELLOOO")
                console.log(res.data[0])
                setData(res.data[0]);
                console.log(data)
                setIsLoding(false)
                this.forceUpdate()
                return table;
        });
        };

        return (
            <div> 
            {isLoding ? (
                <LoadingScreen
            loading={true}
            textColor="#676767"
            logoSrc={spinner}
            text="Loading..."
            />
            ) : (
            <>

            {showButton ? (<button  className="btn-const1" onClick={onGenerate}>Generate Solution</button>) :<> </> }
            {downButton ?
            (<form action='http://localhost:5000/downloadFile/'>
            <input  className="btn-const1" type="submit" value="Download Solution" />
            </form>) :
            <></>}
            </>
            )}

            </div> 

        )
    }