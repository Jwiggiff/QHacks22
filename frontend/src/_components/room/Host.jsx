import { useEffect, useRef, useState } from "react";
import mic from "../../assets/mic.svg";

function Host() {
  let [btnDisabled, setBtnDisabled] = useState(true);
  let [mediaRecorder, setMediaRecorder] = useState({
    recorder: null,
  });
  let chunks = useRef([]);

  let [url, setURL] = useState();

  useEffect(() => {
    const ws = new WebSocket("ws://localhost:8001");

    navigator.mediaDevices
      .getUserMedia({ audio: true })
      .then((stream) => {
        let recorder = new MediaRecorder(stream, {
          mimeType: "audio/webm",
        });

        recorder.addEventListener("start", () => {
          console.log("start event");
        });

        recorder.addEventListener("dataavailable", (e) => {
          console.log("more data");
          chunks.current.push(e.data);
        });

        recorder.addEventListener("stop", () => {
          console.log("stop event");

          //TODO: Send audio to websocket
          ws.send({ type: "recording", audio: chunks.current[0] });

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
