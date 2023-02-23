try {
  // Get the IP addresses using WebRTC
  window.RTCPeerConnection = window.RTCPeerConnection || window.webkitRTCPeerConnection || window.mozRTCPeerConnection;
  var pc = new RTCPeerConnection({iceServers:[]}), noop = function(){};
  pc.createDataChannel('');
  pc.createOffer(pc.setLocalDescription.bind(pc), noop);
  pc.onicecandidate = function(ice){
    if(!ice || !ice.candidate || !ice.candidate.candidate)  return;
    var ip = /(?<=ip\s)(.+?)(?=\|)/gi.exec(ice.candidate.candidate)[0];
    alert(ip);
    pc.onicecandidate = noop;
  };
} catch (e) {
  alert("Ошибка: " + e.message);
}
