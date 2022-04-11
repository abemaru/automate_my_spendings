import os
import glob
from tkinter.tix import Tree
from matplotlib.pyplot import axis
import pandas as pd

import src.helper as sh

from src.download_csv import Rakuten
from src.create_ui import writer
from src.clean_tmp import clean_tmp


def read_all_files():
    all_files = glob.glob(sh.DOWNLOAD_DIR + "*.csv")
    tmp = []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        tmp.append(df)
    return pd.concat(tmp, axis=0, ignore_index=True)


if __name__ == "__main__":
    master_card = Rakuten.mastercard()
    master_card.download_csv()
    # download_from_rakuten()
    # df = read_all_files()
    # writer(df)
    # #clean_tmp()
    