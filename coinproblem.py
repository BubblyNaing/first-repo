# A function is a Reusable block of code

def coins_converter(total_number_of_cents) :
    total_number_of_cents = int(total_number_of_cents)
    number_of_dimes = total_number_of_cents//10
    remaining_cents = total_number_of_cents%10
    number_of_nickels = remaining_cents//5
    number_of_pennys = remaining_cents%5
    print("--"*5)
    return number_of_dimes, number_of_nickels, number_of_pennys

coins_converter(106)