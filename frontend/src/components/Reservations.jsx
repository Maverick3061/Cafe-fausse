import React, { useState } from "react";
import "./reservations.css";

function Reservations() {
  const [form, setForm] = useState({
    name: "",
    email: "",
    phone: "",
    guests: 1,
    time_slot: ""
  });
  const [message, setMessage] = useState("");

  const handleChange = (e) => {
    const { name, value } = e.target;
    setForm((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage("Submitting...");

    try {
      const response = await fetch("http://127.0.0.1:5000/api/reservations"
, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form)
      });

      let data;
      try {
        data = await response.json();
      } catch {
        data = { error: "Invalid response from server" };
      }

      if (!response.ok) {
        setMessage(`Error: ${data.error || "Unknown error"}`);
      } else {
        setMessage(
          `Success! Your table number is ${data.table_number} at ${new Date(
            data.time_slot
          ).toLocaleString()}`
        );
        setForm({ name: "", email: "", phone: "", guests: 1, time_slot: "" });
      }
    } catch (err) {
      setMessage(`Error: ${err.message}`);
    }
  };

  return (
    <div className="reservation-form">
      <h2>Make a Reservation</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" name="name" placeholder="Your Name" value={form.name} onChange={handleChange} required />
        <input type="email" name="email" placeholder="Email" value={form.email} onChange={handleChange} required />
        <input type="text" name="phone" placeholder="Phone (optional)" value={form.phone} onChange={handleChange} />
        <input type="number" name="guests" min="1" max="20" value={form.guests} onChange={handleChange} />
        <input type="datetime-local" name="time_slot" value={form.time_slot} onChange={handleChange} required />
        <button type="submit">Reserve</button>
      </form>
      {message && <p className="message">{message}</p>}
    </div>
  );
}

export default Reservations;
