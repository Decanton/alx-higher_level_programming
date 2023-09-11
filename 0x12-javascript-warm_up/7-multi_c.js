#!/usr/bin/node
/* writes "c is fun" x times */

const args = process.argv.slice(2);

const line = 'c is fun';

const num = parseInt(args[0]);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) {
    console.log(line);
  }
}
