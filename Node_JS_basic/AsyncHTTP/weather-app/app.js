const request =  require("request")

const url = 'http://api.weatherstack.com/current?access_key=6219314f5320cd5e5b0c6239914e8d80&query=New%20York';

request({url: url}, (err, response) => {
  const data = JSON.parse(response.body);
  console.log(data.currently);
})
