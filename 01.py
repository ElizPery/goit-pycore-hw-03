from datetime import datetime

def get_days_from_today(date: str) -> int:
    # function that take date in string (format '2020-10-09') and return number of days from this date to today's date

    try:
        parsed_date = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print('Date format must be: "2024-10-09"')
    else:
        date_today = datetime.today()
        return date_today.toordinal() - parsed_date.toordinal()


get_days_from_today('2024-10-29')