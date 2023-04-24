import pandas as pd
import numpy as np


class User:

    def __init__(self, id, name, instagram_username, followers, url_image):
        self.__id = id
        self.__name = name
        self.__instagram_username = instagram_username
        self.__followers = followers
        self.__url_image = url_image

    @property
    def Id(self):
        return self.__id

    @property
    def Name(self):
        return self.__name

    @property
    def Instagram_username(self):
        return self.__instagram_username

    @property
    def Followers(self):
        return self.__followers

    @Followers.setter
    def Followers(self, value):
        self.__followers = value

    @property
    def Url_image(self):
        return self.__url_image

    def __str__(self):
        return f'{self.Id}, {self.Name},{self.Instagram_username},' \
               f'{self.Followers},{self.Url_image}'

    def __repr__(self):
        return {
            "id": self.Id,
            "name": self.Name,
            "instagram_username": self.Instagram_username,
            "followers": self.Followers,
            "url_image": self.Url_image.rstrip()
        }



