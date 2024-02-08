def pretty_print_int(number: int) -> str:
    number_string = str(number)
    strings_to_add = []

    for i in range(len(number_string)):
        if i % 3 == 0:
            strings_to_add.append(number_string[:i] + ',')

    return number_string



print(pretty_print_int(1000))
print(pretty_print_int(5))
print(pretty_print_int(547475874))
print(pretty_print_int(-84989))
print(pretty_print_int(999))