import React, { useState } from 'react';
import axios from 'axios';
import LoadingScreen from 'react-loading-screen';
import spinner from './download.gif';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import './table.css';

const Table = () => {
  const [data, setData] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [showButton, setShowButton] = useState(true);
  const [downButton, setDownButton] = useState(false);
  const [loadingTime, setLoadingTime] = useState(null);

  const checkIterations = () => {
    console.log("innn check")
    axios
      .get('http://35.223.140.142/get_iterations/')
      .then((res) => {
        console.log(res.data)
        setLoadingTime(res.data.iterations);
      })
      .catch((error) => {
        console.error('Failed to get iterations:', error);
      });
  };

  const onGenerate = () => {
    setIsLoading(true);
    setShowButton(false);
    setDownButton(true);

    axios
      .post('http://35.223.140.142/generate/')
      .then((res) => {
        console.log(res.data[0]);
        setData(res.data[0]);
        setIsLoading(false);
      })
      .catch((error) => {
        console.error('Failed to generate:', error);
      });
  };

  const handleSubmit = (event) => {
    toast('CSV file is downloading !!!');
  };

  return (
    <div>
      {isLoading ? (
        <>
         <button className="btn-const1" onClick={checkIterations}>
              check iterations remaining
            </button>
          <p> This might take a while ~{loadingTime} mins</p>
          {/* <LoadingScreen
            loading={true}
            logoSrc={spinner}
            text={`This might take a while ~${loadingTime} mins`}
            // textStyle={{ fontSize: "2px", color: "gray" }}
          /> */}
        </>
      ) : (
        <>
          {showButton && (
            <button className="btn-const1" onClick={onGenerate}>
              Generate Solution 
            </button>
          )}

          {downButton && (
            <>
              <form action="http://35.223.140.142/downloadFile/">
                <input
                  onClick={handleSubmit}
                  className="btn-const2"
                  type="submit"
                  value="Download Solution"
                />
              </form>

              {data && (
                <table className="ArchiveTable">
                  <thead>
                    <tr>
                      <th>Examiner</th>
                      <th>Supervisor</th>
                      <th>Student</th>
                      <th>Student Name</th>
                      <th>Student Email</th>
                      <th>Topic</th>
                      <th>Time</th>
                      <th>Room</th>
                      <th>Color</th>
                    </tr>
                  </thead>
                  <tbody>
                    {data.map((data, index) => (
                      <tr key={index}>
                        <td>{data.Examiner}</td>
                        <td>{data.Supervisor}</td>
                        <td>{data.Student}</td>
                        <td>{data.Studentname}</td>
                        <td>{data.Studentemail}</td>
                        <td>{data.Topic}</td>
                        <td>{data.Time}</td>
                        <td>{data.Room}</td>
                        <td>{data.Color}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              )}

              <ToastContainer />
            </>
          )}
        </>
      )}
    </div>
  );
};

export default Table;
