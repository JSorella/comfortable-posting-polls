from functions.utils import get_tracks_in_json_format, save_dict_to_json_file, \
    get_absolute_path


class TracksJsonGenerator(object):
    @staticmethod
    def create(folder_path='data/albums/'):
        """
        Creates a JSON file.
        """
        tracks_in_str = input("Enter tracks separated by low dash (_): ")
        album_title = input("Enter album title: ")

        tracks = [track.strip() for track in tracks_in_str.split("_")]
        tracks_with_votes_parameters = get_tracks_in_json_format(tracks)
        album_json = {
            "album_title": album_title,
            "tracks": tracks_with_votes_parameters
        }
        file_path = get_absolute_path(
            '{}.json'.format(album_title.lower().replace(' ', '_')), folder_path
        )
        save_dict_to_json_file(album_json, file_path)
        print("Done! File should be saved here: {}".format(file_path))
