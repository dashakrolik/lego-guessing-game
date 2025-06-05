from lego_api import get_random_set
# from game_logic import display_clues, check_guess

def main():
    lego_set = get_random_set()
    if not lego_set:
        print("Could not fetch LEGO set.")
        return

    print("🔍 Here’s a LEGO set pulled live from the Rebrickable API:")
    print(lego_set.summary())

if __name__ == "__main__":
    main()