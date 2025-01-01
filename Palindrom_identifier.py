'''
This program checks whether a user-provided three-digit number is a palindrome.

- **Input**: 
  - The user is prompted to enter a three-digit number.
  - The program validates the input to ensure it is within the range of valid three-digit numbers (100-999).
  - If the input is invalid, an error message is displayed.

- **Process**:
  - The first digit (hundreds place) and the last digit (units place) are extracted from the input.
  - These two digits are compared to determine if the number is a palindrome (reads the same forward and backward).

- **Output**:
  - If the first and last digits match, the program prints "This number is a palindrome."
  - Otherwise, it prints "This number is not a palindrome."
'''
userTal = eval(input("Enter three digits:"))

if userTal not in range (99,999):
    print ("Invalid input. Enter three digits!")
else :
    digit1 = userTal // 100
    digit3 = userTal % 10
    if digit1 == digit3:
        print ("This number is a palindrome")
    else:
        print ("This number is not a palindrome")
    
