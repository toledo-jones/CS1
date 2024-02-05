INITIAL_PRINCIPAL = 10000.0
YEARS = 5
ACCOUNT_RATE_1 = .027
ACCOUNT_RATE_2 = .0268
ACCOUNT_RATE_3 = .0266
ACCOUNT_CMP_FREQ_1 = 1
ACCOUNT_CMP_FREQ_2 = 12
ACCOUNT_CMP_FREQ_3 = 365


def amount_after_n_years(init_principal, acc_rate, acc_cmp_freq, years):
    return init_principal * (1 + acc_rate / acc_cmp_freq) ** (acc_cmp_freq * years)


amount_1 = amount_after_n_years(INITIAL_PRINCIPAL, ACCOUNT_RATE_1, ACCOUNT_CMP_FREQ_1, YEARS)
amount_2 = amount_after_n_years(INITIAL_PRINCIPAL, ACCOUNT_RATE_2, ACCOUNT_CMP_FREQ_2, YEARS)
amount_3 = amount_after_n_years(INITIAL_PRINCIPAL, ACCOUNT_RATE_3, ACCOUNT_CMP_FREQ_3, YEARS)


# These print states will give more insight into the final values of your account holdings.
# print(c1, c2, c3)
# print(max(c1, c2, c3))
print(f"Account option 1 will hold ${amount_1:,.2f}.")
print(f"Account option 2 will hold ${amount_2:,.2f}.")
print(f"Account option 3 will hold ${amount_3:,.2f}.")
print(f"The maximum amount that can be reached is "
        f"${max(amount_1, amount_2, amount_3):,.2f}.")