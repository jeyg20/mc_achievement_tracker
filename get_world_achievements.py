import json

with open(
    "/home/jeison/.local/share/atlauncher/instances/BetterMCFORGEBMC4/saves/bobby-fallback/advancements/3818f121-a7dd-43b1-a1fa-71a019c9faa3.json"
) as file:
    data = json.load(file)


def get_world_achievements():
    complete_achievements: int = 0
    incomplete_achievements: int = 0

    for key, value in data.items():
        if isinstance(value, dict) and value.get("done") == True:
            complete_achievements += 1
        elif isinstance(value, dict) and value.get("done") == False:
            incomplete_achievements += 1

    return complete_achievements
