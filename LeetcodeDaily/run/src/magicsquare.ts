function generateMagicSquare(n:number) {
  if (n % 2 === 0) {
    throw new Error("This method only works for odd-order magic squares.");
  }

  // Initialize a 2D array filled with zeros
  const magicSquare = Array.from({ length: n }, () => Array(n).fill(0));

  let num = 1; // Start filling numbers from 1
  let i = 0;
  let j = Math.floor(n / 2); // Start in the middle of the first row

  while (num <= n * n) {
    magicSquare[i][j] = num; // Place the current number
    num++;

    // Move up and to the right
    let newI = (i - 1 + n) % n;
    let newJ = (j + 1) % n;

    // If the target cell is already filled, move down instead
    if (magicSquare[newI][newJ] !== 0) {
      i = (i + 1) % n;
    } else {
      i = newI;
      j = newJ;
    }
  }

  return magicSquare;
}

// Example usagels
const n = 5;
const magicSquare = generateMagicSquare(n);
magicSquare.forEach(row => console.log(row));
