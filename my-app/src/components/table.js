import React, { Component,useState,table, useEffect } from 'react'
import ReactDOM from 'react-dom'
import Timetable from 'react-scheduler-table'
const axios = require("axios").default;
export default function Table(){
    // const loadDates = (searchDate) => {
    //     return axios.get(url).then((res) => {
    //       const exams = res.data["dates"];
    //       setDates(exams);
    //       let list = [];
    //       exams.forEach((ex) => list.push({ value: ex, label: ex }));
    //       return list.filter((d) => d.label.toLowerCase().includes(searchDate.toLowerCase()));
    //     });
    //   };


    const [data, setData] = useState();
    const [dwata, setDwata] = useState(false);
    // useEffect(() => {
    //     // Update the document title using the browser API
    //     setDwata= true;

    //     });
    const onGenerate=()=>{
        return axios.post('http://localhost:5000/generate/').then((res) => {
            console.log("HELLOOO")
            setDwata = true;
            this.forceUpdate()
            return table;
    });
    };
    const onDownload=()=>{
        return axios.post('http://localhost:5000/downloadFile/').then((res) => {
        console.log(res.data)
    });
    };



    return (

        <div> 
        <button onClick={onGenerate}>Generate Solution</button>
        <button onClick={onDownload}>Downlaod Solution</button>
        <a href='/Solution.json' download>Click to download</a>

        </div> 

    )
}