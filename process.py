"""Function to process calculations"""


def needs_processing(text: str):
    """Figure out if an expression needs processing"""
    symbols = ["+", "-", "*", "/"]
    for symbol in symbols:
        if symbol in text:
            return True
    return False


def subprocess(texts: list):
    """Subprocess all operations"""
    new_texts = []
    for expression in texts:
        if needs_processing(expression):
            expression = process(expression)
        new_texts.append(float(expression))
    return new_texts


def process_multiplication(text: str):
    """Process a single multiplication statement."""
    if "*" in text:
        texts = text.split("*", maxsplit=1)
        texts = subprocess(texts)
        total = 1
        for expression in texts:
            total *= expression
        return total


def process_division(text: str):
    """Process a single multiplication statement."""
    if "/" in text:
        texts = text.split("/", maxsplit=1)
        texts = subprocess(texts)
        total = float(texts[0])
        texts.pop(0)
        for expression in texts:
            total /= float(expression)
        return total


def process_addition(text: str):
    """Process a single multiplication statement."""
    if "+" in text:
        texts = text.split("+", maxsplit=1)
        texts = subprocess(texts)
        total = 0
        for expression in texts:
            total += float(expression)
        return total


def process_subtraction(text: str):
    """Process a single multiplication statement."""
    if "-" in text:
        texts = text.split("-", maxsplit=1)
        texts = subprocess(texts)
        total = float(texts[0])
        texts.pop(0)
        for expression in texts:
            total -= float(expression)
        return total


def get_operation(text: str):
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
    # Program will only get to this point if there are no operations left
    return None


def process(text: str):
    """Process an expression"""
    operation = get_operation(text)
    if operation == "*":
        return process_multiplication(text)
    elif operation == "/":
        return process_division(text)
    elif operation == "+":
        return process_addition(text)
    elif operation == "-":
        return process_subtraction(text)
    return text


def calculate(text: str):
    """Convert numbers that end in .0 to an int"""
    try:
        num = process(text)
    except ArithmeticError:
        return "Whoops! Math Error!"
    except ValueError:
        return "Whoops! Math Error!"
    return str(num).rstrip(".0")


print(calculate("+"))
