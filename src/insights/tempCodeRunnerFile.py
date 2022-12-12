def get_unique_job_types(path: str) -> List[str]:
    list_infos = read(path)
    unique_job = list()
    for job in list_infos:
        if job not in unique_job:
            unique_job.append(job)
    return unique_job