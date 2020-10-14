import os

from functions.utils import get_fixture_content, get_tracks_in_json_format, save_dict_to_json_file
from pathlib import Path

DIR = os.path.dirname(os.path.abspath(__file__))


class VotesProcessor(object):

    def __init__(self):
        self.album_votes = None
        self.track_votes = None
        self.data = None
        self.album_positive_k = 1
        self.album_negative_k = 1
        self.album_k = 1
        self.track_positive_k = 1
        self.track_negative_k = 1
        self.track_k = 1

    def print_albums_ranking(self):
        ranking = []
        if not self.data:
            self._load_data()

        for album in self.data:
            raw_score = album["positive_votes"] - album["negative_votes"]
            ranking.append((album["name"], raw_score))

        ranking.sort(key=lambda item: item[1])

        print("Most disliked albums ranking:")
        for album in ranking:
            print("  * {}: {}".format(*album))

    def _print_tracks_ranking(self):
        ranking = []

        for album in self.data:
            album_raw_score = album["positive_votes"] * self.album_positive_k \
                              - album["negative_votes"] * self.album_negative_k
            album_songs_weight_ratio = 1 / len(album["tracks"])
            for track in album["tracks"]:
                album_score = album_raw_score * self.album_k * album_songs_weight_ratio
                track_raw_score = album_score + track["positive_votes"] * self.track_positive_k \
                                  - track["negative_votes"] * self.track_negative_k
                ranking.append((track["name"], track_raw_score))

        ranking.sort(key=lambda item: item[1])

        print("\nMost disliked songs/tracks ranking:\n")
        for song in ranking:
            print("  * {}: {}".format(*song))

    def generate_songs_json(self):
        """
        TODO: Refactor this to other class.
        """
        tracks_in_str = input("Enter tracks separated by commas (,): ")
        album_title = input("Enter album title: ").lower().replace(' ', '_')

        tracks = [track.strip() for track in tracks_in_str.split(",")]
        tracks_with_votes_parameters = get_tracks_in_json_format(tracks)
        file_path = self._get_data_file_path('albums/{}.json'.format(album_title))
        save_dict_to_json_file(tracks_with_votes_parameters, file_path)
        print("Done! File should be saved here: {}".format(file_path))

    def calculate_votes(self):
        self.album_votes = self._calculate_albums_votes()
        self.track_votes = self._calculate_tracks_votes()
        self._correct_ratios()

        self._print_total_votes()
        self._print_tracks_ranking()

    def _calculate_albums_votes(self):
        total_positive_votes = 0
        total_negative_votes = 0

        if not self.data:
            self._load_data()

        for album in self.data:
            total_positive_votes += album["positive_votes"]
            total_negative_votes += album["negative_votes"]

        return total_positive_votes, total_negative_votes

    def _calculate_tracks_votes(self):
        total_positive_votes = 0
        total_negative_votes = 0

        if not self.data:
            self._load_data()

        for album in self.data:
            for track in album["tracks"]:
                total_positive_votes += track['positive_votes']
                total_negative_votes += track['negative_votes']

        return total_positive_votes, total_negative_votes

    def _correct_ratios(self):
        self.album_positive_k, self.album_negative_k = self._correct_ratio(self.album_votes)
        self.track_positive_k, self.track_negative_k = self._correct_ratio(self.track_votes)

        total_votes = (sum(self.album_votes), sum(self.track_votes))
        self.album_k, self.track_k = self._correct_ratio(total_votes)

    @staticmethod
    def _correct_ratio(votes):
        positive_ratio = 1
        negative_ratio = 1

        positives, negatives = votes
        if positives > negatives:
            negative_ratio = positives / negatives
        elif negatives > positives:
            positive_ratio = negatives / positives

        return positive_ratio, negative_ratio

    def _load_data(self):
        """
        Load data from JSON files.
        """
        self.data = []
        albums = self._get_albums()

        for album in albums:
            album_file_name = album["name"].lower().replace(" ", "_")
            album_file_path = self._get_data_file_path('albums/{}.json'.format(album_file_name))
            album["tracks"] = get_fixture_content(album_file_path)
            self.data.append(album)

    def _print_total_votes(self):
        for votes, type_of_vote in [(self.album_votes, "albums"), (self.track_votes, "tracks")]:
            positives, negatives = votes
            print("* Total positive votes for {}: {}".format(type_of_vote, positives))
            print("* Total negative votes for {}: {}".format(type_of_vote, negatives))
            print("* Total votes for {}: {}".format(type_of_vote, positives + negatives))

    @staticmethod
    def _get_data_file_path(file_name):
        return (Path(DIR) / '..' / 'data' / file_name).resolve()

    def _get_albums(self):
        return get_fixture_content(self._get_data_file_path('albums_ratings.json'))
