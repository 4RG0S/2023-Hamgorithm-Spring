import datetime

def main():
    today = list(map(int, input().split()))
    d_day = list(map(int, input().split()))
    
    today_1000 = datetime.date(today[0] + 1000, today[1], today[2])
    today = datetime.date(today[0], today[1], today[2])
    d_day = datetime.date(d_day[0], d_day[1], d_day[2])

    days_1000 = (today_1000 - today).days
    days = (d_day - today).days
    
    if days >= days_1000:
        print("gg")
    else:
        print("D-" + str(days))	
    
if __name__ == '__main__':
    main()
