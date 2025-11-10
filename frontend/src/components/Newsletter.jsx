import React, { useState } from "react";
import "./Newsletter.css"; // optional styling

const Newsletter = () => {
  const [email, setEmail] = useState("");
  const [message, setMessage] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage("Processing...");

    try {
      const response = await fetch("http://127.0.0.1:5000/api/newsletter", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email }),
      });

      const data = await response.json();
      if (response.ok) {
        setMessage(`✅ ${data.message}`);
        setEmail("");
      } else {
        setMessage(`❌ ${data.error}`);
      }
    } catch (err) {
      setMessage("❌ Network error, please try again later.");
    }
  };

  return (
    <div className="newsletter-container min-h-screen flex flex-col items-center justify-center bg-gray-100 p-8">
      <h2 className="text-3xl font-bold mb-4">Subscribe to Our Newsletter</h2>
      <form onSubmit={handleSubmit} className="flex flex-col gap-4 w-full max-w-sm">
        <input
          type="email"
          placeholder="Enter your email"
          required
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="p-2 rounded border border-gray-300"
        />
        <button type="submit" className="bg-gray-800 text-white p-2 rounded hover:bg-gray-700">
          Subscribe
        </button>
      </form>
      <p className="mt-4 text-center">{message}</p>
    </div>
  );
};

export default Newsletter;
