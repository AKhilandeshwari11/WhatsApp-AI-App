function MessageBubble({ message, currentUser }) {
  const isSent = message.sender === currentUser;

  return (
    <div className={`message-row ${isSent ? "sent" : "received"}`}>
      <div className="message-bubble">
        <p>{message.content}</p>

        <div className="message-meta">
          <span>
            {message.timestamp
              ? new Date(message.timestamp).toLocaleTimeString([], {
                  hour: "2-digit",
                  minute: "2-digit",
                })
              : ""}
          </span>

          {isSent && (
            <span className={`status ${message.status}`}>
              {message.status === "sent" && "✓"}
              {message.status === "delivered" && "✓✓"}
              {message.status === "read" && "✓✓✓"}
            </span>
          )}
        </div>
      </div>
    </div>
  );
}

export default MessageBubble;