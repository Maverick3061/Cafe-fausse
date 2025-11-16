import React from "react";
import "./menu.css";

function Menu() {
  return (
    <div className="container">
      <div className="card">
        <h2>Our Menu</h2>

        <div className="menu-section">
          <h3>Starters</h3>
          <div className="menu-item"><span>Bruschetta</span><span>$8.50</span></div>
          <div className="menu-item"><span>Caesar Salad</span><span>$9.00</span></div>
        </div>

        <div className="menu-section">
          <h3>Main Courses</h3>
          <div className="menu-item"><span>Grilled Salmon</span><span>$22.00</span></div>
          <div className="menu-item"><span>Ribeye Steak</span><span>$28.00</span></div>
          <div className="menu-item"><span>Vegetable Risotto</span><span>$18.00</span></div>
        </div>

        <div className="menu-section">
          <h3>Desserts</h3>
          <div className="menu-item"><span>Tiramisu</span><span>$7.50</span></div>
          <div className="menu-item"><span>Cheesecake</span><span>$7.00</span></div>
        </div>
      </div>
    </div>
  );
}

export default Menu;
