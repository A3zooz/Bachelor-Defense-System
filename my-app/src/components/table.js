    import React, { Component,useState,table, useEffect } from 'react'
    import LoadingScreen from "react-loading-screen";
    import spinner from'./download.gif'
    import ReactDOM from 'react-dom'
    import Timetable from 'react-scheduler-table'
    import CSVRenderer from './CSVRenderer'; 
    import { ToastContainer, toast } from 'react-toastify';
    import 'react-toastify/dist/ReactToastify.css';
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
        const handleSubmit = (event) => {      
            toast("CSV file is downloading !!!");}

    
        return (
            <div> 
            {isLoding ? (
            <LoadingScreen
            loading={true}
            logoSrc={spinner}
            // text="Loading..."
            />
            ) : (
            <>

            {showButton ? (<button  className="btn-const1" onClick={onGenerate}>Generate Solution</button>) :<> </> }
            {downButton ? (
            <> 
            <CSVRenderer data={data}></CSVRenderer>
            <form action='http://localhost:5000/downloadFile/'>
            <input onClick={handleSubmit} className="btn-const2" type="submit" value="Download Solution" />
            </form>
            <ToastContainer/>
            </> ) :
            <></>}
            </>
            )}

            </div> 

        )
    }