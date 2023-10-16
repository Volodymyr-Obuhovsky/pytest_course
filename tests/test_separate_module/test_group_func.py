import pytest

from contextlib import nullcontext as without_exception
from pytest import raises
from separate_module.calculator import Calculator


# Example group united tests by class
@pytest.mark.development
class TestCalculator:

    # Example test with expected raised exception and
    # how this exception is handled
    @pytest.mark.parametrize(
        "number1, number2, expected_result",
        [
            (2, 4, 6),
            (3, -1, 2),
            (5, "4", 10)  # expect that in this case will be raised exception TypeError

        ],
        ids=str
    )
    def test_add(self, number1, number2, expected_result):
        # There will be raised exception TypeError by pytest in all cases inside context manager "with"
        # if ,in our case, exception will be raised by self -> test will be passed
        # without exception -> test will be fallen
        with raises(TypeError):
            calculation = Calculator(number1, number2).add()
            print(calculation)
            assert calculation == expected_result

    # Example test with expected exception in some cases and without exceptions
    @pytest.mark.parametrize(
        "number1, number2, expected_result, expected_exception",
        [
            (6, 3, 2, without_exception()),
            (10, -1, -10, without_exception()),
            (5, 0, 1, raises(ZeroDivisionError))

        ],
        ids=str
    )
    def test_divide(self, number1, number2, expected_result, expected_exception):
        # If in case there is no raised exception by self and param - without_exception() -> test will be passed
        # if there will be raised exception by self and param - raises() - test also will be passed
        with expected_exception:
            calculation = Calculator(number1, number2).divide()
            print(calculation)
            assert calculation == expected_result
