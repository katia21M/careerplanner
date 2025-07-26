def get_personality_matches(personality):
    if "Creative" in personality:
        return ["UI/UX Designer", "Product Manager"]
    if "Analytical" in personality:
        return ["Data Scientist", "Security Analyst"]
    return ["Generalist"]
