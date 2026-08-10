function ChatHeader({ phone }) {
  return (
    <div className="chat-header">
      <div className="chat-avatar">
        {phone ? phone.slice(-2) : "WA"}
      </div>

      <div>
        <h3>{phone || "Select a conversation"}</h3>
        <p>{phone ? "online" : "WhatsApp Dashboard"}</p>
      </div>
    </div>
  );
}

export default ChatHeader;