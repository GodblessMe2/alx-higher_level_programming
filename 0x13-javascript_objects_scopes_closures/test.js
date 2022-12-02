// const num = 2.9;
// console.log(num | 0);

// const arr = [5, 5, 5, 2, 2, 2, 2, 2, 9, 4];
// const counts = {};

// for (const num of arr) {
//   counts[num] = counts[num] ? counts[num] + 1 : 1;
// }

// console.log(counts);
// console.log(counts[5], counts[2], counts[9], counts[4]);

// let index = 0;
// const target = 'c';
// const collection = ['a', 'b', 'c', 'd'];

// function findIndex () {
//   for (const val in collection) {
//     index++;
//     console.log(index[val]);
//   }
// }

// findIndex();


// module.exports = class Square extends require('./5-square.js') {
//   charPrint (C) {
//     if (C === undefined) {
//       this.print();
//     } else {
//       for (let i = 0; i < this.height; i++) {
//         let result = '';
//         for (let j = 0; j < this.width; j++) result += 'C';
//         console.log(result);
//       }
//     }
//   }
// };


// exports.nbOccurences = function (list, searchElement) {
//   const counts = {};

//   for (const num of list) {
//     counts[num] = counts[num] ? counts[num] + 1 : 1;
//   }
//   return (counts[searchElement]);
// };

// const fs = require('fs');
// const text1 = fs.readFileSync('./fileA', 'utf-8');
// const text2 = fs.readFileSync('./fileB', 'utf-8');
// fs.writeFileSync('./fileC', text1 + text2);