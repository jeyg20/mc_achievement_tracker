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

    print(f"{'NAME' :<35} {'CODE':^35} {'COMPLETED':>32}")
    for name, achievement in zip(achievement_name, achievements_code):
        print(
            f"{name :<35} {achievement :<60} {achievement in world_achievements}"
        )
