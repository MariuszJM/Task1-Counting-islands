import pytest


@pytest.fixture(params=[
    (
        [
            [0, 1, 0],
            [0, 0, 0],
            [0, 1, 1]
        ],
        2
    ),
    (
        [
            [0, 0, 0, 1],
            [0, 0, 1, 0],
            [0, 1, 0, 0]
        ],
        3
    ),
    (
        [
            [0, 0, 0, 1],
            [0, 0, 1, 1],
            [0, 1, 0, 1]
        ],
        2
    )
])
def basic_test_case(request):
    return request.param