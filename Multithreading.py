import _thread
import time

def countdown(threadname):
    count=0
    while (count < 10):
        print("{} , the count is:{}".format(threadname,count))
        count=count+1
        time.sleep(2)
def main():
    try:
        _thread.start_new_thread(countdown,("Thread 1",))#the commas indicate that the data is a tuple
        _thread.start_new_thread(countdown,("thread 2",)) # the third thread
        print("thread is running")#this line is run on a different thread(multi threading)
    except:
        print("unable to start thread")
    while 1: #this piece of code ensures that the thread output is seen.the application waits after the thread is done
        pass



if __name__ == '__main__':main()
