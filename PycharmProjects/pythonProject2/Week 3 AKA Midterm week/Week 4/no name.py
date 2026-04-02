class Duration:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __lt__(self, other):
        if self.hours < other.hours:
            return True
        elif self.hours == other.hours:
            if self.minutes < other.minutes:
                return True
        return False

workday = Duration(9, 45)
monday_time = Duration(9, 45)
tuesday_time = Duration(11, 15)
wednesday_time = Duration(6, 45)

print(monday_time < workday)
print(tuesday_time < workday)
print(wednesday_time < workday)
print(tuesday_time < monday_time)