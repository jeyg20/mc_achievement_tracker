import json

with open(
    "/home/jeison/.local/share/atlauncher/instances/BetterMCFORGEBMC4/saves/bobby-fallback/advancements/3818f121-a7dd-43b1-a1fa-71a019c9faa3.json"
) as file:
    data = json.load(file)


def get_completed_achievements() -> list:
    complete_achievements = []

    for key, value in data.items():
        if isinstance(value, dict):
            complete_achievements.append(key)

    return complete_achievements
