// signaling-server.js
const express = require('express');
const http = require('http');
const { Server } = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = new Server(server);

// Store clients
const clients = {};

io.on('connection', (socket) => {
  console.log('A user connected:', socket.id);

  // When a user joins a room
  socket.on('join', (room) => {
    if (!clients[room]) {
      clients[room] = [];
    }
    clients[room].push(socket.id);

    // Notify all clients in the room of a new peer
    io.to(room).emit('new-peer', socket.id);

    socket.join(room);
  });

  // When a user sends an offer
  socket.on('offer', (data) => {
    io.to(data.target).emit('offer', {
      sdp: data.sdp,
      from: socket.id,
    });
  });

  // When a user sends an answer
  socket.on('answer', (data) => {
    io.to(data.target).emit('answer', {
      sdp: data.sdp,
      from: socket.id,
    });
  });

  // When a user sends an ICE candidate
  socket.on('candidate', (data) => {
    io.to(data.target).emit('candidate', {
      candidate: data.candidate,
      from: socket.id,
    });
  });

  // Handle user disconnect
  socket.on('disconnect', () => {
    for (let room in clients) {
      clients[room] = clients[room].filter(client => client !== socket.id);
      if (clients[room].length === 0) {
        delete clients[room];
      }
    }
    console.log('A user disconnected:', socket.id);
  });
});

server.listen(5000, () => {
  console.log('Signaling server is running on port 5000');
});
