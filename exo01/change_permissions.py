import os
import stat
import sys

def change_permissions(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                os.chmod(file_path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IROTH)
                print(f"Permissions changées pour {file_path}")

if __name__ == "__main__":
    directory = sys.argv[1]
    change_permissions(directory)
