import React from "react";
import Navbar from "./components/Navabar.js";
import "./App.css";
function App() {
  return (
    <div className="container">
      <div className="App">
        <Navbar />{" "}
      </div>
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

      <form className="myConst">
        <div className="divTitle">Added Constraints</div>
        <table>
          <tr>
            <th>Name</th>
            <th>role</th>
            <th>constraint</th>
            <th></th>
          </tr>
          <tr>
            <td>Hossam shehata shalaby Elfar</td>
            <td>Student</td>
            <td>4 july - 7 August </td>
            <td><button className="del">Delete</button></td>
          </tr>
        </table>
      </form>
    </div>
  );
}
export default App;
