import instaloader
from model.User import User


class ConfigInstagram:

    @staticmethod
    def load():
        username = 'irineu.almeida.jr@icloud.com'
        bot = instaloader.Instaloader()
        bot.interactive_login(username)
        profile = instaloader.Profile

        pos_read = 0

        list_users_instagram = []
        with open(f'./data/list_users_instagram.txt', "r") as file:
            try:
                for item in file:
                    if item.strip() != '':
                        user = item.split(',')
                        user = User(
                            user[0],
                            user[1],
                            user[2],
                            int(profile.from_username(bot.context, user[2].strip()).followers),
                            user[3]
                        )
                        list_users_instagram.append(user)

                # while pos_read < len(list_users_instagram):
                #     list_users_instagram[pos_read].Followers = int(profile.from_username(
                #         bot.context, list_users_instagram[pos_read].Followers).followers)
                #     pos_read += 1

            except Exception as e:
                bot = instaloader.Instaloader()
                bot.interactive_login(username)

                print('EXECPTION -> ', e)

        return list_users_instagram
