import os
import subprocess

def get_user_dirs():
    user_dirs = []
    with open("/etc/passwd") as f:
        for line in f:
            parts = line.split(":")
            if parts[3] == "1000":  
                user_dirs.append(parts[5])
    return user_dirs

def check_all_user_dirs(seuil):
    user_dirs = get_user_dirs()
    problematic_users = []

    for user_dir in user_dirs:
        result = subprocess.run(['python3', 'check_dir.py', user_dir, str(seuil)], capture_output=True)
        if result.returncode == 255:
            problematic_users.append(user_dir)
    
    if problematic_users:
        print("Répertoires problématiques :")
        for dir in problematic_users:
            print(dir)
    else:
        print("Aucun répertoire problématique trouvé.")

if __name__ == "__main__":
    try:
        seuil = int(input("Entrez le seuil de fichiers : "))
        if seuil < 0:
            print("Erreur : le seuil doit être un nombre entier positif.")
        else:
            check_all_user_dirs(seuil)
    except ValueError:
        print("Erreur : veuillez entrer un nombre entier valide pour le seuil.")
