import React from "react";
import "../components/aboutus.css";
import owner1 from "../assets/owner1.jpg";
import owner2 from "../assets/owner2.jpg";

function AboutUs() {
  return (
    <div className="about-container">
      <section className="intro-section">
        <h2>About Café Fausse</h2>
        <p>
          Welcome to <strong>Café Fausse</strong>, where passion meets flavor.
          Established with a love for artisanal coffee and gourmet cuisine,
          Café Fausse offers a cozy escape from the everyday rush. Whether
          you're here for a morning espresso or an evening dessert, every cup
          and plate tells a story of craftsmanship and care.
        </p>
      </section>

      <section className="owners-section">
        <h3>Meet the Founders</h3>
        <div className="owners-grid">
          <div className="owner-card">
            <img src={owner1} alt="Owner 1" className="owner-image" />
            <h4>Alizay</h4>
            <p>
              Alizay is the visionary behind Café Fausse’s concept. With a
              background in culinary arts and a deep appreciation for
              hospitality, she ensures every guest feels like family.
            </p>
          </div>

          <div className="owner-card">
            <img src={owner2} alt="Owner 2" className="owner-image" />
            <h4>Amir</h4>
            <p>
              Amir curates the café’s unique ambiance and oversees quality.
              His dedication to excellence is reflected in every corner of
              Café Fausse — from the décor to the last sip of coffee.
            </p>
          </div>
        </div>
      </section>
    </div>
  );
}

export default AboutUs;
