import { useEffect, useRef, useState } from "react";
import mic from "../../assets/mic.svg";

function Host(props) {
  let [btnDisabled, setBtnDisabled] = useState(true);
  let [mediaRecorder, setMediaRecorder] = useState({
    recorder: null,
  });
  let chunks = useRef([]);

  useEffect(async () => {
    const ws = new WebSocket("ws://localhost:8001");

    ws.onopen = () => {
      // Create room
      ws.send(JSON.stringify({ type: "create_room", id: props.roomId }));
    };

    ws.onmessage = (message) => {
      console.log("Socket: ", JSON.parse(message.data));
    };

    navigator.mediaDevices
      .getUserMedia({ audio: true })
      .then((stream) => {
        let recorder = new MediaRecorder(stream, {
          mimeType: "audio/webm;codecs=pcm",
        });

        recorder.addEventListener("start", () => {
          console.log("start event");
        });

        recorder.addEventListener("dataavailable", (e) => {
          console.log("more data");
          chunks.current.push(e.data);
        });

        recorder.addEventListener("stop", async () => {
          console.log("stop event");

          const reader = new FileReader();
          reader.onload = () => {
            let event = {
              type: "recording",
              audio: reader.result.split("base64,")[1],
              time: new Date().toUTCString(),
              id: props.roomId,
            };
            ws.send(JSON.stringify(event));
          };
          reader.readAsDataURL(chunks.current[0]);

          chunks.current = [];
        });

        setMediaRecorder({
          recorder: recorder,
        });

        setBtnDisabled(false);
      })
      .catch((e) => {
        console.log("Unable to record audio :(.");
        console.error(e);
      });
  }, []);

  return (
    <>
      <div className="app">
        <h1>Hold to Record!</h1>
        <button
          id="recordBtn"
          onMouseDown={(e) =>
            e.button == 0 &&
            mediaRecorder.recorder.state == "inactive" &&
            mediaRecorder.recorder.start()
          }
          onMouseUp={(e) => e.button == 0 && mediaRecorder.recorder.stop()}
          disabled={btnDisabled}
        >
          <img src={mic} alt="Record" />
        </button>
      </div>
    </>
  );
}

export default Host;
