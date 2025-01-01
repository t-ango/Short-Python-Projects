'''
This program calculates the 10th digit of an ISBN-10 code based on the first 9 digits provided by the user.

- **Input**: The user is prompted to enter the first 9 digits of an ISBN code.
  - The input is validated to ensure it is exactly 9 digits.
  - If the input is invalid, the program displays an error message.

- **Process**:
  - Each digit of the 9-digit input is extracted using division and modulus operations.
  - The 10th digit (checksum) is calculated using the formula:
    d10 = (d1*1 + d2*2 + d3*3 + ... + d9*9) % 11

- **Output**:
  - If valid input is provided, the program outputs the complete 10-digit ISBN code.
  - The checksum digit (d10) is appended to the original 9 digits.

This program adheres to the ISBN-10 standard for generating valid ISBN codes.
'''
first9digits = int(input("Enter first 9 digits of an ISBN code:"))

if first9digits not in range (99999999,999999999):
    print ("Invalid input! Enter 9 digits")
    
else :
    d1 = first9digits // 100000000  
    tal = first9digits % 100000000
    d2 = tal // 10000000
    tal = tal % 10000000
    d3 = tal // 1000000 
    tal = tal % 1000000
    d4 = tal // 100000
    tal = tal % 100000
    d5 = tal // 10000
    tal = tal % 10000
    d6 = tal // 1000
    tal = tal % 1000
    d7 = tal // 100
    tal = tal % 100
    d8 = tal // 10 
    d9 = tal % 10 

    d10 = (d1*1+d2*2+d3*3+d4*4+d5*5+d6*6+d7*7+d8*8+d9*9) % 11
    print ("The ISBN number is " , first9digits , d10, sep="")

