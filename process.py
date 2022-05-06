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


def process(text: str):
    """Process an expression"""
    if "-" in text:
        texts = text.split("-")
        texts = subprocess(texts)
        total = float(texts[0])
        texts.pop(0)
        for expression in texts:
            total -= float(expression)
        return total

    if "+" in text:
        texts = text.split("+")
        texts = subprocess(texts)
        total = 0
        for expression in texts:
            total += float(expression)
        return total

    if "/" in text:
        texts = text.split("/")
        texts = subprocess(texts)
        total = float(texts[0])
        texts.pop(0)
        for expression in texts:
            total /= float(expression)
        return total

    if "*" in text:
        texts = text.split("*")
        texts = subprocess(texts)
        total = 1
        for expression in texts:
            total *= expression
        return total


print(process("100*15/4+3-2"))
