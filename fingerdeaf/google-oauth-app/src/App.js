// src/App.js
import React, { useState, useRef } from 'react';
import { GoogleOAuthProvider, GoogleLogin } from '@react-oauth/google';

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [user, setUser] = useState(null);
  const localVideoRef = useRef(null);
  const remoteVideoRef = useRef(null);
  const peerConnectionRef = useRef(null);

  // STUN server configuration for establishing WebRTC connections
  const iceServers = {
    iceServers: [
      { urls: 'stun:stun.l.google.com:19302' },
    ],
  };

  const handleLoginSuccess = (response) => {
    console.log('Login Success:', response);

    // Send token to your server for verification
    fetch('/auth/google', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ token: response.credential }),
    })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        setIsAuthenticated(true);
        setUser(data.user);
        console.log("User authenticated successfully:", data);
      } else {
        console.error("Authentication failed:", data.error);
      }
    })
    .catch(error => {
      console.error("Error sending token to server:", error);
    });
  };

  const handleLoginError = (error) => {
    console.error('Login Failed:', error);
  };

  const startWebRTC = async () => {
    // Create a new RTCPeerConnection
    peerConnectionRef.current = new RTCPeerConnection(iceServers);

    // Add event listener for incoming ICE candidates
    peerConnectionRef.current.onicecandidate = (event) => {
      if (event.candidate) {
        // Send ICE candidate to the other peer via your signaling server
        console.log('New ICE candidate:', event.candidate);
        // Implement signaling server communication here
      }
    };

    // Add event listener for remote streams
    peerConnectionRef.current.ontrack = (event) => {
      // Add remote stream to the video element
      remoteVideoRef.current.srcObject = event.streams[0];
    };

    try {
      // Get the user's media stream
      const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
      localVideoRef.current.srcObject = stream;

      // Add local tracks to the peer connection
      stream.getTracks().forEach(track => {
        peerConnectionRef.current.addTrack(track, stream);
      });

      // Create an offer to connect with another peer
      const offer = await peerConnectionRef.current.createOffer();
      await peerConnectionRef.current.setLocalDescription(offer);

      // Send the offer to the other peer via your signaling server
      console.log('Sending offer:', offer);
      // Implement signaling server communication here
    } catch (error) {
      console.error('Error accessing media devices.', error);
    }
  };

  return (
    <GoogleOAuthProvider clientId="YOUR_CLIENT_ID.apps.googleusercontent.com">
      <div className="App">
        <h1>Google OAuth and WebRTC in React</h1>

        {!isAuthenticated ? (
          <GoogleLogin
            onSuccess={handleLoginSuccess}
            onError={handleLoginError}
          />
        ) : (
          <div>
            <p>Welcome, {user?.name}</p>
            <button onClick={startWebRTC}>Start WebRTC</button>

            <div style={{ display: 'flex', justifyContent: 'center', marginTop: 20 }}>
              <video ref={localVideoRef} autoPlay muted style={{ width: '300px', marginRight: '10px' }}></video>
              <video ref={remoteVideoRef} autoPlay style={{ width: '300px' }}></video>
            </div>
          </div>
        )}
      </div>
    </GoogleOAuthProvider>
  );
}

export default App;
