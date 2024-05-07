import { createClient } from 'redis';

const client = createClient();

client.on('error', err => {
  console.log(`Redis client not connected to the server: ${err}`)
});
client.on('connect', () => {
  console.log('Redis client connected to the server')
});

const channelName = 'holberton school channel';

client.subscribe(channelName);

client.on('message', (channel, message) => {
  if (message === 'KILL_SERVER') {
    client.unsubscribe(channelName);
    client.quit();
  }
  console.log(message);
});
