"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
const pg_1 = require("pg");
const client = new pg_1.Client({
    connectionString: "postgresql://postgres:code2100@localhost/postgres",
});
function createTable() {
    return __awaiter(this, void 0, void 0, function* () {
        try {
            yield client.connect();
            const result = yield client.query(`
      CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        email VARCHAR(200) UNIQUE NOT NULL,
        password VARCHAR(99) NOT NULL,
        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
      )
    `);
            console.log("Table created:", result);
        }
        catch (err) {
            console.error("Error creating table:", err);
        }
    });
}
function insertIntoTable() {
    return __awaiter(this, void 0, void 0, function* () {
        try {
            const insert = yield client.query(`
      INSERT INTO users (username, email, password)
      VALUES 
        ('venkat', 'venkyvenkat.iit@example.com', 'codecodce'),
        ('ram', 'ramgopal.iit@example.com', 'rambo'),
        ('arjun1', 'arjundas.pop@example.com', 'coop')
    `);
            console.log("Data inserted:", insert);
        }
        catch (err) {
            console.error("Error inserting data:", err);
        }
        finally {
            yield client.end();
        }
    });
}
function main() {
    return __awaiter(this, void 0, void 0, function* () {
        yield createTable();
        yield insertIntoTable();
    });
}
main();
