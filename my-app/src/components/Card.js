import React from "react";
import { items } from "./cardItems";
import { slots_1, slots_2 } from "./slots";
import { useState } from "react";

function Card() {
  const getInitialState = () => {
    const inst = "NoExaminer";
    return inst;
  };
  const getInitialState2 = () => {
    const day  = "NoDay";
    return day;
  };
  const [inst, setInst] = useState(getInitialState);
  const handleChange = (e) => { setInst(e.target.value); };
  const [day, setDay] = useState(getInitialState2);
  const handleChange2 = (e) => { setDay(e.target.value); };
  const [check ,setCheck]=useState([]);
  const handleChange3=(e)=>{setCheck(arr => [...arr,e.target.value])}
  return (
    <>
      {items.map((item, index) => {
        return (
          <form key={index} className={"Constarints-" + item.Num}>
            <div className="divTitle">{item.title + "'s Constraints"}</div>
            <label className="divLabel-1">
              please select {item.title} <span className="required">*</span>
            </label>
            <label className="divLabel-2">
              Choose non available day <span className="required">*</span>
            </label>
            <label className="divLabel-3">
              Choose non available slot <span className="required">*</span>
            </label>
            <select value={inst} onChange={handleChange} key = {index} className="dropdown-1">
            <option value="-">-</option>
            <option value="ahmed">ahmed</option>
            </select>
            <select value={day} onChange={handleChange2} key = {index} className="dropdown-2">
              <option value="-">-</option>
              <option value="date">17/3/2001</option>
            </select>
            <div className="slots1">
              {slots_1.map((slot, index) => {
                return (
                  <div key={index}>
                    <input
                      type="checkbox"
                      name={slot.title}
                      value={slot.title}
                      onChange={handleChange3}
                    />
                    <label >{slot.title}</label>
                  </div>
                );
              })}
            </div>
            <div className="slots2">
              {slots_2.map((slot, index) => {
                return (
                  <div key={index}>
                    <input
                      type="checkbox"
                      name={slot.title}
                    />
                    <label >{slot.title}</label>
                  </div>
                );
              })}
            </div>
            <p>{`You selected ${day} +${inst}+${check} `}</p>
            <button className="btn-const">ADD</button>
          </form>
        );
      })}
    </>
  );
}
export default Card;
