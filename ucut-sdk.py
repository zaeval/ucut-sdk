# This is a sample Python script.
import requests
from requests import Response


class UcutManager:
    BASE_URL = "https://service.ucut.in/api/shorturl"

    def __init__(self, api_key: str):
        self._api_key = api_key

    def __str__(self):
        return "< UcutManager: {} >".format(self._api_key)

    def __repr__(self):
        return "< UcutManager: {} >".format(self._api_key)

    # TODO: link 생성 api 연동 sdk
    def createLink(self,
                   origin: str,
                   key: str = None,
                   alias: str = None,
                   author: int = None,
                   private: bool = None,
                   password: str = None) -> Response:
        return requests.post("{BASE_URL}/{PATH}/".format(
            BASE_URL=self.BASE_URL, PATH="/link"
        ),
            headers={
                'X-Api-Key': self._api_key
            },
            data={
                "key": key,
                "alias": alias,
                "author": author,
                "origin": origin,
                "private": private,
                "password": password
            })

    # TODO: link 가져오기 sdk
    def getLink(self, key: str = None, alias: str = None, origin: str = None, origin__contains: str = None):
        params = {}
        if key != None:
            params["key"] = key
        if alias != None:
            params["alias"] = alias
        if origin != None:
            params["origin"] = origin
        if origin__contains != None:
            params["origin__contains"] = origin__contains

        return requests.get("{BASE_URL}/{PATH}/".format(
            BASE_URL=self.BASE_URL, PATH="link"
        ),
            headers={
                'X-Api-Key': self._api_key
            },
            params=params)

    # TODO: authentication 요청 연동 sdk
    def authentication(self, id: str, password: str):
        return requests.get("{BASE_URL}/{PATH}/".format(
            BASE_URL=self.BASE_URL, PATH="link/{ID}/authentication".format(ID=id)
        ),
            headers={
                'X-Api-Key': self._api_key,
                'X-Password': password
            })
