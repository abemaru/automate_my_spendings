from src.download_csv import download_from_rakuten
from src.create_ui import writer
from src.clean_tmp import clean_tmp


if __name__ == "__main__":
    download_from_rakuten()
    writer()
    clean_tmp()
    print("testing!")