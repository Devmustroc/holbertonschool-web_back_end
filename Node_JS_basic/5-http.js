const http = require('http');

const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    countStudents('database.csv')
      .then(() => {
        res.end('This is the list of our students\n');
      })
      .catch((error) => {
        res.end(error.message);
      });
  } else {
    res.end('Not found');
  }
});
app.listen(1245, () => {
  console.log('Server is running on port 1245');
});

module.exports = app;
