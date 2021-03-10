from functions.messages import get_random_exit_message
from functions.tracks_json_generator import TracksJsonGenerator
from functions.utils import get_fixture_content, get_file_names_in_folder
from functions.votes_processor import VotesProcessor
from prettytable import PrettyTable


def calculate_and_print_votes(folder_path):
    total_positive_votes = 0
    total_negative_votes = 0
    file_names = get_file_names_in_folder(folder_path, 'json')
    table = PrettyTable(
        ['Track', 'Up Votes', 'Down Votes', 'Total Votes', 'Score', 'Abs.Score']
    )
    album_table = PrettyTable(['Album', 'Up Votes', 'Down Votes', 'Score'])

    for file_name in file_names:
        album_data = get_fixture_content(file_name, folder_path)
        tracks = album_data['tracks']
        album_positive_votes = 0
        album_negative_votes = 0

        for track in tracks:
            difference = int(track['positive_votes']) - int(track['negative_votes'])
            sum_votes = int(track['positive_votes']) + int(track['negative_votes'])
            table.add_row(
                [track['name'], track['positive_votes'], track['negative_votes'],
                 sum_votes, difference, abs(difference)]
            )
            album_positive_votes += track['positive_votes']
            album_negative_votes += track['negative_votes']

        album_table.add_row(
            [album_data['album_title'], album_positive_votes, album_negative_votes,
             int(album_positive_votes) - int(album_negative_votes)]
        )
        total_positive_votes += album_positive_votes
        total_negative_votes += album_negative_votes

    table.align = "c"
    table.align["Track"] = "l"
    table.reversesort = True

    print('\nTotal votes from "Most liked" poll: {}'.format(total_positive_votes))
    print('Total votes from "Least liked" poll: {}'.format(total_negative_votes))

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

    print('\nALBUMS TOTAL SCORE')
    print(album_table.get_string(sortby='Score'))


if __name__ == '__main__':
    processor = VotesProcessor()
    print("\n-- KING GIZZARD & THE LIZARD WIZARD SH!T POSTING POLLS RESULTS DATA PROCESSOR --")
    while True:
        print("\nWelcome to an Altered Future.")
        print("C - Calculate polls votes.")
        print("G - Generate songs dictionary in JSON format.")
        print("Q - Quit this program.")
        choice = input("Enter your choice: ").upper()

        if choice == "G":
            TracksJsonGenerator.create('kg_poll/albums')
        elif choice == "C":
            calculate_and_print_votes('kg_poll/albums')
        elif choice in ["Q", "QUIT"]:
            break
        else:
            print("Invalid choice. Try again.")

    print("\n{}".format(get_random_exit_message()))
