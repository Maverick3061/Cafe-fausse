import { Link } from "react-router-dom";
import "./Navbar.css";

export default function Navbar() {
  return (
    <nav className="navbar">
      <div className="nav-logo">
        Café <span>Fausse</span>
      </div>

      <ul className="nav-links">
        <li><Link to="/">Home</Link></li>
        <li><Link to="/menu">Menu</Link></li>
        <li><Link to="/reservations">Reservations</Link></li>
        <li><Link to="/gallery">Gallery</Link></li>
        <li><Link to="/about">About</Link></li>
        <li><Link to="/newsletter">Newsletter</Link></li>
      </ul>
    </nav>
  );
}
