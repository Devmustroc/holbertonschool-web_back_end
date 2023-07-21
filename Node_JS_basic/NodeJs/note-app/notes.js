const fs = require('fs')
const chalk = require('chalk')


const removeNote = function (title, body, length) {
  const notes = loadNotes()
  const nodeToKeep = notes.filter((note) =>{
    return note.title !== title
  })
  if (notes.length > nodeToKeep.length) {
    console.log(chalk.bgGreen('Note removed !'))
    saveNotes(nodeToKeep)
  }
  else {
    console.log(chalk.bgRed('No note found !'))
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
    console.log(chalk.green('New note added !'))
  } else {
    console.log(chalk.red('Node title Taken !'))
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
