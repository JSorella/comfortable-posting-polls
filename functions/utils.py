import json
import os
from pathlib import Path

DIR = os.path.dirname(os.path.abspath(__file__))


def file_reader(path):
    """
    Given a file path, reads the file content.
    :param path:    String      Path of the file to read
    :return:        String      File content
    """
    with open(path, 'r', encoding='utf-8') as fh:
        return fh.read()


def file_writer(path, content):
    """
    Given a file path, creates/writes a file.
    :param path:        String      Path of the file to save.
    :param content:     String      Content to write into the file.
    """
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(content)


def get_fixture_content(payload_filename, folder_path=None):
    """
    Given a fixture filename, returns its content.
    :param payload_filename:    String      Name of the payload to load.
    :param folder_path:         String      (Optional) Containing folder for the file.
    :return:                    Dict        Payload loaded as a dict
    """
    file_path = get_absolute_path(payload_filename, folder_path)
    file_content = file_reader(file_path)

    return json.loads(file_content)


def get_file_names_in_folder(folder_path, filter_extension=None):

    file_names = os.listdir(get_absolute_path(folder_path))

    if filter_extension:
        file_names = [
            filename for filename in file_names if filename.endswith(
                '.{}'.format(filter_extension)
            )
        ]

    return file_names


def get_tracks_in_json_format(tracks):
    tracks_in_json_format = []
    for track in tracks:
        if track:
            data = {
                "name": track,
                "positive_votes": 0,
                "negative_votes": 0
            }
            tracks_in_json_format.append(data)

    return tracks_in_json_format


def save_dict_to_json_file(dictionary, file_path):
    json_object = json.dumps(dictionary, indent=4)
    file_writer(file_path, json_object)


def get_absolute_path(obj_path, folder_path=None):
    if folder_path:
        path = (Path(DIR) / '..' / folder_path / obj_path).resolve()
    else:
        path = (Path(DIR) / '..' / obj_path).resolve()
    return path
