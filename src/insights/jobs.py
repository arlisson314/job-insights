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
    return {job["job_type"] for job in list_infos}


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    return [job for job in jobs if job["job_type"] == job_type]


if __name__ == "__main__":
    read()
