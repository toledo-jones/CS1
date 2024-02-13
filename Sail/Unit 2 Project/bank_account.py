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
    from math import e
    # a = pe^rt
    return principle * e ** (rate * years)


def simulate_account_balance(
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

    for year in range(1, years+1):
        new_principal = formula(principal, acc_cmp_freq, acc_rate, year)
        if year % 2 == 0 and year != 0:
            print(f"{year} {round(new_principal, 2)}")


simulate_account_balance(592422.7803677524,
                         0.38452481654391935,
                         0,
                         13,
                         15)

print("line 1 should read: 2 1278251.27")
