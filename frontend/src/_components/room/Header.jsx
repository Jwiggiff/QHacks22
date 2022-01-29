import { Link } from "react-router-dom";
import logo from "../../assets/logo.png";

function RoomHeader(props) {
  return (
    <header className="roomHeader">
      <Link to="/">
        <img src={logo} alt="Iris" />
      </Link>
      <p>Room ID: {props.roomId}</p>
    </header>
  );
}

export default RoomHeader;
