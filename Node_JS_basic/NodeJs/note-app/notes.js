const fs = require('fs')
const getNotes = () => {
  return ('note...')
}
const addNote = function (title, body) {
  const notes = loadNotes()
  const duplicateNotes = notes.filter((note) =>{
    return nodes.title === title
  })
  if (duplicateNotes.length === 0) {
    notes.push({
      title: title,
      body: body
    })
    saveNotes(notes)
    console.log("New Node Added")
  } else {
    console.log("Node title Taken !")
  }

}
const loadNotes = () => {
  try {
    const dataBuffer = fs.readFileSync('notes.json')
    const dataJSON = dataBuffer.toString()
    return JSON.parse(dataJSON)
  } catch (e) {
    return []
  }

}
const saveNotes = function (notes) {
  const dataJSON = JSON.stringify(notes)
  fs.writeFileSync('notes.json', dataJSON)
}

module.exports = {
  getNotes: getNotes,
  addNote: addNote
}
