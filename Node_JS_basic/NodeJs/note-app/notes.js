const fs = require('fs')
const chalk = require('chalk')


const readNotes = (title) => {
  const notes = loadNotes()
  const findNotes = notes.find((note) => note.title === title)
  debugger
  if (findNotes) {
    console.log(chalk.yellow(findNotes.title + "\n"+ findNotes.body))
  } else {
    console.log(chalk.red('title not found'))
  }
}

const removeNote =  (title) => {
  const notes = loadNotes()
  const nodeToKeep = notes.filter((note) => note.title !== title)
  if (notes.length > nodeToKeep.length) {
    console.log(chalk.bgGreen('Note removed !'))
    saveNotes(nodeToKeep)
  }
  else {
    console.log(chalk.bgRed('No note found !'))
  }

}

const listNotes = () => {
  const notes= loadNotes()
  notes.forEach((note) => console.log(chalk.bgCyan(note.title)))
}

const getNotes = () => 'note...'

const addNote = function (title, body, length) {
  const notes = loadNotes()
  const duplicateNote = notes.find((note) => note.title ===title)
  if (!duplicateNote) {
    notes.push({
      title: title,
      body: body,
      length: length
    })
    saveNotes(notes)
    console.log(chalk.bgGreen('New note added !'))
  } else {
    console.log(chalk.bgRed('Node title Taken !'))
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
const saveNotes =  (notes) => {
  const dataJSON = JSON.stringify(notes)
  fs.writeFileSync('notes.json', dataJSON)
}

module.exports = {
  getNotes: getNotes,
  addNote: addNote,
  removeNote: removeNote,
  listNotes: listNotes,
  readNotes: readNotes
}
