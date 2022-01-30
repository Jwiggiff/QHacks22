import copyImg from "../../assets/copy.svg";

function CopyButton(props) {
  return (
    <button title="Copy Room URL" id="copyBtn" onClick={() => navigator.clipboard.writeText(props.text)}>
      <img src={copyImg} alt="Copy Invite Link" />
    </button>
  );
}

export default CopyButton;
