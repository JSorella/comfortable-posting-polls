import os
from functions.messages import get_random_exit_message, get_random_prompt_message
from functions.votes_processor import VotesProcessor


if __name__ == '__main__':
    processor = VotesProcessor()
    print("\n-- PINK FLOYD 'COMFORTABLY POSTING' POLLS RESULTS DATA PROCESSOR --")
    while True:
        print("\n{}".format(get_random_prompt_message()))
        print("A - Get the most disliked albums ranking.")
        print("V - Calculate song votes.")
        print("S - Generate songs dictionary in JSON format.")
        print("Q - Quit this program.")
        choice = input("Enter your choice: ").upper()

        if choice == "A":
            processor.print_albums_ranking()
        elif choice == "S":
            processor.generate_songs_json()
        elif choice == "V":
            processor.calculate_votes()
        elif choice == "Q":
            break
        else:
            print("Invalid choice. Try again.")

    print("\n{}".format(get_random_exit_message()))
