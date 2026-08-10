import ChatHeader from "./ChatHeader";
import MessageBubble from "./MessageBubble";
import MessageInput from "./MessageInput";

function ChatWindow({
  phone,
  messages,
  onSend,
  currentUser,
}) {
  if (!phone) {
    return (
      <div className="chat-window empty-chat">
        <h2>WhatsApp Dashboard</h2>
        <p>Select a conversation to start chatting</p>
      </div>
    );
  }

  return (
    <div className="chat-window">
      <ChatHeader phone={phone} />

      <div className="messages-container">
        {messages.length === 0 ? (
          <div className="no-messages">
            <p>No messages yet</p>
          </div>
        ) : (
          messages.map((message) => (
            <MessageBubble
              key={message.id}
              message={message}
              currentUser={currentUser}
            />
          ))
        )}
      </div>

      <MessageInput
        onSend={onSend}
        disabled={!phone}
      />
    </div>
  );
}

export default ChatWindow;