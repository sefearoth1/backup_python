import paramiko

# Informations de connexion SSH
hostname = "adresse_ip_ou_nom_de_domaine"  # Adresse IP ou nom de domaine du serveur distant
port = 22  # Port SSH par défaut
username = "votre_utilisateur_ssh"  # Nom d'utilisateur SSH pour la connexion
password = "votre_mot_de_passe_ssh"  # Mot de passe SSH de l'utilisateur

# Chemin du fichier de sauvegarde à restaurer
backup_filename = "backup_YYYYMMDDHHMMSS.tar.gz"  # Remplacez YYYYMMDDHHMMSS par l'horodatage du fichier de sauvegarde

# Commande de restauration à exécuter sur le serveur distant
restore_command = f"commande_de_restauration {backup_filename}"  # La commande pour effectuer la restauration avec le fichier de sauvegarde

# Connexion SSH
ssh_client = paramiko.SSHClient()  # Création d'une instance de client SSH
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Politique pour gérer les clés d'hôte manquantes
ssh_client.connect(hostname, port, username, password)  # Connexion au serveur distant avec les informations fournies

# Copie du fichier de sauvegarde vers le serveur distant
sftp = ssh_client.open_sftp()  # Création d'une session SFTP pour le transfert de fichiers
sftp.put(backup_filename, backup_filename)  # Copie du fichier de sauvegarde sur le serveur distant
sftp.close()  # Fermeture de la session SFTP

# Exécution de la commande de restauration sur le serveur distant
stdin, stdout, stderr = ssh_client.exec_command(restore_command)  # Exécution de la commande et récupération des flux d'entrée/sortie

# Attendre que la commande soit terminée et récupérer le code de sortie
stdout.channel.recv_exit_status()

# Suppression du fichier de sauvegarde restauré sur le serveur distant
ssh_client.exec_command(f"rm {backup_filename}")  # Suppression du fichier de sauvegarde restauré

# Fermeture de la connexion SSH
ssh_client.close()

# Affichage du message de réussite de la restauration
print("Restauration terminée avec succès!")
