// Command line Using Yargs
const chalk = require('chalk');
const getNotes = require('./notes.js');
const yargs = require('yargs');
const {argv} = require("yargs");
// costumise yargs version
yargs.version('2.1.0')
const arg = argv
console.log(arg)
