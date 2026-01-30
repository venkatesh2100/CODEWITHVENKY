import express, { Request, Response } from "express";
import bcrypt from "bcryptjs";

const app = express();
app.use(express.json());

interface UserInterface {
  username: string;
  password: string;
}

const USERS: UserInterface[] = [];

app.post("/signup", async (req: Request, res: Response) => {
  const { username, password } = req.body as UserInterface;

  // Validation
  if (!username || !password) {
    return res.status(400).json({
      message: "Username and password are required",
    });
  }

  // Check uniqueness
  const userExists = USERS.find(
    (user) => user.username === username
  );

  if (userExists) {
    return res.status(409).json({
      message: "User with this username already exists",
    });
  }

  // Hash password
  const hashedPassword = await bcrypt.hash(password, 10);

  USERS.push({
    username,
    password: hashedPassword,
  });

  return res.status(201).json({
    message: "User created successfully",
  });
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});
