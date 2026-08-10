import { useEffect, useState } from "react";
import API from "./services/api";

import Sidebar from "./components/Sidebar";
import ChatWindow from "./components/ChatWindow";
const CURRENT_USER = "9999999999";

function App() {
  const [messages, setMessages] = useState([]);
  const [selectedPhone, setSelectedPhone] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
  let isMounted = true;

  const loadMessages = async () => {
    try {
      const response = await API.get("/messages");

      if (isMounted) {
        setMessages(response.data);
        setLoading(false);
      }
    } catch (error) {
      console.error("Failed to fetch messages:", error);
    }
  };

  loadMessages();

  const interval = setInterval(loadMessages, 5000);

  return () => {
    isMounted = false;
    clearInterval(interval);
  };
}, []);
  const fetchMessages = async () => {
    try {
      const response = await API.get("/messages");
      setMessages(response.data);
    } catch (error) {
      console.error("Failed to fetch messages:", error);
    } finally {
      setLoading(false);
    }
  };

  const getConversations = () => {
  const phones = new Set();

  messages.forEach((message) => {
    if (message.sender !== CURRENT_USER) {
      phones.add(message.sender);
    }

    if (message.receiver !== CURRENT_USER) {
      phones.add(message.receiver);
    }
  });

  return Array.from(phones);
};

  const getChatMessages = () => {
    if (!selectedPhone) {
      return [];
    }

    return messages.filter(
      (message) =>
        message.sender === selectedPhone ||
        message.receiver === selectedPhone
    );
  };

  const handleSendMessage = async (content) => {
    try {
      const response = await API.post("/send-message", {
        sender: CURRENT_USER,
        receiver: selectedPhone,
        content,
        status: "sent",
      });

      setMessages((previousMessages) => [
        ...previousMessages,
        response.data,
      ]);
    } catch (error) {
      console.error("Failed to send message:", error);
    }
  };

  const conversations = getConversations();
  const chatMessages = getChatMessages();

  if (loading) {
    return <div className="loading">Loading messages...</div>;
  }

  return (
    <div className="app">
      <Sidebar
        conversations={conversations}
        selectedPhone={selectedPhone}
        onSelect={setSelectedPhone}
      />

      <ChatWindow
        phone={selectedPhone}
        messages={chatMessages}
        onSend={handleSendMessage}
        currentUser={CURRENT_USER}
      />
    </div>
  );
}

export default App;
