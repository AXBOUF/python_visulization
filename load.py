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
    bar = '#' * filled_length + '-' * (bar_length - filled_length)
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
    bar = '#' * filled_length + '-' * (bar_length - filled_length)
    elapsed_minutes = elapsed // 60
    total_minutes = total // 60
    return f"{elapsed_minutes} min out of {total_minutes} min [{bar}]"

def promtuser_time():
    try:
        elapsed = int(input("Enter the elapsed time in seconds: "))
        total = int(input("Enter the total time in seconds: "))
        bar_length = int(input("Enter the desired length of the progress bar (default is 20): ") or 20)
        print(ascii_progress_bar_time(elapsed, total, bar_length))
    except ValueError:
        print("Please enter valid integers for elapsed time, total time, and bar length.")

promtuser_time()