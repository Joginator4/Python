class WeekDayError(Exception):
    def error(self):
        return "There is no attribute that u passed in WeekDayError!"
	

class Weeker:
    __days=["Mon","Tue", "Wed" ,"Thu", "Fri", "Sat", "Sun"]

    def __init__(self, day):
        self.__current=Weeker.__days.index(day)

    def __str__(self):
        return Weeker.__days[self.__current]

    def add_days(self, n):
        self.__current = (self.__current + n) % 7

    def subtract_days(self, n):
        self.__current = (self.__current - n) % 7


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(7)
    print(weekday)
    weekday.subtract_days(14)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")





















