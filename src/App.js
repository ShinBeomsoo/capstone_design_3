import React, { useState, useEffect } from 'react';
import './App.css'; 
import Chat from './Chat'; 
import Map from './Map'; 
import mainlogo from './mainlogo.png';
import Kakao from './Kakao'; 
import robotGif from './로봇.gif'; // 로봇 GIF 이미지를 import

function App() {
  const [logoVisible, setLogoVisible] = useState(false);
  const [chatVisible, setChatVisible] = useState(false);

  useEffect(() => {
    // 페이지 로딩 후 0.5초 뒤에 로고를 보이도록 설정
    const logoTimeout = setTimeout(() => {
      setLogoVisible(true);
    }, 500);

    // 페이지 로딩 후 0.5초 뒤에 채팅창을 보이도록 설정
    const chatTimeout = setTimeout(() => {
      setChatVisible(true);
    }, 500);

    return () => {
      clearTimeout(logoTimeout); // 로고 타임아웃 클리어
      clearTimeout(chatTimeout); // 채팅창 타임아웃 클리어
    };
  }, []);

  const handleLogoClick = () => {
    window.location.reload(); 
  };

  return (
    <div className="app">
      <div className={`mainlogo ${logoVisible ? 'fade-in-slide' : ''}`} onClick={handleLogoClick} style={{ cursor: 'pointer' }}>
        {/* 로고 이미지 */}
        <img src={mainlogo} alt="Logo" style={{ width: '160px', height: 'auto' }} />
      </div>
      <div className={`chat-container ${chatVisible ? 'fade-in-slide' : ''}`}>
        {/* 채팅창 컴포넌트 */}
        <Chat />
      </div>
      <div className="map-container">
        {/* 카카오지도 컴포넌트 */}
        <Kakao />
      </div>
      <div className="robot-container">
        {/* 로봇 GIF 이미지 */}
        <img src={robotGif} alt="Robot" style={{ width: '120px', height: 'auto' }} />
      </div>
    </div>
  );
}

export default App;