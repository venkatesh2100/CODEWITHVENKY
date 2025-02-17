import { generateMnemonic, mnemonicToSeedSync } from "bip39";

const message = generateMnemonic()
const seedMessage =mnemonicToSeedSync(message)
console.log(message)
console.log(seedMessage)
