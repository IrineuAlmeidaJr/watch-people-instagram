import os
from datetime import date

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from utils.LoadData import LoadData


def create_dataframe(current_date, users):
    dir_file = './data/users_instagram.xlsx'
    if os.path.isfile(dir_file):
        df = pd.read_excel('./data/users_instagram.xlsx')
        new_df = pd.DataFrame(list(map(lambda b: [b.Id, b.Name, b.Followers], users)))
        df[current_date] = new_df[2]
    else:
        df = pd.DataFrame(list(map(lambda b: [b.Id, b.Name, b.Followers], users)))
        df.columns = ['Id', 'Nome', current_date]

    print(df)
    return df


def create_graphic(brothers):
    dataframe_name_img = pd.DataFrame(list(map(lambda b: [b.Name, (int(b.Followers / 1000))], brothers)))
    dataframe_name_img.columns = ['Nome', 'Seguidores']
    sns.set(rc={'figure.figsize': (20, 10)})
    graphic = sns.barplot(
        x=dataframe_name_img["Seguidores"],
        y=dataframe_name_img['Nome'],
        data=dataframe_name_img
    )
    graphic.bar_label(graphic.containers[0])
    plt.show()
    return graphic.get_figure()


# def write_documents(current_date, brothers, dataframe, graphic_figure):
def write_documents(current_date, users, dataframe):
    dataframe.to_excel('./data/users_instagram.xlsx', index=False)
    # graphic_figure.savefig(f'../data/bbb_instagram.png')
    with open(f'./backup/users_instagram_{current_date}.txt', "w") as file:
        for item in users:
            file.write(f'{item}')


def main():
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

    current_date = str(date.today())
    # users_instagram = LoadData.load_data_file()
    users_instagram = LoadData.load_data_intagram()
    dataframe = create_dataframe(current_date, users_instagram)
    # graphic_figure = create_graphic(users_instagram)
    # write_documents(current_date, users_instagram, dataframe, graphic_figure)
    write_documents(current_date, users_instagram, dataframe)


if __name__ == "__main__":
    main()
