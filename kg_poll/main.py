from functions.messages import get_random_exit_message, get_random_prompt_message
from functions.tracks_json_generator import TracksJsonGenerator
from functions.utils import get_fixture_content
from functions.votes_processor import VotesProcessor
from prettytable import PrettyTable


def calculate_and_print_votes(json_path):
    tracks = get_fixture_content(json_path)
    positive_votes = 0
    negative_votes = 0
    table = PrettyTable(['Track', 'Up Votes', 'Down Votes', 'Total Votes', 'Score', 'Abs.Score'])

    for track in tracks:
        difference = int(track['positive_votes']) - int(track['negative_votes'])
        sum_votes = int(track['positive_votes']) + int(track['negative_votes'])
        table.add_row(
            [track['name'], track['positive_votes'], track['negative_votes'],
             sum_votes, difference, abs(difference)]
        )
        positive_votes += track['positive_votes']
        negative_votes += track['negative_votes']

    table.align = "c"
    table.align["Track"] = "l"
    table.reversesort = True

    print('\nTotal votes from "Most liked" poll: {}'.format(positive_votes))
    print('Total votes from "Least liked" poll: {}'.format(negative_votes))

    print('\nMOST LIKED TRACKS TOP 5')
    print(table.get_string(
        start=0, end=5, sortby='Score', fields=['Track', 'Up Votes', 'Down Votes', 'Score'])
    )
    print('\nMOST DISLIKED TRACKS TOP 5')
    print(table.get_string(
        start=0, end=5, sortby='Score', reversesort=False,
        fields=['Track', 'Up Votes', 'Down Votes', 'Score'])
    )

    print('\nMOST POPULAR TRACKS TOP 5 (Tracks with most votes from both polls)')
    print(table.get_string(
        start=0, end=5, sortby='Total Votes',
        fields=['Track', 'Up Votes', 'Down Votes', 'Total Votes'])
    )

    print('\nMOST UNPOPULAR TRACKS TOP 5 (Tracks with least votes from both polls)')
    print(table.get_string(
        start=0, end=5, sortby='Total Votes', reversesort=False,
        fields=['Track', 'Up Votes', 'Down Votes', 'Total Votes'])
    )

    print('\nMOST NEUTRAL TRACKS TOP 5 (Tracks where votes difference are closest to zero)')
    print(table.get_string(
        start=0, end=5, sortby='Abs.Score', reversesort=False,
        fields=['Track', 'Up Votes', 'Down Votes', 'Abs.Score'])
    )

    print('\nMOST LIKED TRACKS - FULL REPORT')
    print(table.get_string(
        sortby='Score', fields=['Track', 'Up Votes', 'Down Votes', 'Score'])
    )


if __name__ == '__main__':
    processor = VotesProcessor()
    print("\n-- KING GIZZARD & THE LIZARD WIZARD SH!T POSTING POLLS RESULTS DATA PROCESSOR --")
    while True:
        print("\nWelcome to an Altered Future.")
        print("C - Calculate polls votes.")
        #print("S - Generate songs dictionary in JSON format.")
        print("Q - Quit this program.")
        choice = input("Enter your choice: ").upper()

        if choice == "S":
            TracksJsonGenerator.create('kg_poll/')
        elif choice == "C":
            calculate_and_print_votes('./kglw.json')
        elif choice in ["Q", "QUIT"]:
            break
        else:
            print("Invalid choice. Try again.")

    print("\n{}".format(get_random_exit_message()))
