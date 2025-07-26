def get_job_matches(skills, interests):
    # You’d call another service or DB here; mocking for now
    if "Python" in skills:
        return ["Backend Developer", "Data Analyst"]
    if "React" in skills or "Web" in interests:
        return ["Frontend Dev", "Fullstack Engineer"]
    return ["Tech Support"]
