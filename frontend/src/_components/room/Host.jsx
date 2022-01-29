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

          //TODO: Send audio to websocket
          // let audio = await new Response(chunks.current[0]).text();
          const reader = new FileReader();
          reader.onload = () => {
            console.log(reader.result);
            let event = {
              type: "recording",
              audio: reader.result.split("base64,")[1],
            };
            ws.send(JSON.stringify(event));
          };
          reader.readAsDataURL(chunks.current[0]);

          console.log(audio);
          // let event = { type: "recording", audio: btoa(chunks.current[0]) };
          // ws.send(JSON.stringify(event));

          setURL(URL.createObjectURL(chunks.current[0]));

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
        <audio controls src={url}></audio>
      </div>
    </>
  );
}

export default Host;
