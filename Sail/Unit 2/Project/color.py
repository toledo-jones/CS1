def time_color(time):
    if time > 10:
        return 'black'
    elif time >= 6:
        return 'orange'
    else:
        return 'red'


# Assert statements to check validity of code
assert time_color(25) == 'black'
assert time_color(10) == 'orange'
assert time_color(6) == 'orange'
assert time_color(5) == 'red'
assert time_color(3) == 'red'
assert time_color(-100) == 'red'

COLORS = ["red", "orange", "blue", "green", "yellow", "pink", "black", "gray",
          "purple"]


def is_correct(
        bg_color: str,
        text_color: str,
        text: str,
        input_color: str,
        mode: str) -> bool:
    def neither(_bg_color, _text_color, _text, _input_color):
        if _input_color != _bg_color and _input_color != _text_color and _input_color != _text:
            return _input_color in COLORS
        return False

    mode_mapping = {'Background Color': input_color == bg_color,
                    'Text Color': input_color == text_color,
                    'Text': input_color == text,
                    'Neither': neither(bg_color, text_color, text, input_color)}

    return mode_mapping.get(mode)


assert is_correct('black', 'red', 'blue', 'blue', 'Background Color') == False
assert is_correct('black', 'red', 'blue', 'black', 'Background Color') == True
assert is_correct('black', 'red', 'blue', 'red', 'Text Color') == True
assert is_correct('black', 'red', 'blue', 'blue', 'Text Color') == False
assert is_correct('black', 'red', 'blue', 'pink', 'Text') == False
assert is_correct('black', 'red', 'blue', 'red', 'Text') == False
assert is_correct('black', 'red', 'blue', 'red', 'Neither') == False
assert is_correct('black', 'red', 'blue', 'pink', 'Neither') == True
