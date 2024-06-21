import scraper
import get_world_achievements

if __name__ == "__main__":
    achievement_name, achievements_code = scraper.extract_achievements()
    world_achievements: list = get_world_achievements.get_completed_achievements()

    for name, achievement in zip(achievement_name, achievements_code):
        print(
            f"Name: {name} Code: {achievement} Completed: {achievement in world_achievements}"
        )

#    for achievement in world_achievements:
#        print(f"code: {achievement}")
#
