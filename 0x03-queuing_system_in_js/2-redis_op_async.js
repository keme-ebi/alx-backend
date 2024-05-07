import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('error', err => {
  console.log(`Redis client not connected to the server: ${err}`)
});
client.on('connect', () => {
  console.log('Redis client connected to the server')
});

const get = promisify(client.get).bind(client);

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  try {
    const value = await get(schoolName);
    console.log(`${value}`);
  } catch (err) {
    console.error(`Error: ${err}`);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
