const fs = require('fs')
const getNotes = () => {
  return ('note...')
}
const addNote = function (title, body) {
  const notes = loadNotes()
}
const loadNotes = () => {
  try {
    const dataBuffer = fs.readFileSync('notes.json')
    const dataJSON = dataBuffer.toString()
    return JSON.parse(dataJSON)
  } catch (e) {
    return [


    ]
  }

}

module.exports = {
  getNotes: getNotes,
  addNote: addNote
}
