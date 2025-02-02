import base58 from "bs58";

const arr = new Uint8Array([10, 393, 238948, 2992, 256]);

// Convert Uint8Array to Buffer (to handle base58 encoding properly)
const buffer = Buffer.from(arr);

const res = buffer.toString("base64");
const val58 = base58.encode(buffer);

console.log("NormalText", buffer);
console.log("Base64:", res);
console.log("Base58:", val58);
