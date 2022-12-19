from src.pre_built.sorting import sort_by

jobs = [
    {
        "date_posted": "2022-12-19",
        "max_salary": 5000,
        "min_salary": 1500,
    },
    {
        "date_posted": "2022-12-15",
        "max_salary": 15000,
        "min_salary": 100,
    },
    {
        "date_posted": "2022-12-10",
        "max_salary": 3000,
        "min_salary": 1000,
    },
]

jobs_sorted_by_max_salary = [
    {
        "date_posted": "2022-12-15",
        "max_salary": 15000,
        "min_salary": 100,
    },
    {
        "date_posted": "2022-12-19",
        "max_salary": 5000,
        "min_salary": 1500,
    },
    {
        "date_posted": "2022-12-10",
        "max_salary": 3000,
        "min_salary": 1000,
    },
]

jobs_sorted_by_min_salary = [
    {
        "date_posted": "2022-12-15",
        "max_salary": 15000,
        "min_salary": 100,
    },
    {
        "date_posted": "2022-12-10",
        "max_salary": 3000,
        "min_salary": 1000,
    },
    {
        "date_posted": "2022-12-19",
        "max_salary": 5000,
        "min_salary": 1500,
    },
]


def test_sort_by_criteria():
    sort_by(jobs, "max_salary")
    assert (jobs) == jobs_sorted_by_max_salary

    sort_by(jobs, "min_salary")
    assert (jobs) == jobs_sorted_by_min_salary
    assert (jobs) != jobs_sorted_by_max_salary
