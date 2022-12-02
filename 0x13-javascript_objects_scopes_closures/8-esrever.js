#!/usr/bin/node
exports.esrever = function (list) {
  const newString = [];
  while (list.length) {
    newString.push(list.pop());
  }
  return newString;
};
