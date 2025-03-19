import os
import sys

def check_files(directory, seuil):
    file_count = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        file_count += len(filenames)
        if file_count > seuil:
            return -1
    return 0

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 check_dir.py <directory> <seuil>")
        sys.exit(1)

    directory = sys.argv[1]
    seuil = int(sys.argv[2])

    result = check_files(directory, seuil)

    if result == -1:
        print(f"Le répertoire {directory} contient plus de {seuil} fichiers.")
        sys.exit(-1)
    else:
        print(f"Le répertoire {directory} ne dépasse pas {seuil} fichiers.")
        sys.exit(0)
