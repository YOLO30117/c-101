import time
def countDownTimer(secs):
    while(secs>0):
        mins = int(secs/60)
        seconds = int(secs%60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end = "\r")
        time.sleep(1)
        secs -= 1
    print("time up")
s = int(input("enter time in seconds: "))
countDownTimer(s)

  
