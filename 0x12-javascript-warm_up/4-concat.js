#!/usr/bin/node
/* prints two arguments passed to it in the format: "arg1 is arg2" */

const args = process.argv.slice(2);

if (args.length === 1) {
  console.log(`${args[0]} is undefined`);
} else if (args.length === 2) {
  console.log(`${args[0]} is ${args[1]}`);
} else {
  console.log('undefined is undefined');
}
