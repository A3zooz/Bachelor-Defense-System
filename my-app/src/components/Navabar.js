import React, { Component } from "react";
import {menuItems} from "./MenuItems"
import "./Navbar.css"
class Navbar extends Component{
   render(){
    return(
      <nav className="NavbarItems">
        <h1 className="navbar-logo">Bachelor Defense Scheduler</h1>
        <ul className="nav-menu">
          {
            menuItems.map((item , index) =>{return (<li key={index}><a className={item.cName} href ={item.url}>{item.title}</a></li>)} )}

        </ul>
      </nav>
    
      )
   }
}
export default Navbar;
