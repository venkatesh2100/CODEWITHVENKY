// save this as checkPassword.js

import bcrypt from 'bcryptjs';

const hash = "$2b$10$DgJGMRFpr9etepneN2Z6m.gPA6ph/y2fe/FOsYCiLcHkDYQMehhYW";
const plainTextPassword = "venky";

async function checkPassword() {
  const isValid = await bcrypt.compare(plainTextPassword, hash);
  console.log("Password is valid?", isValid);
}

checkPassword();

