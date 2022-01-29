import { useParams } from "react-router-dom";
import RoomHeader from "../_components/room/Header";
import Host from "../_components/room/Host";
import Transcript from "../_components/room/Transcript";

function Room() {
  let params = useParams();

  let host = true;

  return (
    <div className="room">
      <RoomHeader roomId={params.roomId} />
      {host ? <Host /> : <Transcript />}
    </div>
  );
}

export default Room;
