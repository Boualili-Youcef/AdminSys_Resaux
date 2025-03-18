import os

def create_test_tree(base_dir):
    directories = [
        "folder1",
        "folder1/subfolder1",
        "folder2",
        "folder2/subfolder2",
        "folder3"
    ]
    
    for dir in directories:
        os.makedirs(os.path.join(base_dir, dir), exist_ok=True)

    files = [
        "folder1/file1.txt",
        "folder1/subfolder1/file2.txt",
        "folder2/file3.txt",
        "folder2/subfolder2/file4.txt",
        "folder3/file5.txt"
    ]
    
    for file in files:
        file_path = os.path.join(base_dir, file)
        with open(file_path, "w") as f:
            f.write(f"Contenu de {file}\n")

    print(f"Arborescence de test créée dans : {base_dir}")

if __name__ == "__main__":
    base_dir = "test_directory"
    create_test_tree(base_dir)
