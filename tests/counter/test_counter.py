from src.pre_built.counter import count_ocurrences
import pytest


def test_counter():
    assert (count_ocurrences("data/jobs.csv", "python")) == 1639

    assert (count_ocurrences("data/jobs.csv", "javascript")) != 22
    assert (count_ocurrences("data/jobs.csv", "python")) != 140

    assert (count_ocurrences("data/jobs.csv", "Comed!ante")) == 0
    with pytest.raises(FileNotFoundError):
        count_ocurrences("non-existent-file.txt", "Arilsson")
