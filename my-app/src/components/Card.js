import React, { useState, } from "react";
import AsyncSelect from "react-select/async";
import makeAnimated from 'react-select/animated';
import Select from 'react-select';
const axios = require("axios").default;
const url = "http://localhost:5000/allExternals/";
const animatedComponents = makeAnimated();

function Card() {
  const [SelectedExaminar, setSelectedExaminar] = useState({ value: "", label: "" });
  const [SelectedDate, setSelectedDate] = useState({ value: "", label: "" });
  const [day, setDay] = useState([]);
  const [dates,setDates]=useState([]);
  const [selectedslots,setSelectedslots]=useState(Array(dates.length*15).fill(1));
  const slotOptions = [
    { value: 0, label: '1st' },
    { value: 1, label: '2nd' },
    { value: 2, label: '3rd' },
    { value: 3, label: '4th' },
    { value: 4, label: '5th' },
    { value: 5, label: '6th' },
    { value: 6, label: '7th' },
    { value: 7, label: '8th' },
    { value: 8, label: '9th' },
    { value: 9, label: '10th' },
    { value: 10, label: '11th' },
    { value: 11, label: '12th' },
    { value: 12, label: '13th' },
    { value: 13, label: '14th' },
    { value: 14, label: '15th' },
  ]
  const loadExaminars = (searchExaminar) => {
    return axios.get(url).then((res) => {
      let list = [];
      console.log(res.data);
      res.data["externals"].forEach((ex) => list.push({ value: ex, label: ex }));
      return list.filter((d) => d.label.toLowerCase().includes(searchExaminar.toLowerCase()));
    });
  };

  const loadDates = (searchDate) => {
    return axios.get(url).then((res) => {
      const exams = res.data["dates"];
      setDates(exams);
      let list = [];
      exams.forEach((ex) => list.push({ value: ex, label: ex }));
      return list.filter((d) => d.label.toLowerCase().includes(searchDate.toLowerCase()));
    });
  };

  const changeExaminar = (value) => {
    setSelectedExaminar(value);
    setSelectedslots(Array(dates.length*15).fill(1));
    setDay([])
  }

  const changeDate = (value) => {
    const tmp=dates.indexOf(SelectedDate.value)*15
    let tmplist = [...selectedslots];
    day.forEach((s) =>tmplist[tmp+s.value]=0)
    setSelectedslots(tmplist);
    setDay([])
    setSelectedDate(value)  
  }

  const handleSubmit = (event) => {
    event.preventDefault()
    const tmp=dates.indexOf(SelectedDate.value)*15
    let tmplist = [...selectedslots];
    day.forEach((s) =>tmplist[tmp+s.value]=0)
    setSelectedslots(tmplist);
    let res={};
    res[SelectedExaminar.value]=selectedslots
    axios.post('http://localhost:5000/external/',res)
    setSelectedslots(Array(dates.length*15).fill(1));
  }

  return (
    <>
      <form className={"Constarints"}>
        <div className="divTitle">Examiner's Constraints</div>
        <label className="divLabel-1">
          please select Examiner <span className="required">*</span>
        </label>
        <label className="divLabel-2">
          Choose available day <span className="required">*</span>
        </label>
        <label className="divLabel-3">
          Choose available slot <span className="required">*</span>
        </label>
        <AsyncSelect
          className="dropdown-1"
          cacheOptions
          defaultOptions
          value={SelectedExaminar}
          getOptionLabel={(e) => e.label}
          getOptionValue={(e) => e.value}
          loadOptions={loadExaminars}
          onChange={changeExaminar}
        />
        <AsyncSelect 
          className="dropdown-2" 
          cacheOptions
          defaultOptions
          value={SelectedDate}
          getOptionLabel={(e) => e.label}
          getOptionValue={(e) => e.value}
          loadOptions={loadDates}
          onChange={changeDate}
        />
        <Select
          components={animatedComponents}
          isMulti
          value={day}
          onChange={setDay}
          options={slotOptions}
        />
        <button className="btn-const" onClick={handleSubmit}>ADD</button>
      </form>
    </>
  );
}
export default Card;
