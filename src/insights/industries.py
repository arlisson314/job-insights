from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    list_infos = read(path)
    unique_industries = set()
    for industry in list_infos:
        if industry["industry"]:
            unique_industries.add(industry["industry"])
    return unique_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    return [job for job in jobs if job["industry"] == industry]
