import React, {useState} from "react";
import axios from 'axios'
import writeXlsxFile from 'write-excel-file'
function Form() {
  const[file ,setFile ]= useState();
  const handleChange = (event)=> {
     setFile(event.target.files[0]);
  }
  const handleSumbit = (event)=> {
     event.preventDefault();
     const url = 'http://localhost:5000/upload-file';
     const formData = new FormData();
     formData.append('File',file);
     console.log(formData.get('File'))
     const config = {
      headers: {
        'content-type': 'multipart/form-data',
      },
    };
     axios.post(url,formData,config).then((response) => {
      console.log(response.data);
    });
    
  }
    return (
      <form className="addForm" onSubmit={handleSumbit}>
        <div className="formTitle">Schedule's Data</div>
        <label className="uploadLabel">
          Upload Excel File <span className="required">*</span>
        </label>
        <label className="info">(.xlsx, .xls, .csv)</label>
        <br></br>
        <input
          className="inpt"
          type="file"
          name = "file"
          onChange={handleChange}
          accept=".xlsx, .xls, .csv"
        />
        <button className="btn">Sumbit</button>
      </form>
    );
  
}
export default Form;
