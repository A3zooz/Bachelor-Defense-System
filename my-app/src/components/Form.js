import React, {useState} from "react";
import DatePicker from "react-multi-date-picker"
import DatePanel from "react-multi-date-picker/plugins/date_panel"
import { Text, View, FlatList, TouchableOpacity} from 'react-native';

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
        <label className="info">(.csv)</label>
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
      <label className="roomLabel">
        Choose Rooms <span className="required">*</span>
      </label>


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

      <div style={{ display: 'flex', marginTop: '5px' }}>

      {/* <FlatList list={[1, 2, 3]} renderItem={rooms.map((item) => (
          <li key={item}>{item}</li>
        ))}/> */}
        
        <FlatList
      data={rooms}
      keyExtractor={(item, index) => index.toString()}
      contentContainerStyle={{ justifyContent: 'flex-start', flexDirection: 
      'row', flexWrap: 'wrap', paddingHorizontal: 10 }}
      renderItem={({ item }) =>
                  <TouchableOpacity style={{ padding: 10 }}>
                  <Text style={{ backgroundColor: '#edf4fa', fontSize: 15, 
                      padding: 6, borderRadius: 7 }}>{item}</Text>
                    </TouchableOpacity>

      }
  />

      </div>


    
      </div>
      <button className="btn">Submit</button>


      </form>
      
    </>
    );
  
}
export default Form;
