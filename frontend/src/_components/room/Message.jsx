function Message(props) {
  return (
    <li>
      <span className="time">{new Date(props.time).toLocaleString()}</span>
      <p className="message">{props.message}</p>
    </li>
  );
}

export default Message;
