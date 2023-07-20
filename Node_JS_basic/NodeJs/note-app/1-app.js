// Command line Using Yargs

const yargs = require('yargs');

yargs.command({
  command: 'add',
  describe: 'Add a new note',
  builder: {
    title: {
      describe: 'Add Title',
      demandOption: true,
      type: 'string'
    },
    length: {
      describe: 'note length',
      demandOption: true,
      type: 'number'
    }
  },
  handler: () => {

    console.log('Adding a new note!');
  }
});
// Create remove command
yargs.command({
  command: 'remove',
  describe: 'Remove a note',
  builder: {
    title: {
      describe: 'Title remove',
      demandOption: true
    }
  },
  handler: () => {
    console.log('Removing the note!');
  }
})
yargs.command({
  command: 'list',
  describe: 'list a note',
  builder: {
    title: {
      describe: 'Note title',
      demandOption: true,
    }
  },
  handler: (argv) => {
    console.log('notes ar listed', argv)
  }
})
yargs.command({
  command: 'read',
  describe: 'read notes',
  builder: {
    title: {
      describe: 'Title read note',
      demandOption: true
    }
  },
  handler: () => {
    console.log('reading the notes')
  }
})
console.log(yargs.argv)
