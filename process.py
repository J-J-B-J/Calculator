"""Function to __process calculations"""

from math import pow, pi, e


def replace_symbols(text: str):
    """Replace pi with the actual value of pi, etc"""
    symbols = {"pi": pi, "e": e}
    for key, value in symbols.items():
        text = text.replace(key, str(value))
    return text


def __needs_processing(text: str):
    """Figure out if an expression needs processing"""
    symbols = ["+", "-", "*", "/", "^"]
    for symbol in symbols:
        if symbol in text:
            return True
    return False


def __subprocess(texts: list):
    """Subprocess all operations"""
    new_texts = []
    for expression in texts:
        if __needs_processing(expression):
            expression = __process(expression)
        new_texts.append(float(expression))
    return new_texts


def __process_multiplication(text: str):
    """Process a single multiplication statement."""
    texts = __subprocess(text.split("*", maxsplit=1))
    return texts[0] * texts[1]


def __process_division(text: str):
    """Process a single division statement."""
    texts = __subprocess(text.split("/", maxsplit=1))
    return texts[0] / texts[1]


def __process_addition(text: str):
    """Process a single addition statement."""
    texts = __subprocess(text.split("+", maxsplit=1))
    return texts[0] + texts[1]


def __process_subtraction(text: str):
    """Process a single subtraction statement."""
    texts = __subprocess(text.split("-", maxsplit=1))
    return texts[0] - texts[1]


def __process_powers(text: str):
    """Process a single logarithmic statement."""
    texts = __subprocess(text.split("^", maxsplit=1))
    return pow(texts[0], texts[1])


def __get_operation(text: str):
    """Get the first operation needed"""
    symbols_1 = ["+", "-"]
    symbols_2 = ["*", "/"]
    for character in text:
        for symbol in symbols_1:
            if character == symbol:
                return symbol
    # Program will only get to this point if no operation from * or / has
    # been found yet
    for character in text:
        for symbol in symbols_2:
            if character == symbol:
                return symbol

    for character in text:
        if character == "^":
            return "^"
    # Program will only get to this point if there are no operations left
    return None


def __process(text: str):
    """Process an expression"""
    operation = __get_operation(text)
    if operation == "*":
        return __process_multiplication(text)
    elif operation == "/":
        return __process_division(text)
    elif operation == "+":
        return __process_addition(text)
    elif operation == "-":
        return __process_subtraction(text)
    elif operation == "^":
        return __process_powers(text)
    return text


def calculate(text: str):
    """Convert numbers that end in .0 to an int"""
    text = replace_symbols(text)
    try:
        num = __process(text)
    except ArithmeticError:
        return "Whoops! Math Error!"
    except ValueError:
        return "Whoops! Syntax Error!"
    return str(num).rstrip(".0")


print(calculate("pi*2"))
