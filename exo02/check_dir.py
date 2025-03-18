import os
import sys

def check_files(directory, threshold):
    file_count = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        file_count += len(filenames)
        if file_count > threshold:
            return -1
    return 0

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 check_dir.py <directory> <threshold>")
        sys.exit(1)

    directory = sys.argv[1]
    threshold = int(sys.argv[2])

    result = check_files(directory, threshold)

    if result == -1:
        print(f"Le répertoire {directory} contient plus de {threshold} fichiers.")
    else:
        print(f"Le répertoire {directory} ne dépasse pas {threshold} fichiers.")
