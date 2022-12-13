from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    list_infos = read(path)
    salarys = [
        int(salary["max_salary"])
        for salary in list_infos
        if salary["max_salary"].isdigit()
    ]
    return max(salarys)


def get_min_salary(path: str) -> int:
    list_infos = read(path)
    salarys = [
        int(salary["min_salary"])
        for salary in list_infos
        if salary["min_salary"].isdigit()
    ]
    return min(salarys)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if (
        ("min_salary" not in job or "max_salary" not in job)
        or (
            not str(job["min_salary"]).isnumeric()
            or not str(job["max_salary"]).isnumeric()
        )
        or (int(job["min_salary"]) > int(job["max_salary"]))
    ):
        raise ValueError("Invalid salaries")

    elif (
        not isinstance(salary, int)
        and not isinstance(salary, str)
        or (isinstance(salary, str) and not salary.isnumeric())
    ):
        raise ValueError("Invalid salary")

    return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
