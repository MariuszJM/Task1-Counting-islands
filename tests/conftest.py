import pytest


@pytest.fixture(
    params=[
        ([[0, 1, 0], [0, 0, 0], [0, 1, 1]], 2),
        ([[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]], 3),
        ([[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 0, 1]], 2),
        ([[]], 0),
        ([], 0),
        (
            [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
            ],
            0,
        ),
        (
            [
                [1, 1, 1],
                [1, 1, 1],
                [1, 1, 1],
            ],
            1,
        ),
        (
            [
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1],
            ],
            3,
        ),
        (
            [
                [1, 0, 1],
                [0, 1, 0],
                [1, 0, 1],
            ],
            5,
        ),
        (
            [
                [1, 0, 0, 1, 0, 0, 0, 1, 1, 1],
                [1, 0, 0, 1, 1, 0, 0, 1, 1, 0],
                [0, 1, 1, 0, 1, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
                [1, 1, 0, 1, 1, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
                [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
                [0, 1, 0, 1, 1, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
                [1, 1, 1, 1, 0, 0, 0, 1, 0, 0],
            ],
            19,
        ),
    ]
)
def test_cases(request):
    return request.param
