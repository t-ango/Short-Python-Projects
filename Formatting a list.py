'''
This program allows users to input a list of items and formats the list into a human-readable string.

- **Input**:
  - The user enters items one at a time.
  - Input stops when the user enters a blank space.

- **Process**:
  - The `formatListOfItems` function formats the list:
    - Single item: Returns the item directly.
    - Two items: Combines with "and" (e.g., "a and b").
    - More than two items: Combines with commas and "and" before the last item (e.g., "a, b, c and d").

- **Output**:
  - Prints the formatted string of items.
'''

def main ():
    myList = []
    userInput = input("Enter items (enter blank to stop): ")
    
    while userInput != " ":
        myList.append(userInput)
        userInput = input("Enter items (enter blank to stop): ")

    
    formatedList = formatListOfItems(myList)

     
    print ("The items are: " , formatedList)   

def formatListOfItems (listofitems):
    """Takes a list of items and formats them as: a,b,c and d"""

    if len(listofitems) == 0:
        return " "
    elif len(listofitems) == 1:
        return listofitems[0]
    elif len(listofitems) == 2:
        return f"{listofitems[0]} and {listofitems[1]}"
    else:
        allItemsbutthelast = ",".join (listofitems[: -1])
        return f"{allItemsbutthelast} and {listofitems[-1]}"

main ()