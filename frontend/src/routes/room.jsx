import { useParams } from "react-router-dom";
import RoomHeader from "../_components/room/Header";
import Transcript from "../_components/room/Transcript";

function Room() {
  let params = useParams();

  return (
    <div className="room">
      <RoomHeader roomId={params.roomId} />
      <Transcript />
    </div>
  );
}

export default Room;
