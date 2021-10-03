def clamp(value: int, lower_bound: int, upper_bound: int) -> int:
    if value < lower_bound:
        return lower_bound
    if value > upper_bound:
        return upper_bound
    return value
