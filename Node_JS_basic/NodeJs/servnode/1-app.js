const http = require('http');
const fs = require('fs');
const buffer = require('buffer');


const appServer = http.createServer((req, res) => {
  const method = req.method;
  const url = req.url;

  if (url === "/") {
    res.setHeader('Content-Type', 'text/html');
    res.write('<html lang="en">');
    res.write('<head><title>This is NodeJS</title></head>');
    res.write('<body><form action="/message" method="POST"><input type="text" name="message"><button type="submit">Send</button></form></body>');
    res.write('</html>');
    return res.end();
  }
  if (url === '/message' && method === "POST") {
    const body = [];
    req.on('data', (chuck) => {
      body.push(chuck)
    });
    return req.on('end', () => {
      const parseBody = Buffer.concat(body).toString();
      const message = parseBody.split('=')[1];
      fs.writeFile('message.txt', `${message}`, err => {
        res.statusCode = 302;
        res.setHeader('Location', '/');
        return res.end();
      });
    });
  }
  res.setHeader('Content-Type', 'text/html')
  res.write('<html lang="en">');
  res.write('<head><title>This is NodeJS</title></head>');
  res.write('<body><h1>NodeJS is Connected</h1></body>');
  res.write('</html>');
  res.end();
});
appServer.listen(1254);
