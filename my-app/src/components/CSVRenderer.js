    import React from "react";
    import { Table } from "react-bootstrap";

    // 3. create customers table component
    const CSVRenderer = ({ data }) => {
    // table header
    const TableHeader = (
        <thead className="bgvi">
        <tr>
            <th>#</th>
            <th>Examiner</th>
            <th>Supervisor</th>
            <th>Student ID</th>
            <th>Student Name</th>
            {/* <th>Student Email</th> */}
            <th>Topic</th>
            <th>Time</th>
            <th>Room</th>
            <th>Color</th>
        </tr>
        </thead>
    );

    // table row construction
    const CustomerRow = (data, index) => (
        <tr key={index} className="even">
        <td>{index + 1}</td>
        <td>{data.Examiner}</td>
        <td>{data.Supervisor}</td>
        <td>{data.Student}</td>
        <td>{data.Studentname}</td>
        {/* <td>{data.Studentemail}</td> */}
        <td>{data.Topic}</td>
        <td>{data.Time}</td>
        <td>{data.Room}</td>
        <td>{data.Color}</td>
        </tr>
    );

    // render customers's items
    const DataTable = data.map((cust, index) =>
        CustomerRow(cust, index)
    );

    return (
        <Table striped bordered hover>
        {TableHeader}
        <tbody>{DataTable}</tbody>
        </Table>
    );
    };

    export default CSVRenderer;