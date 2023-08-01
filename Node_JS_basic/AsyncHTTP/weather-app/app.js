const request =  require("request")

const url = 'http://api.weatherstack.com/current?access_key=2134d1bbc5317748dc625e0e79c25420&query=Agadir&units=f';

request({url: url, json: true}, (err, response) => {
  if (err) {
    console.log("Unable to connect to weather service");
  }
  console.log(response.body.current.temperature);
})
