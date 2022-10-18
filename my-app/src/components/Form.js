import React, {useState} from "react";
import DatePicker from "react-multi-date-picker"
import DatePanel from "react-multi-date-picker/plugins/date_panel"
const axios = require('axios').default;

function Form() {
  const[file ,setFile ]= useState();
  const[dates ,setDates ]= useState([]);
  const[rooms ,setRooms ]= useState([]);
  const[room ,setRoom ]= useState('');
  const handleChange = (event)=> {
    setFile(event.target.files[0]);
  }
  const handleSumbit = (event)=> {
    event.preventDefault();
    const url = 'http://localhost:5000/upload-file/';
    const formData = new FormData();
    formData.append('File',file);
    formData.append('Dates',dates);
    formData.append('Rooms',rooms);
    console.log(formData.get('File'))
    axios.post(url,formData).then((response) => {
      console.log(response.data);
    });
  }
    return (
      <>
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
      <label className="dateLabel">
        Choose Dates <span className="required">*</span>
      </label>
      <div className='datePicker'>
        <DatePicker
        multiple
        value={dates}
        onChange={ setDates }
        sort
        plugins={[
          <DatePanel />
      	]}
        ></DatePicker>
      </div>
      <div className="room">
      <div>
        <input type="text" value={room} onChange={(event) => {
    setRoom(event.target.value);
  }} />
        <button type="button" onClick={() => {
    const newList = rooms.concat(room);

    setRooms(newList);
  }}>
          Add
        </button>
      </div>

      <ul>
        {rooms.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
    </div>
      <button className="btn">Submit</button>
      </form>
    </>
    );
  
}
export default Form;
