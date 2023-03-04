import time
def countdown(t):
    if (t==0):
        print("BLAST OFF!!")
    else:
        print(t)
        print('*'*t)
        time.sleep(1)
        countdown(t-1)

count = int(input("Enter a number to start the countdown"))
countdown(count)