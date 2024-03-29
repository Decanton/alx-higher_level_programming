#!/usr/bin/node
/* prints My number: <first argument converted in integer>
 * if the first argument can be converted to an integer:
 */

const args = process.argv.slice(2);
const arg = args[0];
const num = parseInt(arg);

if (!isNaN(num)) { // Call isNaN with num
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
