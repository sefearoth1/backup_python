# Importation de la bibliothèque Paramiko pour la gestion SSH
import paramiko
import datetime

# Informations de connexion SSH
hostname = "adresse_ip_ou_nom_de_domaine"  # Adresse IP ou nom de domaine du serveur distant
port = 22  # Port SSH par défaut
username = "votre_utilisateur_ssh"  # Nom d'utilisateur SSH pour la connexion
password = "votre_mot_de_passe_ssh"  # Mot de passe SSH de l'utilisateur

# Commande de sauvegarde à exécuter sur le serveur distant
backup_command = "commande_de_sauvegarde"  # La commande à exécuter pour effectuer la sauvegarde

# Chemin où sauvegarder les fichiers sur le serveur distant
backup_directory = "/chemin/vers/dossier_de_sauvegarde/"

# Nom du fichier de sauvegarde basé sur la date et l'heure actuelles
current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")  # Formatage de la date et de l'heure actuelles
backup_filename = f"backup_{current_time}.tar.gz"  # Nom du fichier de sauvegarde combinant "backup_" et l'horodatage

# Connexion SSH
ssh_client = paramiko.SSHClient()  # Création d'une instance de client SSH
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Politique pour gérer les clés d'hôte manquantes
ssh_client.connect(hostname, port, username, password)  # Connexion au serveur distant avec les informations fournies

# Exécution de la commande de sauvegarde sur le serveur distant
stdin, stdout, stderr = ssh_client.exec_command(backup_command)  # Exécution de la commande et récupération des flux d'entrée/sortie

# Attendre que la commande soit terminée et récupérer le code de sortie
stdout.channel.recv_exit_status()

# Téléchargement du fichier de sauvegarde depuis le serveur distant
sftp = ssh_client.open_sftp()  # Création d'une session SFTP pour le transfert de fichiers
sftp.get(f"{backup_directory}/{backup_filename}", backup_filename)  # Téléchargement du fichier de sauvegarde vers le dossier local
sftp.close()  # Fermeture de la session SFTP

# Fermeture de la connexion SSH
ssh_client.close()

# Affichage du message de réussite de la sauvegarde
print("Sauvegarde terminée avec succès!")
