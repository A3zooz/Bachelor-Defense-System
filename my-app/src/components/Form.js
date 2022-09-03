import React, { Component } from "react";
class Form extends Component {
    render(){
        return (
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
        )
    }
}
export default Form;