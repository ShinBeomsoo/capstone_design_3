import React, { useEffect } from "react";

const { kakao } = window;

function Kakao() {
  useEffect(() => {
    const container = document.getElementById('map');
    const options = {
      center: new kakao.maps.LatLng(33.450701, 126.70667),
      level: 3
    };
    const map = new kakao.maps.Map(container, options);
  }, []);

  return (
    <div className="map-container kakao">
      <div id="map" style={{ width: '600px', height: '600px' }}></div>
    </div>
  );
}

export default Kakao;