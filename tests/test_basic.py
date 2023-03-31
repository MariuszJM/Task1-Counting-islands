import pytest
from count_islands import count_islands_dfs, count_islands_bfs
import copy


@pytest.mark.parametrize("count_islands_func", [count_islands_dfs, count_islands_bfs])
def test_basic(count_islands_func, test_cases):
    input_matrix, expected_output = copy.deepcopy(test_cases)
    assert count_islands_func(input_matrix) == expected_output
