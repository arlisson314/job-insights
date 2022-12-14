from typing import List, Dict
from src.insights.jobs import read

indt = "industry"


def get_unique_industries(path: str) -> List[str]:
    list_infos = read(path)
    return {industry[indt] for industry in list_infos if industry[indt]}


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    return [job for job in jobs if job[indt] == industry]
