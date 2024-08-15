import { Hono } from "hono";

const app = new Hono();

async function  authMiddleware(c:any,next:any) {
  if(c.req.header("Auth")){
    await next();
  }else{
    return c.text("You dont have Acesss")
  }
}





app.post("/",authMiddleware, async (c) => {

  const body=await c.req.json();
  console.log(c.req.header("Auth"))
  console.log(c.req.query("param"))

  console.log(body);
  return c.text("Hello KONA!");
});
app.get("/", (c) => {
  return c.json({"code":"Hello KONA!"});
});
export default app;
