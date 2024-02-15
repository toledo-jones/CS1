

def compound_at_frequency(principle, frequency, rate, years):
    # a = P(1+ r/n)^nt
    return principle * (1 + rate / frequency) ** (frequency * years)


def compound_continuously(principle, frequency, rate, years):
    from math import e
    # a = pe^rt
    return principle * e ** (rate * years)


def simulate_account_balance_pp(
        init_principal,
        acc_rate,
        acc_cmp_freq,
        setup_fee,
        years):
    principal = init_principal - setup_fee
    if acc_cmp_freq == 0:
        formula = compound_continuously
    else:
        formula = compound_at_frequency
    
    values_to_display = {}
    for year in range(1, years+1):
        new_principal = formula(principal, acc_cmp_freq, acc_rate, year)
        if year % 2 == 0 and year != 0:
            values_to_display[year] = pretty_print_dollars(new_principal)
    display_table(values_to_display)


def make_field(content: any, length: int) -> str:
    content = str(content)
    if len(content) > length:
        content = content[:length - 2]
    return f"| {content.rjust(length)} |"


def make_line(length: int) -> str:
    start = "+-"
    end = "-+"
    middle = "-" * length
    return start + middle + end


def pretty_print_int(number: int) -> str:
    return f"{number:,}"

def pretty_print_dollars(number: float) -> str:
    if number < 0:
        return f"-${number * -1:,.2f}"
    return f"${number:,.2f}"

def find_dictionary_max_values(values):
    keys = list(values.keys())
    final_value = values[keys[-1]]
    value_max_length = len(final_value)
    key_max_length = len(str(keys[-1]))
    return key_max_length, value_max_length
    
def display_table(values):
    key_max, value_max = find_dictionary_max_values(values)
    # ugly. Sorry
    value_max += 0
    left_column_width = 4
    print(f"{make_line(left_column_width)}{make_line(value_max)}")
    print(f"{make_field('Year', left_column_width)}{make_field('Balance', value_max)}")
    print(f"{make_line(left_column_width)}{make_line(value_max)}")
    
    for key in values.keys():
        print(f"{make_field(key, left_column_width)}{make_field(values[key], value_max)}")
        
    print(f"{make_line(left_column_width)}{make_line(value_max)}")


simulate_account_balance_pp(341063.90672736865, 0.8450937437233716, 0, 8, 2)

# HOLY FUCK IT'S DONE