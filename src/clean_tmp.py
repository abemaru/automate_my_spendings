import os
import src.helper as sh

def clean_tmp():
    file_list = [file for file in os.listdir("./tmp/") if ".csv" in file]
    print(file_list)

    for file in file_list:
        file_path = os.path.join(sh.DOWNLOAD_DIR, file)
        print(f"deleting ... {file_path}")
        os.remove(file_path)
    