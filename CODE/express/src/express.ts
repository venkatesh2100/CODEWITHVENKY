import bcrypt from "bcryptjs";
import express, { Request, Response } from "express";
const app = express();
app.use(express.json());

interface User {
  username: string;
  password: string;
}

const USERS: User[] = [];

app.post("/signup", async (req: Request, res: Response) => {
  const { username, password } = req.body as User;

  if (!username || !password) {
    return res.status(409).json({
      msg: "Inputs Fileds are empty",
    });
  }

  const userExists = USERS.find((user) => user.username == username);

  if (userExists) {
    return res.status(400).json({
      msg: "User already Exists",
    });
  }

  const hanshedPassword = await bcrypt.hash(password, 10);

  USERS.push({
    username,
    password: hanshedPassword,
  });

  return res.status(200).json({
    msg: "User Created Succesfully",
  });
});

app.post("/login", async (req: Request, res: Response) => {
  const { username, password } = req.body as User;

  if (!username || !password) {
    return res.status(400).json({
      msg: "Input Fileds are empty",
    });
  }

  const userExists = USERS.find((user) => user.username == username);
  if (!userExists) {
    return res.status(409).json({
      msg: "User not Found",
    });
  }
  const passwordMatch = await bcrypt.compare(password, userExists.password);
  if (!passwordMatch) {
    return res.status(400).json({
      msg: "password not Valid",
    });
  }

  return res.status(200).json({
    msg: "Sucessfully Loggedin",
  });
});

app.listen(5000, () => {
  console.log("5000 Porting is Running");
});
