"use strict";
function generateMagicSquare(n) {
    if (n % 2 === 0) {
        throw new Error("This method only works for odd-order magic squares.");
    }
    const magicSquare = Array.from({ length: n }, () => Array(n).fill(0));
    let num = 1;
    let i = 0;
    let j = Math.floor(n / 2);
    while (num <= n * n) {
        magicSquare[i][j] = num;
        num++;
        let newI = (i - 1 + n) % n;
        let newJ = (j + 1) % n;
        if (magicSquare[newI][newJ] !== 0) {
            i = (i + 1) % n;
        }
        else {
            i = newI;
            j = newJ;
        }
    }
    return magicSquare;
}
const n = 5;
const magicSquare = generateMagicSquare(n);
magicSquare.forEach(row => console.log(row));
