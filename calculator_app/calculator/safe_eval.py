import ast
import operator

_allowed_binops = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.FloorDiv: operator.floordiv,
}

_allowed_unaryops = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}

def safe_eval(expr: str):
    """Вычисляет выражение безопасно."""
    try:
        node = ast.parse(expr, mode='eval')
    except Exception:
        raise ValueError("Синтаксическая ошибка")

    def _eval(n):
        if isinstance(n, ast.Expression):
            return _eval(n.body)
        elif isinstance(n, ast.Constant):
            if isinstance(n.value, (int, float)):
                return n.value
            raise ValueError("Только числа разрешены")
        elif isinstance(n, ast.BinOp):
            left = _eval(n.left)
            right = _eval(n.right)
            if type(n.op) in _allowed_binops:
                try:
                    return _allowed_binops[type(n.op)](left, right)
                except ZeroDivisionError:
                    raise ValueError("Деление на ноль")
            raise ValueError("Операция не разрешена")
        elif isinstance(n, ast.UnaryOp):
            operand = _eval(n.operand)
            if type(n.op) in _allowed_unaryops:
                return _allowed_unaryops[type(n.op)](operand)
            raise ValueError("Унарная операция не разрешена")
        else:
            raise ValueError("Недопустимый элемент")
    return _eval(node)
