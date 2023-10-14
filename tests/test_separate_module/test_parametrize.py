import pytest
from separate_module.calculator import Calculator


# Example of parametrize decorator:
# We will be able to pass list with tuples of arguments,
# that will be passed in our testing function
@pytest.mark.development
@pytest.mark.parametrize(
    "number1, number2, expected_result",
    [
        (2, 4, 6),
        (3, -1, 2),
        (5, 5, 10)

    ]
)
def test_example_with_parametrize(number1, number2, expected_result):
    calculation = Calculator(number1, number2).add()
    assert calculation == expected_result


@pytest.mark.skip("Test is skipped")
# Example of decorator for skipping:
# This test will be skipped during test session
def test_example_with_skip():
    calculation = Calculator(2, 5).multi()
    expected_result = 10
    assert calculation == expected_result


@pytest.mark.development
# Example of decorator that marks our test function by special environment:
# in this case - development. Flow for setting markers:
# 1. Add variable "markers" to file pytest.ini with value that
#    will be sequence of names our envs - development, production, stage, etc.
# 2. Use one of their values in our decorators
#    @pytest.mark.development
# 3. Use in command line addition argument "-k" and env name "development" or "stage", example:
#    pytest -v -s -k development tests/
def test_example_mark_development():
    calculation = Calculator(3, 4).subtract()
    expected_result = -1
    assert calculation == expected_result
    print("Development testing is ok")


@pytest.mark.stage
# Example of decorator that marks our test function by stage env
def test_example_mark_development():
    calculation = Calculator(10, 5).divide()
    expected_result = 2
    assert calculation == expected_result
    print("Stage testing is ok")
