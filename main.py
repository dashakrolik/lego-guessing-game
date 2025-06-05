from lego_api import get_random_set
from game_logic import display_clues, check_guess

def main():
    lego_set = get_random_set()
    if not lego_set:
        print("❌ Could not fetch LEGO set. Try again later.")
        return

    display_clues(lego_set)
    guess = input("💡 Your guess: ")

    if check_guess(guess, lego_set["name"]):
        print("✅ Correct! 🎉")
    else:
        print(f"❌ Nope. It was: {lego_set['name']}")

if __name__ == "__main__":
    main()
