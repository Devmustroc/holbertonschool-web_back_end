const fs = require('fs')


const removeNote = function (title, body, length) {
  const notes = loadNotes()
  console.log(notes)
  const duplicateNotes = notes.filter((note) =>{
    return note.title !== title
  })
  console.log(duplicateNotes)
  if (notes.length > duplicateNotes.length) {
    notes.pop({
      title: title,
    })
    saveNotes(notes)
    console.log("Node Removed")
  } else {
    console.log("Node Not Found !")
  }
}

const getNotes = () => {
  return ('note...')
}
const addNote = function (title, body, length) {
  const notes = loadNotes()
  const duplicateNotes = notes.filter((note) =>{
    return note.title === title
  })
  if (duplicateNotes.length === 0) {
    notes.push({
      title: title,
      body: body,
      length: length
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
  addNote: addNote,
  removeNote: removeNote
}
