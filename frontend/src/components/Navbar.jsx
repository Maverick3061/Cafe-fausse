import React from "react";
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <header className="header">
      <div className="brand">Café Fausse</div>
      <nav>
        <Link to="/">Home</Link>
        <Link to="/menu">Menu</Link>
        <Link to="/reservations">Reservations</Link>
        <Link to="/about">About</Link>
        <Link to="/gallery">Gallery</Link>
        <Link to="/newsletter">Newsletter</Link>
      </nav>
    </header>
  );
}

export default Navbar;
