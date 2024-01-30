# Number-guesser
generate random number in a range 1-101
create a variable named guess that counts the amount of tries the user makes and start at 0
assign keepgoing boolean value of true 
create a while loop with keepgoing in it
  tries +=1
  guess= input(pick a number 1-100)
  if user picks number greater than number
    print(too high, try again)
  elif user picks number lower than number
    print(too low, try again)
  elif user guesses number correctly
    print the phrase (Great job, you got it!)
    keepgoing=false
  if the user guesses over 7 times
    print(Too many tries, start over)
    keepgoing=false
