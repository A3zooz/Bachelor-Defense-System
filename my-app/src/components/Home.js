import React from "react";
import {slots_1,slots_2} from "./slots"
function Home(){
    return (
        <div>
            <form className="addForm" action="/action_page.php" method="post">
        <div className="formTitle">Schedule's Data</div>
        <label className="uploadLabel">
          Upload Excel File <span className="required">*</span>
        </label>
        <label className="info">(.xlsx, .xls, .csv)</label>
        <br></br>
        <input className="inpt" type="file" name ="ExcelFile" id = "ExcelFile" accept=".xlsx, .xls, .csv" />
        <button className="btn">Sumbit</button>
      </form>

      <form className="Constarints-1">
        <div className="divTitle">Examiners' Constraints</div>
        <label className="divLabel-1">
          please select Examiners <span className="required">*</span>
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
       {slots_1.map((slot,index) => {return(
            <div> 
          <input type="checkbox" id={slot.title+"exam"} name={slot.title}/>
          <label for={slot.title}>{slot.title}</label>
      </div>)})}
    </div>
    <div className="slots2">
       {slots_2.map((slot,index) => {return(
            <div> 
          <input type="checkbox" id={slot.title+"exam"} name={slot.title}/>
          <label for={slot.title}>{slot.title}</label>
      </div>)})}
    </div>
        <button className="btn-const">ADD</button>
      </form>

      <form className="Constarints-2">
        <div className="divTitle">Supervisors' Constraints</div>
        <label className="divLabel-1">
          please select Supervisor <span className="required">*</span>
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
       {slots_1.map((slot,index) => {return(
            <div> 
          <input type="checkbox" id={slot.title+"super"} name={slot.title}/>
          <label for={slot.title}>{slot.title}</label>
      </div>)})}
    </div>
    <div className="slots2">
       {slots_2.map((slot,index) => {return(
            <div> 
          <input type="checkbox" id={slot.title+"super"} name={slot.title}/>
          <label for={slot.title}>{slot.title}</label>
      </div>)})}
    </div>
        <button className="btn-const">ADD</button>
      </form>

      <form className="Constarints-3">
        <div className="divTitle">Students' Constraints</div>
        <label className="divLabel-1">
          please select Student <span className="required">*</span>
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
       {slots_1.map((slot,index) => {return(
            <div> 
          <input type="checkbox" id={slot.title+"student"} name={slot.title}/>
          <label for={slot.title}>{slot.title}</label>
      </div>)})}
    </div>
    <div className="slots2">
       {slots_2.map((slot,index) => {return(
            <div> 
          <input type="checkbox" id={slot.title+"student"} name={slot.title}/>
          <label for={slot.title}>{slot.title}</label>
      </div>)})}
    </div>
        <button className="btn-const">ADD</button>
      </form>

        </div>
    )
}
export default Home;