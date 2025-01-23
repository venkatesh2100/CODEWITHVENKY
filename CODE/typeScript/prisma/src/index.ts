import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

async function Inserdata(
  lastname: string,
  email: string,
  password: string,
  fisrtname: string,
) {
  const res = await prisma.user.create({
    data: {
      lastname,
      fisrtname,
      email,
      password,
    },
    select: { id: true, password: true, fisrtname: true },
  });
  console.log(res);
}
// Inserdata("kona","konasnail.ynm@gmail.com", "venkat", "kona");

async function Updatedate(
  email: string,
  { fisrtname, password, lastname }: any,
) {
  const res = await prisma.user.update({
    where: { email: email },
    data: {
      fisrtname,
      lastname,
      password,
    },
  });
  console.log(res);
}

// Updatedate("konavenkat.ynm@gmail.com", {
//   fisrtname: "venkat99",
//   lastname: "kona99",
// });
//
async function Deletedata(email: string) {
  const res = await prisma.user.delete({
    where: {
      email: email,
    },
  });

  console.log(res);
}
Deletedata("konasnail.ynm@gmail.com");
