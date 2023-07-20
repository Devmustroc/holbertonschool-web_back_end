/*
const chalk = require('chalk');
const msg = chalk.green.bold('Success!');
console.log(msg);
*/


// Get input from user
const chalk = require('chalk');
const getNotes = require('./notes.js');

const command = process.argv[2];
console.log(process.argv)

if (command === "add") {
  console.log(chalk.green.bold('Adding note...'));
} else if (command === "remove") {
  console.log(chalk.red.bold('Removing note...'));
}
