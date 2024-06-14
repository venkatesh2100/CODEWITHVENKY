print('*' * 10)
name="venkatesh suravarapu"
print(name.replace("sura","Sura"))
print('Sura' in name)

secreateNum=9
numberofGuess=1
while numberofGuess<=3:
  guessNumber=int(input(f"Enter your {numberofGuess} guess:"))
  if guessNumber >secreateNum:
    print("Try again your: your guess is Tooo High ")
  elif guessNumber < secreateNum:
    print("Try again your: your guess is Too Low")
  else:
    print("Congrats your Guess is Right")
    break
  numberofGuess=numberofGuess+1
  print("Sorry your chances are Over")
