import os
from functions.messages import get_random_exit_message, get_random_prompt_message
from functions.procedures import calculate_votes, generate_songs_json, print_albums_ranking


if __name__ == '__main__':
    print("\n-- PINK FLOYD 'COMFORTABLE POSTING' POLLS RESULTS DATA PROCESSOR --")
    while True:
        print("\n{}".format(get_random_prompt_message()))
        print("A - Get the most disliked albums ranking.")
        print("V - Calculate song votes.")
        print("S - Generate songs dictionary in JSON format.")
        print("Q - Quit this program.")
        choice = input("Enter your choice: ").upper()

        if choice == "A":
            print_albums_ranking()
        elif choice == "S":
            generate_songs_json()
        elif choice == "V":
            calculate_votes()
        elif choice == "Q":
            break
        else:
            print("Invalid choice. Try again.")

    print("\n{}".format(get_random_exit_message()))
