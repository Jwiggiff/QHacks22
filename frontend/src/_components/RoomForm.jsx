import { useNavigate } from "react-router-dom";

function RoomForm() {
  let navigate = useNavigate();

  function createRoom(e) {
    e.preventDefault();

    //TODO: Create room in database

    // Navigate to new room
    navigate("/room/xxx");
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
        <button>Join Room</button>
      </form>
    </div>
  );
}

export default RoomForm;
