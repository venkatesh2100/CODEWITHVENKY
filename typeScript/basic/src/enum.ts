function move(keypressed:Direction){
  if(keypressed==Direction.Down){
    console.log("Down");
  }

}
enum Direction{
  UP,
  Left,
  Right,
  Down
}
move(Direction.Down);