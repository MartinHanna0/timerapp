import time
import logging
import threading
import timer

def choice() :
    x = int(input("What would you like to do?\n1)View Date\n2)Set Timer\n3)Set Stopwatch\n"))
    if x == 1 :
        date()
        choice()
        return
    if x == 2 :
        timer_input()
        return
    if x == 3 :
        stopwatch()
        return
    else :
        print("Choose a valid input!")
        choice()
        return


def timer_input() :
    print("Choose how long to set timer for...")
    print("How many hours? Input 0 if less than 1 hour")
    h = int(input())
    print("How many minutes? Input 0 if less than 1 minute")
    m = int(input())
    print("How many seconds? Input 0 to cancel operation and return to previous screen")
    s = int(input())
    global seconds
    seconds = s + (m*60) + (h*3600)
    #timer.set_timer(milliseconds,  )
    global set_timer
   
    set_timer = '{:02}:{:02d}:{:02d}'.format(int(h),int(m),int(s))
    
    #threading.Thread(target=timer(milliseconds, timer_callback())).start()
    print("Your timer of" , set_timer , "has begun. You will be notified of when it ends.\nPlease wait patiently or press Ctrl + C to return to menu")
    
    timer_callback()
        

    return

def timer_callback():
    try:
        threading.Thread(target=time.sleep(seconds)).daemon
        print("Your timer of" , set_timer ," has ended")
        choice()
    except KeyboardInterrupt:
        print("Terminating Timer. Returning to menu")
        choice()
    
    

    return


def stopwatch() :
    done = False
    counter = 0
    x = float(input("Choose time interval for stopwatch (e.g. 1 second, 0.1 seconds) in seconds (Time is rounded to 3 decimal places)\n"))
    print("Starting stopwatch, Press Ctrl + C to return to menu.")
    try :
        while not done :
            time.sleep(x) 
            counter += x
            print(f"{counter:0,.3f}")
        
    except KeyboardInterrupt :
        print("Stopwatch terminated. Returning to menu...")
        choice()
    
    return




def date() :
    current_time_tuple = time.localtime()
    #print(current_time_tuple)

    current_day = current_time_tuple.tm_wday

    weekday_names = [ "Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday" , "Saturday" , "Sunday"]
    current_weekday = weekday_names[current_day]
    #print(current_weekday)

    formatted_time = time.strftime("%d/%m/%Y - %H:%M:%S", current_time_tuple)
    print("The date is currently:", current_weekday , ",", formatted_time)
    return

choice()