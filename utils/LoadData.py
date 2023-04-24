from config.ConfigInstagram import ConfigInstagram
from model.User import User


class LoadData:
    @staticmethod
    def load_data_intagram():
        search_instagram = ConfigInstagram()
        list_users_instagram = search_instagram.load()

        return list_users_instagram

