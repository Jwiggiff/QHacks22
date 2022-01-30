import { useEffect, useState } from "react";
import Loader from "./Loader";
import Message from "./Message";

function Transcript(props) {
  let [transcriptions, setTranscriptions] = useState([]);
  let [loading, setLoading] = useState(false);

  useEffect(() => {
    const ws = new WebSocket("ws://localhost:8001");

    ws.onopen = () => {
      // Join room
      ws.send(JSON.stringify({ type: "join_room", id: props.roomId }));
    };

    ws.onmessage = (message) => {
      console.log("Socket: ", JSON.parse(message.data));
      let msg = JSON.parse(message.data);
      if (msg.type == "transcription") {
        setLoading(false);
        setTranscriptions(
          transcriptions.concat({ text: msg.message, time: msg.time })
        );
      } else if (msg.type == "loading") setLoading(true);
    };
  });

  return (
    <div className="transcript">
      <ul>
        {transcriptions.map((transcription, i) => (
          <Message
            key={i}
            time={transcription.time}
            message={transcription.text}
          />
        ))}
        {loading ? <Loader /> : null}
      </ul>
    </div>
  );
}

export default Transcript;
