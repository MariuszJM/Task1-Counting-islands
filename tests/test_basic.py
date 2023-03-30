import pytest
from count_islands import count_islands_greedy


@pytest.mark.parametrize("count_islands_func", [count_islands_greedy])
def test_basic(count_islands_func, basic_test_case):
    input_matrix, expected_output = basic_test_case
    assert count_islands_func(input_matrix) == expected_output
