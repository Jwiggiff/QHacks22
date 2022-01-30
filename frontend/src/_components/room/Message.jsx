import he from "he";

function Message(props) {
  return (
    <li>
      <span className="time">{new Date(props.time).toLocaleString()}</span>
      <p className="message">{he.decode(props.message)}</p>
    </li>
  );
}

export default Message;
