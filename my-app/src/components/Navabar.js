import React, { Component } from "react";
import {menuItems} from "./MenuItems"
import {Link} from "react-router-dom"
import "./Navbar.css"
import logo from './Guc.png'; 

class Navbar extends Component{
  render(){
    return(
      <nav className="NavbarItems">
        <img  style={{ width: "9%", height: "96%" ,marginRight: "5%"}} src={logo}  alt="Logo" />
        <h1 className="navbar-logo">Bachelor Defense Schedule</h1>
        <ul className="nav-menu">
          {
            menuItems.map((item , index) =>{return (<li key={index}><Link to={item.url}  className={item.cName}>{item.title}</Link></li>)} )}

        </ul>
      </nav>
    
      )
  }
}
export default Navbar;
