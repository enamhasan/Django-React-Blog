import react from 'react';
import { Nav, Navbar, NavDropdown } from 'react-bootstrap';
import {NavLink} from 'react-router-dom';
import logo from '../static/logo.png';
import "../App.css";


const Navigation = () => {
return (
<nav className="navbar navbar-expand-lg navbar-light bg-light">
  <link className="navbar-brand" to='/'>Navbar</link>
  <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
    <span className="navbar-toggler-icon"></span>
  </button>

  <div className="collapse navbar-collapse" id="navbarNavDropdown">
    <ul className="navbar-nav">
      <li className="nav-item active">
        <link className="nav-link" to='/'>Home <span className="sr-only">(current)</span></link>
      </li>
      <li className="nav-item">
        <link className="nav-link" to='/' >Features</link>
      </li>
      <li className="nav-item">
        <link className="nav-link" to='/' >Pricing</link>
      </li>
      <li className="nav-item dropdown">
        <link className="nav-link dropdown-toggle" to='/' id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          Dropdown link
        </link>
        <div className="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
          <link className="dropdown-item" to='/'>Action</link>
          <a className="dropdown-item" to='/'>Another action</a>
          <a className="dropdown-item" to='/'>Something else here</a>
        </div>
      </li>
    </ul>
  </div>
</nav>
);
};

export default Navigation;