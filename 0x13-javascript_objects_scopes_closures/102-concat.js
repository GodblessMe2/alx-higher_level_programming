#!/usr/bin/node
const fs = require('fs');
const text1 = fs.readFileSync('./fileA', 'utf-8');
const text2 = fs.readFileSync('./fileB', 'utf-8');
const concats = text1 + text2;
fs.writeFileSync('./fileC', concats);
