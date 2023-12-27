#Count_down_timer_project

#imoort time module 
import time 

#Allow users to type in the number of time needed
timer = int(input('Enter your time in seconds: '))

#divmod function was used to divide the input
minutes, timer = divmod(timer, 60)
hours, minutes = divmod(minutes, 60)


while timer > 0:
    #print started with padding that is to structure the timer from hour to seconds
    print("{:02d}:{:02d}:{:02d}".format(hours, minutes, timer))
    time.time(2)
    timer -= 1

    if timer < 0:
        mintues = 59
        minutes -= 1

        if timer < 0:
            timer = 59
            timer -= 1

timer -=1
