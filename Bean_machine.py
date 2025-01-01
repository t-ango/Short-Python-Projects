'''
This program simulates a bean machine (Galton board), where balls fall through a series of slots to demonstrate random distribution.

- **Input**:
  - Number of balls to drop.
  - Number of slots available.

- **Process**:
  1. Simulates each ball's path using random left/right decisions.
  2. Records how many balls land in each slot.
  3. Displays a histogram representing the final distribution of balls across the slots.

- **Output**:
  - A visual histogram of ball distribution in the slots.
  - Slot labels for clarity.
'''

def main():

    user_input_balls = int(input("Enter a number of balls: "))
    user_input_slots = int(input("Enter a number of slotts: "))

    ballsinslots = bean_machine(user_input_balls, user_input_slots)

    histogram(ballsinslots,user_input_slots)



def bean_machine (balls,slots):
    import random
    slot_list = [0] * slots
    

    for i in range (balls):
        start = 0
        for i in range (slots - 1):
            if random.choice ([True,False]):
                start += 1
            else:
                start -= 1
            start = max(0,start)
        slot_list [start] += 1
    return slot_list

def histogram (some_list,slots):
    
    max_value = max(some_list)
    
    for level in range (max_value,0,-1):
        row = ""
        for item in some_list:
            if item >= level:
                row += "o"
            else:
                row += " "
        print (row)

    label_row = ""
    for item in range (1, slots + 1):
        label_row = str(item)
        print (label_row,end="")
       

main ()
