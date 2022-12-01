#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint (C) {
    if (C === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let result = '';
        for (let j = 0; j < this.width; j++) result += 'C';
        console.log(result);
      }
    }
  }
};
