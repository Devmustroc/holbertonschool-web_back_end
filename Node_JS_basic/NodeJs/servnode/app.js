const http =  require('http');

const SerNode = http.createServer((req, res) => {
  const url = req.url;
  if (url === '/') {
    res.setHeader('Content-Type', 'text/html');
    res.write('<html lang="en">');
    res.write('<head><title>Inter Message</title></head>');
    res.write('<body><form action="/message" method="post"><input type="text"><br><br><button type="submit">Submit</button></form></body>')
    res.write('</html>');
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
