// Map.js

import React from 'react';
import seoulMap from './map.png'; 

function Map() {
  return (
    <div className="map">
      {/* 지도 이미지 */}
      <img src={seoulMap} alt="Seoul Map" />
    </div>
  );
}

export default Map;