# loading [###########]


# promt the ratio it could be 16 out of 20 then we have to standarize the scenario 
 

# then fill up the 16 out of the ttotal 

# test case 1: 5 out of 10 [####----]
# test case 2: 0 out of 10 [----------]
# test case 3: 10 out of 10 [########]

# we will later may prompt how long the ascii bar they want 

def ascii_progress_bar(current, total, bar_length=10):
    if total == 0:
        filled_length = 0
    else:
        filled_length = int(round(bar_length * current / float(total)))
    bar = '\033[92m' + '#' * filled_length + '\033[0m' + '\033[91m' + '-' * (bar_length - filled_length) + '\033[0m'
    return f"{current} out of {total} [{bar}]"


def promtuser():
    try:
        current = int(input("Enter the current value: "))
        total = int(input("Enter the total value: "))
        bar_length = int(input("Enter the desired length of the progress bar (default is 10): ") or 10)
        print(ascii_progress_bar(current, total, bar_length))
    except ValueError:
        print("Please enter valid integers for current, total, and bar length.")


# another way would be to use for timestamp 
# for exmaple if a video is 2 hours long and we are at 30 minutes
# we can show the progress bar based on the time elapsed
# this would be useful for media players or download managers

def ascii_progress_bar_time(elapsed, total, bar_length=20):
    if total == 0:
        filled_length = 0
    else:
        filled_length = int(round(bar_length * elapsed / float(total)))
    bar = '\033[92m' + '#' * filled_length + '\033[0m' + '\033[91m' + '-' * (bar_length - filled_length) + '\033[0m'
    total_minutes = total // 60
    return f"{elapsed_minutes} min out of {total_minutes} min [{bar}]"

# given time format hh:mm:ss we can convert it to seconds
# and then use the above function to show the progress bar
def time_to_seconds(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s

def promtuser_time():
    try:
        elapsed_str = input("Enter the elapsed time (hh:mm:ss): ")
        total_str = input("Enter the total time (hh:mm:ss): ")
        bar_length = int(input("Enter the desired length of the progress bar (default is 20): ") or 20)
        elapsed = time_to_seconds(elapsed_str)
        total = time_to_seconds(total_str)
        print(ascii_progress_bar_time(elapsed, total, bar_length))
    except ValueError:
        print("Please enter valid time in hh:mm:ss format and integers for bar length.")        

def main():
    print("Choose an option:")
    print("1. Progress bar based on current and total values")
    print("2. Progress bar based on elapsed and total time")
    choice = input("Enter 1 or 2: ")
    if choice == '1':
        promtuser()
    elif choice == '2':     
        promtuser_time()
if __name__ == "__main__":
    main()
        
# next we can add colors to the progress bar using ANSI escape codes
# for example we can make the filled part green and the unfilled part red
# this would make it more visually appealing    
