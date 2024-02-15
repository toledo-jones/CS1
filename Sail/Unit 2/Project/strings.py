


def pretty_print_dollars(number: float) -> str:
    if number < 0:
        return f"-${number * -1:,.2f}"
    return f"${number:,.2f}"


print(pretty_print_int(1000))
print(pretty_print_int(5))
print(pretty_print_int(547475874))
print(pretty_print_int(-84989))

print(pretty_print_dollars(1000.0))
print(pretty_print_dollars(5.99))
print(pretty_print_dollars(547475874))
print(pretty_print_dollars(-84989))
print(pretty_print_dollars(999.50))

assert (pretty_print_dollars(-544445.8075406007)) == "-$544,445.81"


def make_field(content: any, length: int) -> str:
    content = str(content)
    if len(content) > length - 2:
        content = content[:length - 2]
    return f"| {content} |"


def make_line(length: int) -> str:
    end = "+"
    middle = "-" * length
    return end + middle + end


def pretty_print_int(number: int) -> str:
    return f"{number:,}"