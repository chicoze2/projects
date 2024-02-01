import express from 'express';
import mongoose from 'mongoose';
import http from 'node:http';
import path from 'node:path';
import { Server } from 'socket.io';

import { router }  from './router';

const app = express();
const server = http.createServer(app);
export const io = new Server(server);

io.on('connect', () => {
  // console.log('conectou')
})

app.use((req, res, next) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', '*');
  res.setHeader('Access-Control-Allow-Headers', '*');

  next();
});

app.use('/uploads', express.static(path.resolve(__dirname, '..', 'uploads')));
app.use(express.json());
app.use(router);

mongoose.connect('mongodb://localhost:27017')
  .then(() => {

    server.listen(3000, '192.168.1.100' ,() => {
      console.log('👂 listening on http://192.168.1.100:3000');
    });


  });

