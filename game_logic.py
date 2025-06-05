def display_clues(lego_set):
    print("\n🔍 Guess the LEGO set!")
    print(f"📅 Year: {lego_set['year']}")
    print(f"🧱 Piece Count: {lego_set['num_parts']}")
    print(f"🎭 Theme ID: {lego_set['theme_id']}")
    print(f"🧙 Minifigs: Unknown (placeholder)")  # You can extend this later

def check_guess(user_guess, correct_name):
    return user_guess.lower() in correct_name.lower()
