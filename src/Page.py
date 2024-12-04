import hashlib
import json
import os
from pathlib import Path
from typing import Dict, List, TypeAlias

import requests
from bs4 import BeautifulSoup
from dotenv import dotenv_values
from requests.auth import HTTPBasicAuth

ResponseJSON: TypeAlias = Dict[str, List[Dict[str, str]]]
dev_cache_path = "../.dev_cache"
env = dotenv_values("../.env")


class Page:
    _response: ResponseJSON

    def __init__(self, url: str) -> None:
        cached = self._get_from_dev_cache(url)

        if cached is not None:
            self._response = cached
        else:
            self._response = self._get_page(url)

        if not isinstance(self._response["results"][0]["content"], str):
            raise Exception("Unexpected shape!")

    def __str__(self) -> str:
        return self._response["results"][0]["content"]

    @property
    def soup(self) -> BeautifulSoup:
        return BeautifulSoup(str(self), "html.parser")

    def _get_from_dev_cache(self, url: str) -> ResponseJSON | None:
        dev_cache = Path(dev_cache_path)
        if not dev_cache.is_dir():
            os.mkdir(dev_cache)
            return None

        file_name = hashlib.sha256(url.encode("utf-8")).hexdigest() + ".json"
        file_path = f"{dev_cache_path}/{file_name}"
        file = Path(file_path)
        if file.is_file():
            f = open(file_path, "r")
            file_json: ResponseJSON = json.loads(f.read())
            return file_json

        return None

    def _get_page(self, url: str) -> ResponseJSON:
        OXY_USERNAME = env["OXY_USERNAME"]
        OXY_PASSWORD = env["OXY_PASSWORD"]

        if type(OXY_USERNAME) is not str or type(OXY_PASSWORD) is not str:
            raise Exception(
                "Oxylabs credentials not found. Add them to your .env file!"
            )

        print("Fetching url:", url)
        headers = {
            "Content-Type": "application/json",
        }
        payload = {
            "source": "universal_ecommerce",
            "url": url,
        }
        response: ResponseJSON = requests.post(
            url="https://realtime.oxylabs.io/v1/queries",
            auth=HTTPBasicAuth(OXY_USERNAME, OXY_PASSWORD),
            headers=headers,
            data=json.dumps(payload),
        ).json()

        if not isinstance(response["results"][0]["content"], str):
            raise Exception("Response was unexpected shape!")

        file_name = hashlib.sha256(url.encode("utf-8")).hexdigest() + ".json"
        file_path = f"{dev_cache_path}/{file_name}"
        with open(file_path, "w") as f:
            f.write(json.dumps(response))

        return response
