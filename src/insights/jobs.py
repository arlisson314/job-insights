from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf-8") as file:
        infos = csv.DictReader(file)
        return [info for info in infos]


def get_unique_job_types(path: str) -> List[str]:
    list_infos = read(path)
    unique_job = set()
    for job in list_infos:
        unique_job.add(job["job_type"])
    return unique_job


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
