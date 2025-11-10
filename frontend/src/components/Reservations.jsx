import React, { useState } from "react";
import "../styles/reservations.css";

function Reservations() {
  const [form, setForm] = useState({
    name: "",
    email: "",
    guests: "",
    time: "",
  });
  const [message, setMessage] = useState("");

  const handle
