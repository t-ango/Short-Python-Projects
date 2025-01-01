'''
This program converts a user-provided decimal number between 0 and 15 into its binary equivalent.
- The user inputs a number in the range 0 to 15.
- The program calculates the binary representation by repeatedly dividing the number by 2 and taking the remainder.
- The binary digits are displayed in the correct order.
- If the number is out of range, the program prompts the user to enter a valid number.
'''
userNumber = eval (input ("Enter a number from 0 to 15:"))

digit1 = userNumber % 2 
tal = userNumber // 2 
digit2 = tal % 2 
tal = tal // 2
digit3 = tal % 2 
tal = tal // 2 
digit4 = tal % 2 
if userNumber >= 0 and userNumber <= 7:
    print ("The binary number for" , userNumber , "is" , digit3, digit2, digit1)
elif userNumber >= 8 and userNumber <= 16:
    print ("The binary number for" , userNumber , "is" , digit4, digit3, digit2, digit1)
else :
    print ("Something went wrong! Enter correct number")