import json

def get_completed_achievements(url) -> list:
    with open(url) as file:
        data = json.load(file)
    
    complete_achievements = []

    for key, value in data.items():
        if isinstance(value, dict):
            complete_achievements.append(key)

    return complete_achievements
