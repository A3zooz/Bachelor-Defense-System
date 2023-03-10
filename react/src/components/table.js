import React, { Component,useState, useEffect } from 'react'
import table from 'react'
import LoadingScreen from "react-loading-screen";
import spinner from'./download.gif'
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import "./table.css"
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
        return axios.post('http://35.223.140.142/generate/').then((res) => {
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
        text={"This might take a while ~30 mins"}
        // textStyle={{ fontSize: "2px", color: "gray" }}
        />

        ) : (
        <>

        
        {showButton ? (<button  className="btn-const1" onClick={onGenerate}>Generate Solution</button>) :<> </> }
        {downButton ? (
        <> 
        <form action='http://35.223.140.142/downloadFile/'>
        <input onClick={handleSubmit} className="btn-const2" type="submit" value="Download Solution" />
        </form>
        <table className="ArchiveTable">
        <thead>
            <tr>
                <th>Examiner</th>
                <th>Supervisor</th>
                <th>Student</th>
                <th>Student Name</th>
                <th>Student Email</th>
                <th>Topic</th>
                <th>Time</th>
                <th>Room</th>
                <th>Color</th>
            </tr>
        </thead>
        <tbody>
            {data &&
            data.map((data, index) => (
                <tr key={index}>
                <td>{data.Examiner}</td>
                <td>{data.Supervisor}</td>
                <td>{data.Student}</td>
                <td>{data.Studentname}</td>
                <td>{data.Studentemail}</td>
                <td>{data.Topic}</td>
                <td>{data.Time}</td>
                <td>{data.Room}</td>
                <td>{data.Color}</td>
                </tr>
            ))}
        </tbody>
        </table>
        
        <ToastContainer/>
        </> ) :
        <></>}
        </>
        )}  

        </div> 

    )
}
