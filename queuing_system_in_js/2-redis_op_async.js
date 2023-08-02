import { createClient, print } from "redis";
import { promisify } from "util";

const client = createClient();

client.on('error', err => {
    console.log('Redis client not connected to the server:', err)
});

client.on('connect', () => {
    console.log('Redis client connected to the server')
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (error, reply) => {
        print('reply: ' + reply);
    });
}

const get = promisify(client.get).bind(client);

function displaySchoolValue (schoolName) {
    client.get(schoolName, (error, reply) => {
        console.log(reply)
    })
}

(async () => {
    displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    displaySchoolValue('HolbertonSanFrancisco');
})();