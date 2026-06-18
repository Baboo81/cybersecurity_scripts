import subprocess  # Permet d'exécuter des commandes système
import platform    # Permet de détecter le système d'exploitation
import json        # Pour stocker les informations dans un fichier JSON

# Base du réseau local (réseau 192.168.1.0/24)
network = "192.168.0."

# Liste qui contiendra les IP actives
active_hosts = []

# Détection du système d'exploitation (Windows / Linux / macOS)
os_name = platform.system()


# Boucle sur toutes les IP possibles du réseau
for i in range(1, 255):
    # Construction de l'adresse IP complète
    ip = network + str(i)

    # Commande ping adaptée au système d'exploitation 
    if os_name == "Windows":
        command = ["ping", "-n", "1", "-w", "1000", ip]
        # -n 1    → envoie 1 paquet
        # -w 1000 → timeout (en millisecondes)
    else:
        command = ["ping", "-c", "1", "-W", "1", ip]
        # -c 1 → 1 paquet
        # -W 1 → timeout (en secondes)

    # Exécution de la commande ping sans afficher la sortie 
    result = subprocess.run(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    # Si returncode == 0, la machine répond ;
    if result.returncode == 0:
        print(f"🟢 {ip} est actif")
        active_hosts.append(ip)


# Enregistrement des résultats dans un fichier JSON
with open("network_map.json", "w") as file:
    json.dump(active_hosts, file, indent=4)
