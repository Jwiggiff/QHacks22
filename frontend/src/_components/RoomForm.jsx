import { useNavigate } from "react-router-dom";
import { nanoid } from "nanoid";
import langs from "../assets/langs.json";

function RoomForm() {
  let navigate = useNavigate();

  function createRoom(e) {
    e.preventDefault();

    // Generate random room code
    let roomCode = nanoid();

    // Navigate to new room
    navigate(`/room/${roomCode}?host`);
  }

  function joinRoom(e) {
    e.preventDefault();
    let formData = new FormData(e.target);
    let roomId = formData.get("code");
    let lang = formData.get("lang");

    // Navigate to room
    navigate(`/room/${roomId}?lang=${lang}`);
  }

  return (
    <div className="roomForm">
      <form onSubmit={createRoom} id="createForm">
        <button>Create Room</button>
      </form>
      <div className="seperator">Or</div>
      <form onSubmit={joinRoom} id="joinForm">
        <input type="text" name="code" placeholder="Room Code" />
        <select name="lang">
          {langs.map((lang) => (
            <option key={lang.language_code} value={lang.language_code}>
              {lang.display_name}
            </option>
          ))}
        </select>
        <button>Join Room</button>
      </form>
    </div>
  );
}

export default RoomForm;
