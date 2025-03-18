import psutil
import time

def monitor_system():
    while True:
        # Utilisation du CPU en pourcentage
        cpu_usage = psutil.cpu_percent(interval=1)

        # Utilisation de la mémoire en pourcentage
        memory_info = psutil.virtual_memory()
        memory_usage = memory_info.percent

        # Utilisation de l'espace disque en pourcentage
        disk_info = psutil.disk_usage('/')
        disk_usage = disk_info.percent

        # Affichage des informations
        print(f"Utilisation du CPU : {cpu_usage}%")
        print(f"Utilisation de la mémoire : {memory_usage}%")
        print(f"Utilisation de l'espace disque : {disk_usage}%")
        print('-' * 50)

        # Attendre 5 secondes avant de répéter
        time.sleep(5)

if __name__ == '__main__':
    monitor_system()
