const fs = require('fs')
/*
const book = {
  title: 'Ego is the Enemy',
  author: 'Ryan holiday'
}

const bookJSON = JSON.stringify(book)
fs.writeFileSync('1-json.json', bookJSON)
*/
/*const dataBuffer = fs.readFileSync('1-json.json')
const dataJSON = dataBuffer.toString()
const data = JSON.parse(dataJSON)
console.log(data.title)*/
const dataBuff = fs.readFileSync('1-json.json')
const JSONdata = dataBuff.toString()
const data = JSON.parse(JSONdata)
data.name = "Mustapha"
data.age = 36
const dataToStr = JSON.stringify(data)
const newData = fs.writeFileSync('1-json.json', dataToStr)


