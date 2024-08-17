def bool_to_symbol(value):
    if isinstance(value, bool):
        return '○' if value else '×'
    return value
