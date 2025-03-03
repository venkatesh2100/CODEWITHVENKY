import { Client } from "pg";
const client = new Client({
  host:'localhost',
  port:5432,
  database:'postgres',
  user:'postgres',
  password:'code2100'
});


async function createTable() {


  try {
    await client.connect();

    const result = await client.query(`
      CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        email VARCHAR(200) UNIQUE NOT NULL,
        password VARCHAR(99) NOT NULL,
        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
      )
    `);

    console.log("Table created:", result);
  } catch (err) {
    console.error("Error creating table:", err);
  }
}

async function insertIntoTable() {
  try {
    const insert = await client.query(`
      INSERT INTO users (username, email, password)
      VALUES 
        ('venkat', 'venkyvenkat.iit@example.com', 'codecodce'),
        ('ram', 'ramgopal.iit@example.com', 'rambo'),
        ('arjun1', 'arjundas.pop@example.com', 'coop')
    `);

    console.log("Data inserted:", insert);
  } catch (err) {
    console.error("Error inserting data:", err);
  } finally {
    await client.end();
  }
}

async function main() {
  await createTable();
  await insertIntoTable();
}

main();
