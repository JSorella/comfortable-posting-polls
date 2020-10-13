import glob
import os

from utils import get_fixture_content, get_tracks_in_json_format, save_dict_to_json_file


def print_albums_ranking():
    albums = get_fixture_content('data/albums_ratings.json')
    ranking = []
    for album in albums:
        raw_score = album["positive_votes"] - album["negative_votes"]
        ranking.append((album["name"], raw_score))

    ranking.sort(key=lambda item: item[1])

    print("Most disliked albums ranking:")
    for item in ranking:
        print("  * {}: {}".format(*item))


def generate_songs_json():
    tracks_in_str = input("Enter tracks separated by commas (,): ")
    album_title = input("Enter album title: ").lower().replace(' ', '_')
    tracks = [track.strip() for track in tracks_in_str.split(",")]
    tracks_with_votes_parameters = get_tracks_in_json_format(tracks)
    file_path = 'data/albums/{}.json'.format(album_title)
    save_dict_to_json_file(tracks_with_votes_parameters, file_path)
    print("Done! File should be saved here: {}".format(file_path))


def calculate_votes():
    calculate_albums_votes()
    calculate_tracks_votes()


def calculate_albums_votes():
    total_positive_votes = 0
    total_negative_votes = 0
    albums = get_fixture_content('data/albums_ratings.json')

    for album in albums:
        total_positive_votes += album["positive_votes"]
        total_negative_votes += album["negative_votes"]

    print("* Total positive votes for albums: {}".format(total_positive_votes))
    print("* Total negative votes for albums: {}".format(total_negative_votes))
    print("* Total votes for albums: {}".format(total_positive_votes + total_negative_votes))


def calculate_tracks_votes():
    total_positive_votes = 0
    total_negative_votes = 0

    path = 'data/albums/'
    for filename in glob.glob(os.path.join(path, '*.json')):
        album_tracks = get_fixture_content(filename)

        for track in album_tracks:
            total_positive_votes += track['positive_votes']
            total_negative_votes += track['negative_votes']

    print("* Total positive votes for tracks: {}".format(total_positive_votes))
    print("* Total negative votes for tracks: {}".format(total_negative_votes))
    print("* Total votes for tracks: {}".format(total_positive_votes + total_negative_votes))
