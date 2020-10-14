import json


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


def get_fixture_content(payload_filename):
    """
    Given a fixture filename, returns its content.
    :param payload_filename:    String      Name of the payload to load.
    :return:                    Dict        Payload loaded as a dict
    """
    file_content = file_reader(payload_filename)

    return json.loads(file_content)


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
