import React, { useState, useRef, useEffect } from 'react';
import './index.css';

function Chat() {
  const [messages, setMessages] = useState([]);
  const messageRef = useRef(null);

  useEffect(() => {
    if (messageRef.current) {
      messageRef.current.scrollTop = messageRef.current.scrollHeight;
    }
  }, [messages]);

  const handleMessageSubmit = (e) => {
    e.preventDefault();
    const newMessage = e.target.elements.message.value;
    if (newMessage.trim() !== '') {
      setMessages([...messages, { content: newMessage, user: 'user' }]);
      e.target.elements.message.value = '';
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-list">
        <div ref={messageRef}>
          {messages.map((message, index) => (
            <div key={index} className={message.user === 'user' ? 'message user-message' : 'message'}>
              {message.user === 'user' && <div className="user-icon">🍩</div>}
              <div className="message-bubble">{message.content}</div>
            </div>
          ))}
        </div>
      </div>
      {/* 사용자 입력창 */}
      <form onSubmit={handleMessageSubmit} className="chat-input">
        <input type="text" name="message" placeholder="Type a message..." />
        <button type="submit">전송</button>
      </form>
    </div>
  );
}

export default Chat;