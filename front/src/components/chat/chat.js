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

  const handleMessageSubmit = async (e) => {
    e.preventDefault();
    const newMessage = e.target.elements.message.value;
    if (newMessage.trim() !== '') {
      const messageData = { content: newMessage, user: 'user' };
      setMessages([...messages, messageData]);

      e.target.elements.message.value = '';

      let threadId = localStorage.getItem('thread_id');

      const params = new URLSearchParams({
        thread_id: threadId || '',
        user_input: newMessage,
      });

      try {
        const response = await fetch(`http://localhost:8000/v1/gpt?${params}`, {
          method: 'GET',
        });
        if (!response.ok) throw new Error('Network response was not ok');

        const responseData = await response.json();
        const botMessage = {content: responseData.result, user: 'bot'}
        setMessages(messages => [...messages, botMessage]);

        if (responseData.thread_id && !threadId) {
          localStorage.setItem('thread_id', responseData.thread_id);
        }
      } catch (error) {
        console.error('Error fetching data: ', error);
      }
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