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
    return list(unique_job)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    return [job for job in jobs if job["job_type"] == job_type]


# [{'id': 1, 'job_type': 'PART_TIME'}, {'id': 2, 'job_type': 'PART_TIME'}]
