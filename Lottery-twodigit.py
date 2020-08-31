'''Two Digit Number'''
import random
Lottery = random.randint(10,39)
Your_Guess = int(input("Guess lottery Number pick(two Digits):"))
LotteryDigit_1 = Lottery//10
LotteryDigit_2 = Lottery%10 # apply any  formula for both lottery and Guess..

Your_Guess_Digit_1 = Your_Guess // 10
Your_Guess_Digit_2 = Your_Guess % 10

print("The Lottery Number is",Lottery)
if (Your_Guess == Lottery):
	print("Exact match: you win Rs 10,0000")
elif (Your_Guess_Digit_1 == LotteryDigit_1) and \
      (Your_Guess_Digit_2 == LotteryDigit_2):
		  print("Match all digits: you win Rs 50,000")
elif (Your_Guess_Digit_1 == LotteryDigit_1
     or Your_Guess_Digit_2 == LotteryDigit_2
     or  Your_Guess_Digit_1 == LotteryDigit_2
     or  Your_Guess_Digit_2 == LotteryDigit_1):
		 print("Match one digit: you win Rs 10,000")
else :
	print("Sorry")		 
		 		  	

