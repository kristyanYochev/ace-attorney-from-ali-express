from typing import Optional


def color_control_sequence(text_color: str, text_style: str = "normal", background_color: Optional[str] = None) -> str:
    text_styles = {
        "normal": 0,
        "bold": 1,
        "light": 2,
        "italicized": 3,
        "underlined": 4,
        "blink": 5
    }

    text_colors = {
        "black": 30,
        "red": 31,
        "green": 32,
        "yellow": 33,
        "blue": 34,
        "purple": 35,
        "cyan": 36,
        "white": 37
    }

    background_colors = {
        "black": 40,
        "red": 41,
        "green": 42,
        "yellow": 43,
        "blue": 44,
        "purple": 45,
        "cyan": 46,
        "white": 47
    }

    control_sequence = f"\x1b[{text_styles[text_style]};{text_colors[text_color]}"
    if background_color is not None:
        control_sequence += f";{background_colors[background_color]}"
    control_sequence += "m"

    return control_sequence


RESET_COLOR_CONTROL_SEQUENCE = "\x1b[0;0m"
