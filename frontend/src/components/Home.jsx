import "./Home.css";
import bg from "../assets/coffee-bg.jpg";

export default function Home() {
  return (
    <section
      className="home-hero"
      style={{ backgroundImage: `url(${bg})` }}
    >
      <div className="hero-overlay"></div>
      <div className="hero-content">
        <h1>Welcome to Café Fausse</h1>
        <p>Where aroma, artistry, and ambience blend into perfection.</p>
        <a href="/menu" className="hero-btn">Explore Menu</a>
      </div>
    </section>
  );
}
