#!/usr/bin/node
const fs = require('fs');
const text1 = fs.readFileSync('./fileA', 'utf-8');
const text2 = fs.readFileSync('./fileB', 'utf-8');
fs.writeFileSync('./fileC', text1 + text2);
