from app.calculator import Calculator
import pytest


class Test_Calculator:
    def setup(self):
        self.calc = Calculator

    def test_multiply(self):
        assert self.calc.multiply(3, 4) == 12
        assert self.calc.multiply(-2, 5) == -10
        assert self.calc.multiply(0, 100) == 0

    def test_division(self):
        assert self.calc.division(10, 2) == 5
        assert self.calc.division(-12, 4) == -3
        assert self.calc.division(0, 10) == 0

    def test_subtraction(self):
        assert self.calc.subtraction(5, 3) == 2
        assert self.calc.subtraction(0, 10) == -10
        assert self.calc.subtraction(-5, -3) == -2

    def test_adding(self):
        assert self.calc.adding(5, 3) == 8
        assert self.calc.adding(0, 10) == 10
        assert self.calc.adding(-5, -3) == -8
