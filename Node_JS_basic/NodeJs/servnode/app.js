const http =  require('http');
const fs = require('fs');


const SerNode = http.createServer((req, res) => {
  const url = req.url;
  const method = req.method
  if (url === '/') {
    res.setHeader('Content-Type', 'text/html');
    res.write('<html lang="en">');
    res.write('<head><title>Inter Message</title></head>');
    res.write('<body><form action="/message" method="POST"><input type="text" name="message"><br><br><button type="submit">Submit</button></form></body>')
    res.write('</html>');
    return res.end()
  }
  if (url === '/message' && method === "POST")
  {
    const body = [];
    req.on('data', (chunk) => {
      console.log(chunk);
      body.push();
    });
    req.on('end', () => {
      const parsedBody = Buffer.concat(body).toString();
      console.log(parsedBody)
    });
    fs.writeFileSync('message.txt', 'Execute');
    res.statusCode = 302
    res.setHeader('Location', '/');
    return res.end()
  }
    res.setHeader('Content-Type', 'text/html');
    res.write('<html lang="en">');
    res.write('<head><title>Inter Message</title></head>');
    res.write('<body><h1>This is Node JS</h1></body>')
    res.write('</html>');
    res.end()


});

SerNode.listen(3000)
