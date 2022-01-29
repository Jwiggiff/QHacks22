import logo from "../assets/logo.png";

function Header() {
  return (
    <div className="header">
      <img className="logo" src={logo} alt="Iris" />
      <p>Translate on the go!&trade;</p>
    </div>
  );
}

export default Header;
