// App.js

import React from 'react';
import './App.css'; 
import Chat from './Chat'; 
import Map from './Map'; 
import mainlogo from './mainlogo.png';

function App() {
  const handleLogoClick = () => {
    window.location.reload(); 
  };

  return (
    <div className="star-background"> {/* 별빛 효과 클래스 추가 */}
      <div className="app">
        <div className="mainlogo" onClick={handleLogoClick} style={{ cursor: 'pointer' }}>
          {/* 로고 이미지 */}
          <img src={mainlogo} alt="Logo" style={{ width: '250px', height: 'auto' }} />{/* 이미지 경로를 변수로 지정하여 사용합니다. */}
        </div>
        <div className="chat-container">
          {/* 채팅창 컴포넌트 */}
          <Chat />
        </div>
        <div className="map-container">
          {/* 지도 컴포넌트 */}
          <Map />
        </div>
      </div>
    </div>
  );
}

function LogoComponent() {
  const handleLogoClick = () => {
    window.location.reload(); 
  };

  return (
    <img
      src={mainlogo}
      alt="Logo"
      onClick={handleLogoClick} 
      style={{ cursor: 'pointer' }} 
    />
  );
}

export default App;