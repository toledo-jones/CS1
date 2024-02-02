c1 = 10000.0 * (1 + 0.027) ** 5
c2 = 10000.0 * (1 + 0.0268 / 12) ** (5 * 12)
c3 = 10000.0 * (1 + 0.0266 / 365) ** (5 * 365)
print(c1, c2, c3)
print(max(c1, c2, c3))

INITIAL_PRINCIPAL = 10000.0
YEARS = 5
ACCOUNT_RATE_1 = .027
ACCOUNT_RATE_2 = .0268
ACCOUNT_RATE_3 = .0266
ACCOUNT_CMP_FREQ_1 = 1
ACCOUNT_CMP_FREQ_2 = 12
ACCOUNT_CMP_FREQ_3 = 365

def amount_after_n_years(init_principal, acc_rate, acc_cmp_freq, years):
    