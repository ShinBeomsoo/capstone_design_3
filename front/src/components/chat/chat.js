import React, { useState, useRef, useEffect } from 'react';
import Typewriter from 'typewriter-effect';
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

  const handleMessageSubmit = async (e) => {
    e.preventDefault();
    const newMessage = e.target.elements.message.value;
    if (newMessage.trim() !== '') {
      setSlideDown(true);
      let threadId = localStorage.getItem('thread_id');
      const params = new URLSearchParams({
        thread_id: threadId || '',
        user_input: newMessage,
      });

      setTimeout(async () => {
        const userMessage = { content: newMessage, user: 'user' };
        setMessages(prevMessages => [...prevMessages, userMessage]);

        try {
          const response = await fetch(`http://localhost:8000/v1/gpt?${params}`, {
            method: 'GET',
          });
          if (!response.ok) throw new Error('Network response was not ok');

          const responseData = await response.json();
          const botMessage = { content: responseData.result, user: 'bot' }
          setMessages(messages => [...messages, botMessage]);

          if (responseData.thread_id && !threadId) {
            localStorage.setItem('thread_id', responseData.thread_id);
          }
        } catch (error) {
          console.error('Error fetching data: ', error);
        } finally {
          console.log("finally ")
          //   // setIsLoading(false);
        }
        e.target.elements.message.value = '';
        setShowPrompt(false);
        setShowChatList(true);
      })
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
        <div className="chat-list" ref={messageRef}>
          {messages.map((message, index) => (
            <div key={index} className={message.user === 'user' ? 'message user-message' : 'message'}>
              {message.user === 'user' && <div className="user-icon">🍩</div>}
              <div className="message-bubble">
                {message.user === 'bot' ? (
                  <Typewriter
                    options={{
                      strings: message.content,
                      autoStart: true,
                      delay: 50,
                    }}
                  />
                ) : (
                  message.content
                )}
              </div>
            </div>
          ))}
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