import os
import glob
import pandas as pd

import src.helper as sh

from src.download_csv import Rakuten
from src.streamlit_app import writer


def read_all_files():
    all_files = glob.glob(sh.DOWNLOAD_DIR + "*.csv")
    tmp = []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        tmp.append(df)
    return pd.concat(tmp, axis=0, ignore_index=True)


if __name__ == "__main__":
    master_card = Rakuten.mastercard()
    master_card.execute_download()

    visa = Rakuten.visacard()
    visa.execute_download()

    if sh.RUN_TIME == "LOCAL":
        # streamlit
        writer()
        pass
    if sh.RUN_TIME == "CLOUD":
        # flask
        pass
    