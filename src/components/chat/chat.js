import React, { useState, useRef, useEffect } from 'react';
import './index.css';

function Chat() {
  const [messages, setMessages] = useState([]);
  const [showPrompt, setShowPrompt] = useState(true);
  const [showChatList, setShowChatList] = useState(false);
  const [slideDown, setSlideDown] = useState(false);
  const messageRef = useRef(null);
  const inputRef = useRef(null);

  useEffect(() => {
    if (messageRef.current) {
      messageRef.current.scrollTop = messageRef.current.scrollHeight;
    }
  }, [messages]);

  const handleMessageSubmit = (e) => {
    e.preventDefault();
    const newMessage = e.target.elements.message.value.trim();
    if (newMessage !== '') {
      setSlideDown(true); // 입력창이 아래로 슬라이딩되도록 설정

      setTimeout(() => {
        const userMessage = { content: newMessage, user: 'user' };
        setMessages(prevMessages => [...prevMessages, userMessage]);

        let responseMessage;
        if (newMessage.includes('음식점')) {
          responseMessage = { content: '음식점을 찾으시나요?', user: 'bot' };
        } else {
          responseMessage = { content: '죄송합니다. 이해하지 못했어요.', user: 'bot' };
        }
        
        setMessages(prevMessages => [...prevMessages, responseMessage]);
        
        e.target.elements.message.value = '';
        setShowPrompt(false);
        setShowChatList(true);
      }, 200); // 0.2초 지연 후 메시지 처리
    }
  };

  return (
    <div className="chat-container">
      {showPrompt && (
        <div className="title">
          <h1>어떤 음식점을 찾고 계신가요?</h1>
        </div>
      )}
      {showChatList && (
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
      )}
      <form onSubmit={handleMessageSubmit} className={`chat-input ${slideDown ? 'slide-down' : ''}`}>
        <input
          ref={inputRef}
          type="text"
          name="message"
          placeholder="원하는 맛집으로 이동해보세요"
        />
      </form>
    </div>
  );
}

export default Chat;