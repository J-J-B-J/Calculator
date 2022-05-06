"""Function to __process calculations"""
from math import pow, pi, e
from tkinter import Tk, Frame, Label, RAISED, Entry
from decimal import Decimal as Dec


def _replace_symbols(text: str):
    """Replace pi with the actual value of pi, etc"""
    symbols = {"pi": pi, "e": e}
    for key, value in symbols.items():
        text = text.replace(key, str(value))
    return text


def _needs_processing(text: str):
    """Figure out if an expression needs processing"""
    symbols = ["+", "-", "*", "/", "^"]
    for symbol in symbols:
        if symbol in text:
            return True
    return False


def _get_operation(text: str):
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


class Calculator:
    """A class to manage the calculator"""
    def __init__(self):
        self.window = Tk()
        self.calculation = Entry()
        self.calculation.pack()
        self.result = Label(text=self._calculate(text=self.calculation.get()))
        self.result.pack()
        self.window.bind("<Return>", self._update_calculation)

    def _update_calculation(self, _):
        """Update the calculation result"""
        self.result["text"] = self._calculate(self.calculation.get())

    def _subprocess(self, texts: list):
        """Subprocess all operations"""
        new_texts = []
        for expression in texts:
            if _needs_processing(expression):
                expression = self._process(expression)
            new_texts.append(float(expression))
        return new_texts

    def _process_multiplication(self, text: str):
        """Process a single multiplication statement."""
        texts = self._subprocess(text.split("*", maxsplit=1))
        return float(Dec(str(texts[0])) * Dec(str(texts[1])))

    def _process_division(self, text: str):
        """Process a single division statement."""
        texts = self._subprocess(text.split("/", maxsplit=1))
        return float(Dec(str(texts[0])) / Dec(str(texts[1])))

    def _process_addition(self, text: str):
        """Process a single addition statement."""
        texts = self._subprocess(text.split("+", maxsplit=1))
        return float(Dec(str(texts[0])) + Dec(str(texts[1])))

    def _process_subtraction(self, text: str):
        """Process a single subtraction statement."""
        texts = self._subprocess(text.split("-", maxsplit=1))
        return float(Dec(str(texts[0])) - Dec(str(texts[1])))

    def _process_powers(self, text: str):
        """Process a single logarithmic statement."""
        texts = self._subprocess(text.split("^", maxsplit=1))
        return pow(texts[0], texts[1])

    def _process(self, text: str):
        """Process an expression"""
        operation = _get_operation(text)
        if operation == "*":
            return self._process_multiplication(text)
        elif operation == "/":
            return self._process_division(text)
        elif operation == "+":
            return self._process_addition(text)
        elif operation == "-":
            return self._process_subtraction(text)
        elif operation == "^":
            return self._process_powers(text)
        return text

    def _calculate(self, text: str):
        """Convert numbers that end in .0 to an int"""
        text = _replace_symbols(text)
        try:
            num = self._process(text)
            float(num)
        except ArithmeticError:
            if self.calculation.get() == "":
                return ""
            return "Whoops! Math Error!"
        except ValueError:
            if self.calculation.get() == "":
                return ""
            return "Whoops! Syntax Error!"
        return str(num).rstrip(".0")


Calculator().window.mainloop()
