from datetime import date

def log_datetime(func):

    def wrapper():
        today = date.today()
        print("Today's date:", today)
        func()
        print("the time was:")
        d1 = today.strftime("%d/%m/%Y")
        print(d1)
        d2 = today.strftime("%B %d, %Y")
        print(d2)
        d3 = today.strftime("%m/%d/%y")
        print(d3)
        d4 = today.strftime("%b-%d-%Y")
        print(d4)
    return wrapper


@log_datetime
def daily_backup():
    print('job has finished.')

daily_backup()