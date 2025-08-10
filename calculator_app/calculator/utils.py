def format_result(result):
    if isinstance(result, float) and result.is_integer():
        return str(int(result))
    return str(result)
