import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_success(self):
        assert self.calc.multiply(self, 3, 4) == 12

    def test_division_success(self):
        assert self.calc.division(self, 10, 2) == 5

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 8, 1) == 7

    def test_adding_success(self):
        assert self.calc.adding(self, 9, 1) == 10

    def test_adding_unsuccess(self):

        assert self.calc.adding(self, 1, 1) == 3

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def teardown(self):
        print('Выполнение метода Teardown')








































