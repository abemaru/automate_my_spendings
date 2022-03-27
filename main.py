from distutils.command.clean import clean
from src.download_csv import *
from src.clean_tmp import *

if __name__ == "__main__":
    download_from_rakuten()
    clean_tmp()
    print("testing!")