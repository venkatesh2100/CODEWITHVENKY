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
const client_1 = require("@prisma/client");
const prisma = new client_1.PrismaClient();
function Inserdata(lastname, email, password, fisrtname) {
    return __awaiter(this, void 0, void 0, function* () {
        const res = yield prisma.user.create({
            data: {
                lastname,
                fisrtname,
                email,
                password,
            },
            select: { id: true, password: true, fisrtname: true },
        });
        console.log(res);
    });
}
// Inserdata("kona","konasnail.ynm@gmail.com", "venkat", "kona");
function Updatedate(email_1, _a) {
    return __awaiter(this, arguments, void 0, function* (email, { fisrtname, password, lastname }) {
        const res = yield prisma.user.update({
            where: { email: email },
            data: {
                fisrtname,
                lastname,
                password,
            },
        });
        console.log(res);
    });
}
// Updatedate("konavenkat.ynm@gmail.com", {
//   fisrtname: "venkat99",
//   lastname: "kona99",
// });
//
function Deletedata(email) {
    return __awaiter(this, void 0, void 0, function* () {
        const res = yield prisma.user.delete({
            where: {
                email: email,
            },
        });
        console.log(res);
    });
}
Deletedata("konasnail.ynm@gmail.com");
