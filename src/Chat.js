import React, { useState, useRef, useEffect } from 'react';
import './styles.css'; 

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
    <div className="chat" style={{ position: 'fixed', top: '160px', left: '120px', width: '700px', height: '550px', border: '1px solid #ccc', borderRadius: '5px', overflow: 'auto' }}>
      {/* 채팅 대화 내역 */}
      <div ref={messageRef} style={{ padding: '10px', paddingBottom: '0', overflowY: 'auto', height: '80%' }}>
        {messages.map((message, index) => (
          <div key={index} className={message.user === 'user' ? 'message user-message' : 'message'}>
            {message.user === 'user' && <div className="user-icon">🍩</div>}
            <div className="message-bubble">{message.content}</div>
          </div>
        ))}
      </div>
      {/* 사용자 입력창 */}
      <form onSubmit={handleMessageSubmit} style={{ borderTop: '1px solid #ccc', padding: '10px', display: 'flex' }}>
        <input type="text" name="message" placeholder="Type a message..." style={{ flex: '1', marginRight: '10px' }} />
        {/* 전송 버튼 */}
        <button type="submit" className="gradient_btn">전송</button>
      </form>
    </div>
  );
}

export default Chat;