import json
import os
import pytest

from bot import get_bot_conf

CONFIGS = {
    'filename': 'examples.json',
    'min_channel_num': 2,
}


def test_conf_file_exists():
    conf_file = os.path.abspath(CONFIGS['filename'])
    assert conf_file in os.listdir()


def test_conf_file_has_token_key():
    token, _ = get_bot_conf()
    assert token is not None


def test_conf_file_has_channels_key():
    _, channels = get_bot_conf()
    assert channels is not None


def test_conf_file_has_channels_data():
    min_data = CONFIGS['min_channel_num']
    _, channels = get_bot_conf()
    for message_data in channels:
        assert len(message_data) == min_data
