from random import sample

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    # function generate list of uniq numbers from min to max which number equal to quantity value

    if(min < 1 or max > 1000 or quantity > max - min):
        print('Inaccurate value: min must be more than 1, max - no more than 1000, quantity - value between min and max')
        return []

    list_of_numbers = sample(range(min, max), quantity)

    return sorted(list_of_numbers)


get_numbers_ticket(1, 49, 6)