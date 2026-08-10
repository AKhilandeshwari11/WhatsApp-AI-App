function Sidebar({ conversations, selectedPhone, onSelect }) {
  return (
    <div className="sidebar">
      <div className="sidebar-header">
        <h2>WhatsApp</h2>
      </div>

      <div className="conversation-list">
        {conversations.map((phone) => (
          <div
            key={phone}
            className={`conversation ${
              selectedPhone === phone ? "active" : ""
            }`}
            onClick={() => onSelect(phone)}
          >
            <div className="avatar">
              {phone.slice(-2)}
            </div>

            <div className="conversation-info">
              <h3>{phone}</h3>
              <p>Messages</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Sidebar;