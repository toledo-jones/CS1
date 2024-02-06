author_name = "Sasha"
author_lastname = "Bedregal"
author_age = 24
author_birthyear = 1998
first_work_year = 2018
second_work_year = 2020
third_work_year = 2020
award_1 = "Goodreads Choice Award for Best Memoir & Autobiography"
college = "Yale"

print(f"{(author_name + ' ' + author_lastname).upper().center(65)}")
print("")
print(f"{author_name} {author_lastname}, ________________________________________,"
      f" she had already published her first book of poems and a memoir that earned her a {award_1}."
      f" {author_name} is currently pursuing her MFA in English at {college}.")


print(f"{author_name} {author_lastname}, {author_age}, published her first short story when was {first_work_year - author_birthyear}")

"""
Expected output: 

Sasha Bedregal, 24, published her first short story when she was 20.
At 22, she had already published her first book of poems and a memoir
that earned her a Goodreads Choice Award for Best Memoir & Autobiography.
Sasha is currently pursuing her MFA in English at Yale.

"""


