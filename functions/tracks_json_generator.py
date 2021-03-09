import os
from functions.utils import get_tracks_in_json_format, save_dict_to_json_file
from pathlib import Path

DIR = os.path.dirname(os.path.abspath(__file__))


class TracksJsonGenerator(object):
    @staticmethod
    def create(folder_path='data/albums/'):
        """
        Creates a JSON file.
        """
        tracks_in_str = input("Enter tracks separated by commas (,): ")
        album_title = input("Enter album title: ").lower().replace(' ', '_')

        tracks = [track.strip() for track in tracks_in_str.split(",")]
        tracks_with_votes_parameters = get_tracks_in_json_format(tracks)
        file_path = TracksJsonGenerator._get_data_file_path(
            '{}{}.json'.format(folder_path, album_title)
        )
        save_dict_to_json_file(tracks_with_votes_parameters, file_path)
        print("Done! File should be saved here: {}".format(file_path))

    @staticmethod
    def _get_data_file_path(file_path):
        return (Path(DIR) / '..' / file_path).resolve()
