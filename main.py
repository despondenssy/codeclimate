from engine import run_game
from games import brain_lcm, brain_progression

GAMES = {
    "1": brain_lcm,
    "2": brain_progression
}

def main():
    print("Choose a game:")
    print("1 - Least Common Multiple (LCM)")
    print("2 - Geometric Progression")

    choice = input("Enter the number of the game: ").strip()

    if choice in GAMES:
        run_game(GAMES[choice])
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()