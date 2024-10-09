from datetime import datetime

def get_upcoming_birthdays(users: list):
    # function that take list of users with data about name and birthday, return list of users that have birthdays in upcoming week

    upcoming_birthdays = []

    for user in users:
        birthday_date = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        date_today = datetime.today().date()
        upcoming_birthday = datetime(year=date_today.year, month=birthday_date.month, day=birthday_date.day).date()

        # check if birthday already was this year, if yes, change date to the next year
        if(upcoming_birthday < date_today):
            upcoming_birthday = datetime(year=date_today.year + 1, month=birthday_date.month, day=birthday_date.day).date()

        # check if birthday in upcomming week
        if(upcoming_birthday.toordinal() - date_today.toordinal() <= 7):

            # check if birthday on weekend, if yes, change congratulation date to Monday
            if(upcoming_birthday.weekday() == 5):
                upcoming_birthday = datetime(year=date_today.year, month=birthday_date.month, day=birthday_date.day + 2).date()
            if(upcoming_birthday.weekday() == 6):
                upcoming_birthday = datetime(year=date_today.year, month=birthday_date.month, day=birthday_date.day + 1).date()

            upcoming_birthdays.append({'name': user['name'], 'congratulation_date': datetime.strftime(upcoming_birthday, '%Y.%m.%d')})

    return upcoming_birthdays


get_upcoming_birthdays([
    {"name": "John Doe", "birthday": "1985.10.12"},
    {"name": "Jane Smith", "birthday": "1990.09.09"}
])