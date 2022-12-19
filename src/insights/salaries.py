from typing import Union, List, Dict
from src.insights.jobs import read


max_s = "max_salary"
min_s = "min_salary"


def get_max_salary(path: str) -> int:
    list_infos = read(path)
    salarys = [
        int(salary[max_s]) for salary in list_infos if salary[max_s].isdigit()
    ]
    return max(salarys)


def get_min_salary(path: str) -> int:
    list_infos = read(path)
    salarys = [
        int(salary[min_s]) for salary in list_infos if salary[min_s].isdigit()
    ]
    return min(salarys)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if min_s not in job or max_s not in job:
        raise ValueError("min_salary or max_salary does not exist")
    elif not str(job[min_s]).isdigit() or not str(job[max_s]).isdigit():
        raise ValueError("min_salary or max_salary are not integer values")
    elif int(job[min_s]) > int(job[max_s]):
        raise ValueError("min_salary cannot be higher than the max_salary")
    elif (
        not isinstance(salary, int)
        and not isinstance(salary, str)
        or (isinstance(salary, str) and not salary.isdigit())
    ):
        raise ValueError("Invalid salary value")

    return int(job[min_s]) <= int(salary) <= int(job[max_s])


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:

    salaries_in_range = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                salaries_in_range.append(job)
        except ValueError as err:
            print(err)

    return salaries_in_range


# [
#     {"max_salary": "0", "min_salary": "10"},
#     {"max_salary": "10", "min_salary": "100"},
#     {"max_salary": "10000", "min_salary": "200"},
#     {"max_salary": "15000", "min_salary": "0"},
#     {"max_salary": "1500", "min_salary": "0"},
#     {"max_salary": "-1", "min_salary": "10"},
# ]


# if min_s not in job or max_s not in job:
#         raise ValueError("min_salary or max_salary does not exist")
#     elif not str(job[min_s]).isdigit() or not str(job[max_s]).isdigit():
#         raise ValueError("min_salary or max_salary are not integer values")
#     elif int(job[min_s]) > int(job[max_s]):
#         raise ValueError("min_salary cannot be higher than the max_salary")
