import { useNavigate } from "react-router-dom";
import { v4 as uuidv4 } from "uuid";

function RoomForm() {
  let navigate = useNavigate();

  function createRoom(e) {
    e.preventDefault();

    // Generate random room code
    let roomCode = uuidv4();

    // Navigate to new room
    navigate(`/room/${roomCode}?host`);
  }

  function joinRoom(e) {
    e.preventDefault();
    let roomId = new FormData(e.target).get("code");

    // Navigate to room
    navigate(`/room/${roomId}`);
  }

  return (
    <div className="roomForm">
      <form onSubmit={createRoom} id="createForm">
        <button>Create Room</button>
      </form>
      <div className="seperator">Or</div>
      <form onSubmit={joinRoom} id="joinForm">
        <input type="text" name="code" placeholder="Room Code" />
        {/* <select name="lang">
          <option value=""></option>
        </select> */}
        <button>Join Room</button>
      </form>
    </div>
  );
}

export default RoomForm;
