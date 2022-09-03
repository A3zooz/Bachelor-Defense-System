import React from "react";
function Home(){
    return (
        <div>
            <form className="addForm" method="post">
        <div className="formTitle">Schedule's Data</div>
        <label className="uploadLabel">
          Upload Excel File <span className="required">*</span>
        </label>
        <label className="info">(.xlsx, .xls, .csv)</label>
        <br></br>
        <input className="inpt" type="file" accept=".xlsx, .xls, .csv" />
        <button className="btn">Create</button>
      </form>

      <form className="Constarints-1">
        <div className="divTitle">Examiners' Constraints</div>
        <label className="divLabel">
          please select Examiners <span className="required">*</span>
        </label>
        <select className="dropdown">
          <option value="volvo">##</option>
        </select>
        <button className="btn-const">ADD</button>
      </form>

      <form className="Constarints-2">
        <div className="divTitle">Supervisors' Constraints</div>
        <label className="divLabel">
          please select Supervisor <span className="required">*</span>
        </label>
        <select className="dropdown">
          <option value="volvo">##</option>
        </select>
        <button className="btn">ADD</button>
      </form>

      <form className="Constarints-3">
        <div className="divTitle">Students' Constraints</div>
        <label className="divLabel">
          please select Student <span className="required">*</span>
        </label>
        <select className="dropdown">
          <option value="volvo">##</option>
        </select>
        <button className="btn-const">ADD</button>
      </form>

        </div>
    )
}
export default Home;