import redis from 'redis';
import { promisify } from 'util';
const client = redis.createClient();
client.on('connect', () => console.log('Redis client connected to the server'));

const getAsync = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
  console.log(await getAsync(schoolName));
}

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');