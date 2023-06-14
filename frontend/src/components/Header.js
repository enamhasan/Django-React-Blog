import React from 'react';
import { Link, NavLink } from 'react-router-dom';
import logo from '../static/logo.png';
import "../App.css";

const header = () => (
    <header>
      <div className="top-bar text-center">
			<div className="inside-top-bar grid-container">
			    <p className="topbar-content m-0">Announcement</p>
			</div>
	</div>
    <div className="site-header">
    <div className="header-wrapper container">
    <nav className="navbar navbar-expand-lg navbar-light">
        <Link className="navbar-brand" to='/'><img src={logo} className="logo" alt="logo" /></Link>
        <button
            className="navbar-toggler"
            type="button"
            data-toggle="collapse"
            data-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
        >
            <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
                <li className="nav-item active">
                    <NavLink className="nav-link" exact to='/'>Home <span className="sr-only">(current)</span></NavLink>
                </li>
                 <li className="nav-item">
                    <NavLink className="nav-link" exact to='blog/'>Blogs</NavLink>
                </li>
                 <li className="nav-item">
                    <NavLink className="nav-link" exact to='about'>About</NavLink>
                </li>
                 <li className="nav-item">
                    <NavLink className="nav-link" exact to='test'>Test</NavLink>
                </li>

            </ul>
        </div>

    </nav>
    </div>
     </div>
    </header>
);


export default header;