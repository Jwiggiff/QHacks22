import logo from "../assets/logo.png";

function Header() {
  return (
    <div className="header">
      <img className="logo" src={logo} alt="Iris" />
      <p>Bridging Language Barriers&trade;</p>
    </div>
  );
}

export default Header;
