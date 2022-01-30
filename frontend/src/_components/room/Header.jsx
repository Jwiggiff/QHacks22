import { Link } from "react-router-dom";
import logo from "../../assets/logo.png";
import CopyButton from "./CopyButton";

function RoomHeader(props) {
  return (
    <header className="roomHeader">
      <Link to="/">
        <img src={logo} alt="Iris" />
      </Link>
      <p>
        {" "}
        <CopyButton
          text={window.location.host + `/rooms/${props.roomId}`}
        />{" "}
        Room ID: {props.roomId}
      </p>
    </header>
  );
}

export default RoomHeader;
