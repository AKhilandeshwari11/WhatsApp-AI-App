import { useState } from "react";

function MessageInput({ onSend, disabled }) {
  const [content, setContent] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!content.trim() || disabled) {
      return;
    }

    onSend(content.trim());
    setContent("");
  };

  return (
    <form className="message-input" onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Type a message..."
        value={content}
        onChange={(e) => setContent(e.target.value)}
        disabled={disabled}
      />

      <button type="submit" disabled={disabled || !content.trim()}>
        Send
      </button>
    </form>
  );
}

export default MessageInput;