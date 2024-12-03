function designerPdfViewer(h: number[], word: string): number {
  let maxHeight = 0;

  for (let char of word) {
      // Find the index of the character in the alphabet (0 for 'a', 1 for 'b', etc.)
      const index = char.charCodeAt(0) - 97;
      // Get the height of this character and update the maximum height

      console.log("Index of the Array:"+index);

      maxHeight = Math.max(maxHeight, h[index]);
      console.log("Max Updated Heighy:"+maxHeight);

  }

  // Calculate the highlighted area (maxHeight * word.length)
  return maxHeight * word.length;
}
const h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1];
const word = "abc";
console.log(designerPdfViewer(h, word)); // Expected output: 9
