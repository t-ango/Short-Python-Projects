
def main():
    inputSec = int (input("Enter a number of seconds: "))
    formatTime = hour_min_sec (inputSec)

    print ("The hours, minutes and seconds for total" , inputSec , "seconds is: ", hour_min_sec(inputSec) )




def hour_min_sec (sec):
    """Takes a number of seconds and converts them to Hr:min:sec format"""

    
    day = sec % 86400

    hours = day // 3600
    if hours < 9:
        hours = f"0{hours}"
    minutes = (day % 3600) // 60
    if minutes < 9:
        minutes = f"0{minutes}"
    seconds = (day % 60) % 60
    if seconds < 9:
        seconds = f"0{seconds}"

    return f"{hours}:{minutes}:{seconds}"



main()
    

    






    