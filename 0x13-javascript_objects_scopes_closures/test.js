// const num = 2.9;
// console.log(num | 0);

// const arr = [5, 5, 5, 2, 2, 2, 2, 2, 9, 4];
// const counts = {};

// for (const num of arr) {
//   counts[num] = counts[num] ? counts[num] + 1 : 1;
// }

// console.log(counts);
// console.log(counts[5], counts[2], counts[9], counts[4]);

let index = 0;
const target = 'c';
const collection = ['a', 'b', 'c', 'd'];

function findIndex () {
  for (const val in collection) {
    index++;
    console.log(index[val]);
  }
}

findIndex();
