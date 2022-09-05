import React from "react";
import { items } from "./cardItems";
import { slots_1, slots_2 } from "./slots";
function Card() {
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
            <select className="dropdown-1">
              <option value="volvo">##</option>
            </select>
            <select className="dropdown-2">
              <option value="volvo">17/3/2022</option>
            </select>
            <div className="slots1">
              {slots_1.map((slot, index) => {
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
            <button className="btn-const">ADD</button>
          </form>
        );
      })}
    </>
  );
}
export default Card;
