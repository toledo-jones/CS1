from math import e


def compound_interest(
        init_principal,
        acc_rate,
        acc_cmp_freq,
        years):
    if acc_cmp_freq == 0:
        formula = compound_continuously
    else:
        formula = compound_at_frequency
    return formula(init_principal, acc_cmp_freq, acc_rate, years)


def compound_at_frequency(principle, frequency, rate, years):
    # a = P(1+ r/n)^nt
    return principle * (1 + rate / frequency) ** (frequency * years)


def compound_continuously(principle, frequency, rate, years):
    # a = pe^rt
    return principle * e ** rate * years


def simulate_account_balance(
        init_principal,
        acc_rate,
        acc_cmp_freq,
        setup_fee,
        years):
    principal = init_principal - setup_fee
    for year in range(1, years+1):
        interest = principal * (1 + acc_rate / acc_cmp_freq)
        principal += interest
        if year % 2 == 0 and year != 0:
            print(f"{year} {principal}")


simulate_account_balance(10000.00, 0.025, 12, 25.00, 10)
