import time # time library

time_user = input("Enter the time (in seconds): ")

while not time_user.isdigit(): # check if user enters letter
    time_user = input("Invalid input! Only numbers please, try again: ") 

time_user = int(time_user) # convert string to number

while time_user: # numeric variable with value zero is equal to false
    minutes, seconds = divmod(time_user, 60) # returns result and remainder of division, first value returned is the minutes and second value (remainder of the division) is the variable seconds
    timer = f"{minutes:02d}:{seconds:02d}" 
    ''' 
    0 -> will pad with a leading zero when a digit is missing
    2 -> number width
    d -> variable type (int)
    '''
    print(timer, end="\r") # when including the next value for the line below as "\n" it updates to the current line
    time.sleep(1) # delay 1 second to become visible to the naked eye
    time_user -= 1

print("Time is up!")