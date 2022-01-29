function Message(props) {
  return (
    <li>
      <span className="time">{props.time.toLocaleString()}</span>
      <p className="message">{props.message}</p>
    </li>
  );
}

export default Message;
