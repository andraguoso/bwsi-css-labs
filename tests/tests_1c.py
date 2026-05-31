import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_MSS():
    assert max_subarray_sum([1, 2, 1]) == 3
    assert max_subarray_sum([0, 0, 0]) == 0
    assert max_subarray_sum([-1, 2, -1, 2]) == 3

if __name__ == "__main__":
    pytest.main()