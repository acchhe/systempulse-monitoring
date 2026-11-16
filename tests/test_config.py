import json
from src.systempulse.config import load_config
import pytest

def test_load_config(tmp_path):

    file_path = tmp_path / "test_config.json"

    with open(file_path,"w") as jsonFile:

        urls = {"websites" : ["https://example.com", "https://github.com", "https://python.org"]}

        json.dump(urls,jsonFile)

    
    result = load_config(file_path)

    assert result['websites'] == urls['websites']


def test_file_not_found(tmp_path):

    file_path = tmp_path / "notExist.json"

    with pytest.raises(FileNotFoundError):
        load_config(file_path)



def test_invalid_json(tmp_path):

    file_path = tmp_path / "file.json"

    file_path.write_text('{"websites": [}', encoding="utf-8")

    with pytest.raises(json.JSONDecodeError):
        load_config(file_path)


def test_websites_must_be_list(tmp_path):

    file_path = tmp_path / "test_config.json"

    file_path.write_text('{"websites": "https://example.com"}')

    with pytest.raises(ValueError):
        load_config(file_path)


def test_missing_website_key(tmp_path):


    file_path = tmp_path / "test_config.json"

    file_path.write_text(
        '{"urls" : "https://example.com"}'
    )

    with pytest.raises(ValueError):
        load_config(file_path)

