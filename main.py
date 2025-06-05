from lego_api import get_random_set

def main():
    print("🧩 Welcome to the LEGO Set Guessing Game!")
    score = 0
    play_again = "y"

    while play_again.lower() == "y":
        lego_set = get_random_set()
        if not lego_set:
            print("❌ Couldn't fetch a set. Try again later.")
            continue

        print("\n🔍 Clues:")
        print(f"📅 Year: {lego_set.year}")
        print(f"🧱 Pieces: {lego_set.piece_count}")
        print(f"🎭 Theme: {lego_set.theme}")
        print("❓ Set Name: ???")

        attempts = 3
        while attempts > 0:
            guess = input(f"\n💡 Guess the set name ({attempts} tries left): ").strip().lower()
            if guess in lego_set.name.lower():
                print("✅ Correct! 🎉")
                score += 1
                break
            else:
                print("❌ Nope.")
                attempts -= 1

        if attempts == 0:
            print(f"😿 The correct answer was: {lego_set.name}")

        print(f"📊 Current Score: {score}")
        play_again = input("\n🔁 Play again? (y/n): ").strip()

    print(f"\n🏁 Final Score: {score}")
    print("Thanks for playing! 🧱")

if __name__ == "__main__":
    main()
