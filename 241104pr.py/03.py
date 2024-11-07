import datetime

def get_time():
    current_time=datetime.datetime.now().time()
    return current_time.strftime("%I:%M:%S %p")

if __name__=="__main__":
    print(get_time())