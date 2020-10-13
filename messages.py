from random import randrange


def get_random_prompt_message():
    msgs = [
        "What do you want from me?", "What Shall We Do Now?", "Is there anybody in there?"
    ]
    return _get_random_msg(msgs)


def get_random_exit_message():
    msgs = [
        "Goodbye, blue sky.", "Don't leave me now...", "Goodbye, cruel world.",
        "Things left unsaid...", "Stop.", "Boom boom, bang bang, lie down you're dead."
    ]
    return _get_random_msg(msgs)


def _get_random_msg(msgs):
    return msgs[randrange(0, len(msgs))]
