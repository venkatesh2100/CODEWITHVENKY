"use strict";
function designerPdfViewer(h, word) {
    let maxHeight = 0;
    for (let char of word) {
        const index = char.charCodeAt(0) - 97;
        console.log("Index of the Array:" + index);
        maxHeight = Math.max(maxHeight, h[index]);
        console.log("Max Updated Heighy:" + maxHeight);
    }
    return maxHeight * word.length;
}
const h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1];
const word = "abc";
console.log(designerPdfViewer(h, word));
