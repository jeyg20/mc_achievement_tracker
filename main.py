import scraper
import get_world_achievements
import select_file

if __name__ == "__main__":
    selected_file = select_file.select_file()
    if selected_file:
        print(f"Selected file: {selected_file}")
    else:
        print("No file selected or operation canceled")
    
    achievement_name, achievements_code = scraper.extract_achievements()
    world_achievements: list = get_world_achievements.get_completed_achievements(selected_file)

    for name, achievement in zip(achievement_name, achievements_code):
        print(
            f"Name: {name} Code: {achievement} Completed: {achievement in world_achievements}"
        )
