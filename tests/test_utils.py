from src.utils import read_json


def test_read_json(path, data):
    assert read_json(path) == data
