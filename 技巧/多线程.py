import threading,time
def sing(a1):
    while True:
        print(a1)
        time.sleep(1)
def dance(a2):
    while True:
        print(a2)
        time.sleep(1)
if __name__ == '__main__':
    sing_thread=threading.Thread(target=sing,args=("黑"))#双线程,args:元组传参，kwargs：字典传参
    dance_thread=threading.Thread(target=dance,kwargs={"a2":"白"})
    sing_thread.start()
    dance_thread.start()