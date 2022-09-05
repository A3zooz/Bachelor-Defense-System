import React from "react";
import "./MyConstraints.css";
function MyConstraints() {
  return (
    <form className="myConst">
      <div className="divTitle">Added Constraints</div>
      <table>
        <tr>
          <th>Name</th>
          <th>role</th>
          <th>Non-available day</th>
          <th>Non-available slot</th>
          <th></th>
        </tr>
        <tr>
          <td>Hossam shehata shalaby Elfar</td>
          <td>Student</td>
          <td>4 july - 7 August </td>
          <td>1st slot</td>
          <td>
            <button className="del">Delete</button>
          </td>
        </tr>
      </table>
    </form>
  );
}
export default MyConstraints;
