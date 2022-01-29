import Message from "./Message";

function Transcript() {
  let message =
    "Minim deserunt quis dolor anim nisi est in ea eiusmod laborum in excepteur adipisicing. Proident deserunt cillum deserunt nulla. Ea est sunt duis eiusmod sint ex ad amet sint pariatur qui officia elit. Nostrud irure velit consectetur minim minim magna consectetur non.";

  return (
    <div className="transcript">
      <ul>
        {Array.apply(null, Array(10)).map((_, i) => (
          <Message key={i} time={new Date()} message={message} />
        ))}
      </ul>
    </div>
  );
}

export default Transcript;
