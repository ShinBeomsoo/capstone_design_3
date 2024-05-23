import React from 'react';
import './App.css';
import mainLogo from './assets/mainlogo.png';
import Kakao from './components/map/kakao';
import Chat from './components/chat/chat';

function App() {
  return (
    <div className="app">
      <img className="logo" src={mainLogo} alt="Logo" />
      <div className="container">
        <Chat />
        <Kakao className="kakao" />
      </div>
    </div>
  );
}

export default App;