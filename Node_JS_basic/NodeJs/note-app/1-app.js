// Command line Using Yargs
const yargs = require('yargs');
const notes = require('./notes')

yargs.command({
  command: 'add',
  describe: 'Add a new note',
  builder: {
    title: {
      describe: 'Add Title',
      demandOption: true,
      type: 'string',
    },
    body : {
      title: 'Add body',
      demandOption: true,
      type: 'string'
    },
    content : {
      title: 'Add content',
      demandOption: true,
      type: 'number'
    }
  },
  handler: (argv) => {
    notes.addNote(argv.title, argv.body, argv.content)
  }
});
// Create remove command
yargs.command({
  command: 'remove',
  describe: 'Remove a note',
  builder: {
    title: {
      describe: 'Title remove',
      demandOption: true,
      type: 'string'
    }
  },
  handler: (argv) => {
    notes.removeNote(argv.title)
  }
})
yargs.parse()

