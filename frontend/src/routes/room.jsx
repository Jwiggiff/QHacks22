import { useParams, useSearchParams } from "react-router-dom";
import RoomHeader from "../_components/room/Header";
import Host from "../_components/room/Host";
import Transcript from "../_components/room/Transcript";

function Room() {
  let params = useParams();
  let [searchParams, setSearchParams] = useSearchParams();

  let host = searchParams.has("host");

  return (
    <div className="room">
      <RoomHeader roomId={params.roomId} />
      {host ? (
        <Host roomId={params.roomId} />
      ) : (
        <Transcript roomId={params.roomId} />
      )}
    </div>
  );
}

export default Room;
